cd ..
git clone https://github.com/CMU-Perceptual-Computing-Lab/openpose

cd openpose
git submodule update --init --recursive --remote

sudo apt-get install libunwind-dev libgoogle-glog-dev

mkdir build
cd build
cmake \
  -DUSE_CUDNN=OFF \
  -DBUILD_PYTHON=ON \
  ..
make -j

pip install -U opencv-python
