cd ..
git clone https://github.com/CMU-Perceptual-Computing-Lab/openpose

cd openpose
git submodule update --init --recursive --remote

if [ "$(uname)" == "Darwin" ]; then
  brew install opencv
elif [ "$(uname)" == "Linux" ]; then
  sudo apt-get install libunwind-dev libgoogle-glog-dev
fi

mkdir build
cd build
cmake \
  -DUSE_CUDNN=OFF \
  -DBUILD_PYTHON=ON \
  ..
make -j

pip install -U opencv-python
