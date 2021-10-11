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

    #Analisís y tratamiendo de imagenes con OPENMVG para la reconstrucción stereo de multiples vistas.
    print("\n 1. Anlisís de intrinsecos...")
    pIntrisecos = subprocess.Popen(["openMVG_main_SfMInit_ImageListing", "-i", dir_entrada, "-o", dir_coincidencias, "-d", par_sensor])
    pIntrisecos.wait()

    print("\n 2. Calcular características...")
    pCarater = subprocess.Popen(["openMVG_main_ComputeFeatures", "-i", dir_coincidencias+"/sfm_data.json", "-o", dir_coincidencias, "-m", "SIFT"])
    pCarater.wait()

    print("\n 3. Calcular coincidencias...")
    pCoincid = subprocess.Popen(["openMVG_main_ComputeMatches", "-i", dir_coincidencias+"/sfm_data.json", "-o", dir_coincidencias])
    pCoincid.wait()

    print("\n 4. Reconstrucción incremental SfM...")
    pRecons = subprocess.Popen(["openMVG_main_IncrementalSfM", "-i", dir_coincidencias+"/sfm_data.json", "-m", dir_coincidencias, "-o", dir_reconstruccion])
    pRecons.wait()

    print("\n 5. Colorear Estructura...")
    pRecons = subprocess.Popen(["openMVG_main_ComputeSfM_DataColor", "-i", dir_reconstruccion+"/sfm_data.bin", "-o", os.path.join(dir_reconstruccion,"colorized.ply")])
    pRecons.wait()
    
    # Convesión de MVG a MVS.
    print("\n 6. Convesión de MVG a MVS...")
    pConver = subprocess.Popen(["openMVG_main_openMVG2openMVS", "-i", dir_reconstruccion+"/sfm_data.bin", "-o", dir_reconstruccion+"/scene.mvs", "-d", dir_reconstruccion+"/scene_undistorted_images"])
    pConver.wait()

    # Proceso de reconstrucción final del modelo.
    print("\n 7. Creación de nube de puntos densa...")
    pDenPointCloud = subprocess.Popen(["/usr/local/bin/OpenMVS/DensifyPointCloud", dir_reconstruccion+"/scene.mvs"])
    pDenPointCloud.wait()

    print("\n 8. Reconstrucción de malla basada en nube de puntos, creación de modelo 3D...")
    pRecMesh = subprocess.Popen(["/usr/local/bin/OpenMVS/ReconstructMesh", dir_reconstruccion+"/scene_dense.mvs"])
    pRecMesh.wait()

    print("\n 9. Reninamiento del modelo calculado...")
    pRefMesh = subprocess.Popen(["usr/local/bin/OpenMVS/RefineMesh", dir_reconstruccion+"/scene_dense_mesh.mvs"])
    pRefMesh.wait()

    print("\n 10. Texturizado de modelo final...")
    pTexMesh = subprocess.Popen(["/usr/local/bin/OpenMVS/TextureMesh", dir_reconstruccion+"/scene_dense_mesh_refine.mvs"])
    pTexMesh.wait()

    print("\n !Finalizado!")   