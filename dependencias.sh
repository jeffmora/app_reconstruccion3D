#!/bin/bash

# Preparación de la maquina para la constucción de las dependencias.
sudo apt-get update -qq && sudo apt-get install -qq
sudo apt-get -y install git cmake
sudo apt-get install libpng-dev libjpeg-dev libtiff-dev libxxf86vm1 libxxf86vm-dev libxi-dev libxrandr-dev libglu1-mesa-dev
main_path=´pwd´

#Descarga e instalaamos la dependencias requeridas.
#OpenMVG (Requerido)
git clone --recursive https://github.com/openMVG/openMVG.git
mkdir openMVG_Build && cd openMVG_Build
cmake -DCMAKE_BUILD_TYPE=RELEASE ../openMVG/src/
cmake --build . --target install

#Eigen (Requerido)
git clone https://gitlab.com/libeigen/eigen.git --branch 3.4
mkdir eigen_build && cd eigen_build
cmake . ../eigen
make && sudo make install
cd ..

#Boost (Requerido)
sudo apt-get -y install libboost-iostreams-dev libboost-program-options-dev libboost-system-dev libboost-serialization-dev

#OpenCV (Requerido).
sudo apt-get -y install libopencv-dev

#CGAL (Requerido)
sudo apt-get -y install libcgal-dev libcgal-qt5-dev

#VCGLib (Requerido)
git clone https://github.com/cdcseacave/VCG.git vcglib

#Ceres (Opcional)
sudo apt-get -y install libatlas-base-dev libsuitesparse-dev
git clone https://ceres-solver.googlesource.com/ceres-solver ceres-solver
mkdir ceres_build && cd ceres_build
cmake . ../ceres-solver/ -DMINIGLOG=ON -DBUILD_TESTING=OFF -DBUILD_EXAMPLES=OFF
make -j2 && sudo make install
cd ..

#OpenMVS (Requerido)
git clone https://github.com/cdcseacave/openMVS.git openMVS
mkdir openMVS_build && cd openMVS_build
cmake . ../openMVS -DCMAKE_BUILD_TYPE=Release -DVCG_ROOT="$main_path/vcglib"
make -j2 && sudo make install

#MeshLab (Requerido)
sudo apt-get install meshlab