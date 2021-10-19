# Este scrpit permite ejecutar la reconstrucción del modelo bajo la técnica de fotogrametría,
# los pasos de esta técnica van desde anilizar cada una de la imagenes importadas, hasta
# agregar las texturas al modelo computarizado.

# Importamos librerias propias del sistama para trabajar. 
import os
import subprocess
import sys

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

    if avance == 1:
        #Analisís y tratamiendo de imagenes con OPENMVG para la reconstrucción stereo de multiples vistas.
        print("\n 1. Extraer parametros Exif de cámara...")
        pIntrisecos = subprocess.Popen([
            "openMVG_main_SfMInit_ImageListing", 
            "-i", dir_entrada, 
            "-o", dir_coincidencias, 
            "-d", par_sensor, 
            "-c", "2"])
        pIntrisecos.wait()
        return 2
    elif avance == 2:
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
        return 3
    elif avance == 3:
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
        return 4
    elif avance == 4:
        print("\n 4. Reconstrucción incremental SfM...")
        pRecons = subprocess.Popen([
            "openMVG_main_IncrementalSfM", 
            "-i", dir_coincidencias+"/sfm_data.json", 
            "-m", dir_coincidencias, 
            "-o", dir_reconstruccion,
            "-c", "2",
            "-f", refinamiento_intrinsecos,
            "-t", metodo_triangulacion,
            "-r", metodo_recesion])
        pRecons.wait()
        return 5
    elif avance == 5:
        print("\n 5. Colorear Estructura...")
        pRecons = subprocess.Popen([
            "openMVG_main_ComputeSfM_DataColor", 
            "-i", dir_reconstruccion+"/sfm_data.bin", 
            "-o", os.path.join(dir_reconstruccion,"colorized.ply")])
        pRecons.wait()
        return 6
    elif avance == 6:
        # Convesión de MVG a MVS.
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
        # Proceso de reconstrucción final del modelo.
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
        print("\n 8. Reconstrucción de malla basada en nube de puntos, creación de modelo 3D...")
        pRecMesh = subprocess.Popen([
            "/usr/local/bin/OpenMVS/ReconstructMesh", 
            dir_reconstruccion+"/scene_dense.mvs", 
            "-w", dir_reconstruccion,
            "--max-threads", "0"])
        pRecMesh.wait()
        return 9
    elif avance == 9:
        print("\n 9. Reninamiento del modelo calculado...")
        pRefMesh = subprocess.Popen([
            "/usr/local/bin/OpenMVS/RefineMesh", 
            dir_reconstruccion+"/scene_dense_mesh.mvs", 
            "-w", dir_reconstruccion,
            "--max-threads", "0",
            "--max-face-area", "32"])
        pRefMesh.wait()
        return 10
    elif avance == 10:
        print("\n 10. Texturizado de modelo final...")
        pTexMesh = subprocess.Popen([
            "/usr/local/bin/OpenMVS/TextureMesh", 
            dir_reconstruccion+"/scene_dense_mesh_refine.mvs", 
            "-w", dir_reconstruccion,
            "--max-threads", "0"])
        pTexMesh.wait()
        return 11