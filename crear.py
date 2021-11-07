#!/venv/bin/ python

# Este scrpit permite ejecutar la reconstrucción del modelo bajo la técnica de fotogrametría,
# los pasos de esta técnica van desde anilizar cada una de la imagenes importadas, hasta
# agregar las texturas al modelo computarizado.

# ==================================== IMPORTAR LIBRERIAS ====================================
# Importamos librerias propias del sistama para trabajar. 
import os
import subprocess
import sys
from os.path import expanduser

# ===== BASE DE DATOS DE SENSORES =====
# Busca el archivo de base de datos del sensor en todo el sistema y devuelve su ruta.
def database_sensor():
    usuariopc = expanduser("~")
    data = "sensor_width_camera_database.txt"
    buscar = subprocess.run(["find", usuariopc, "-name", data], capture_output=True)
    buscar2 = os.path.split(buscar.stdout.decode())[0]
    par_sensor = os.path.join(buscar2, data)
    return par_sensor

# ===== MESHLAB ====
# Llama a Meshlab para visualizar los resultados.
def meshlab(selresultado):
    pVis = subprocess.Popen(["meshlab", selresultado])
    pVis.wait()

# ===== Core de reconstruccion 3D ====
# Captura y asigna cada uno de los parametros de configuracion. Llama cada una de las funciones de las dependencias
# de OpenMVG y OpenMVS.
def run(*args):
    dir_entrada = args[0]
    dir_coincidencias = args[1]
    par_sensor = args[2]
    dir_reconstruccion = args[3]
    metodo_descriptor = args[4]
    definicion = args[5]
    modelo_geometrico = args[6]
    metodo_coincidencia = args[7]
    relacion_distancia = args[8]
    refinamiento_intrinsecos = args[9]
    metodo_triangulacion = args[10]
    metodo_recesion = args[11]
    avance = args[12]
    dir_cnd_geometricas = args[13]
    dir_pistas = args[14]
    imagenparA = args[15]
    imagenparB = args[16]

    if avance == 1:
        # Extraccion y organizacion de parametros intrincecos de cada imagen.
        print("\n 1. Extraer parametros Exif de cámara...")
        pIntrisecos = subprocess.Popen([
            "openMVG_main_SfMInit_ImageListing", 
            "-i", dir_entrada, 
            "-o", dir_coincidencias, 
            "-d", par_sensor, 
            "-c", "1"])
        pIntrisecos.wait()
        return 2
    elif avance == 2:
        # Extraccion de caracteristicas de cada imagen.
        print("\n 2. Calcular características...")
        pCarater = subprocess.Popen([
            "openMVG_main_ComputeFeatures",
            "-i", dir_coincidencias+"/sfm_data.json",
            "-o", dir_coincidencias,
            "-f", "1",
            "-m", metodo_descriptor,
            "-p", definicion,
            "-n", "0"])
        pCarater.wait()
        # Conversion de resultados obtenidos a formato .svg para visualizacion
        pPuntos = subprocess.Popen([
            "openMVG_main_exportKeypoints",
            "-i", dir_coincidencias+"/sfm_data.json",
            "-d", dir_coincidencias,
            "-o", dir_coincidencias])
        pPuntos.wait()
        return 3
    elif avance == 3:
        # Calculo de coincidencias entre pares de imagenes, compara cada vista disponible para buscar la mayor cantidad de similitudes
        # y definir la mejor posicion de la vista, asimismo asocia una ubicacion de la camara en el medio.
        print("\n 3. Calcular coincidencias...")
        pCoincid = subprocess.Popen([
            "openMVG_main_ComputeMatches", 
            "-i", dir_coincidencias+"/sfm_data.json", 
            "-o", dir_coincidencias,
            "-f", "1", 
            "-r", relacion_distancia,
            "-g", modelo_geometrico,
            "-n", metodo_coincidencia])
        pCoincid.wait()
        # Exportar coincidencias para visualizacion en formato .svg
        pCoincid = subprocess.Popen([
            "openMVG_main_exportMatches", 
            "-i", dir_coincidencias+"/sfm_data.json",
            "-d", dir_coincidencias,
            "-m", dir_coincidencias+"/matches.putative.bin",
            "-o", dir_cnd_geometricas])
        pCoincid.wait()
        # Exportar pistas para visualizacion en formato .svg
        pCoincid = subprocess.Popen([
            "openMVG_main_exportTracks", 
            "-i", dir_coincidencias+"/sfm_data.json",
            "-d", dir_coincidencias,
            "-m", dir_coincidencias+"/matches.putative.bin",
            "-o", dir_pistas])
        pCoincid.wait()
        return 4
    elif avance == 4:
        # Generacion de la nube de puntos con base en las caracteristicas de las imagenes y posicion halladas previamente. Presenta 
        # la primera aproximacion de la reconstruccion.
        print("\n 4. Reconstrucción incremental SfM...")
        pRecons = subprocess.Popen([
            "openMVG_main_IncrementalSfM", 
            "-i", dir_coincidencias+"/sfm_data.json", 
            "-m", dir_coincidencias, 
            "-o", dir_reconstruccion,
            "-a", imagenparA,
            "-b", imagenparB,
            "-c", "1",
            "-f", refinamiento_intrinsecos,
            "-t", metodo_triangulacion,
            "-r", metodo_recesion])
        pRecons.wait()
        return 5
    elif avance == 5:
        # Asigancion estimada de colores a cada punto disponible. Aún no es la final es solo una aproximación.
        print("\n 5. Colorear Estructura...")
        pRecons = subprocess.Popen([
            "openMVG_main_ComputeSfM_DataColor", 
            "-i", dir_reconstruccion+"/sfm_data.bin", 
            "-o", os.path.join(dir_reconstruccion,"colorized.ply")])
        pRecons.wait()
        return 6
    elif avance == 6:
        # Conversion de archivo necesario para procesamiento posterior.
        print("\n 6. Convesión de MVG a MVS...")
        pConver = subprocess.Popen([
            "openMVG_main_openMVG2openMVS", 
            "-i", dir_reconstruccion+"/sfm_data.bin", 
            "-o", dir_reconstruccion+"/scene.mvs", 
            "-d", dir_reconstruccion+"/scene_undistorted_images",
            "-n", "0"])
        pConver.wait()
        return 7
    elif avance == 7:
        # Densificacion de nube de puntos resultante del paso 4.
        print("\n 7. Creación de nube de puntos densa...")
        pDenPointCloud = subprocess.Popen([
            "/usr/local/bin/OpenMVS/DensifyPointCloud", 
            dir_reconstruccion+"/scene.mvs", 
            "-w", dir_reconstruccion, 
            "--max-threads", "0",
            "--number-views", "0"])
        pDenPointCloud.wait()
        return 8
    elif avance == 8:
        # Creacion de la malla o cirre de puntos, primera etapa de modelado.
        print("\n 8. Reconstrucción de malla basada en nube de puntos, creación de modelo 3D...")
        pRecMesh = subprocess.Popen([
            "/usr/local/bin/OpenMVS/ReconstructMesh", 
            dir_reconstruccion+"/scene_dense.mvs", 
            "-w", dir_reconstruccion,
            "--max-threads", "0"])
        pRecMesh.wait()
        return 9
    elif avance == 9:
        # Filtracion de malla para corregir y/o eliminar nodos erroneos.
        print("\n 9. Refinamiento del modelo calculado...")
        pRefMesh = subprocess.Popen([
            "/usr/local/bin/OpenMVS/RefineMesh", 
            dir_reconstruccion+"/scene_dense_mesh.mvs", 
            "-w", dir_reconstruccion,
            "--max-threads", "0",
            "--max-face-area", "16"])
        pRefMesh.wait()
        return 10
    elif avance == 10:
        # Extraccion y adicion de texturas al modelo final basandose en las imagenes iniciales.
        print("\n 10. Texturizado de modelo final...")
        pTexMesh = subprocess.Popen([
            "/usr/local/bin/OpenMVS/TextureMesh", 
            dir_reconstruccion+"/scene_dense_mesh_refine.mvs", 
            "-w", dir_reconstruccion,
            "--max-threads", "0"])
        pTexMesh.wait()
        return 11