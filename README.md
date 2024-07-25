# Human Pose Detect

## Setup

```bash
conda create -n hpd python=3.10
conda activate hpd
./setup.sh
```

special editing on mac

```bash
edit ../openpose/build/caffe/src/openpose_lib-build/CMakeCache.txt
vecLib_INCLUDE_DIR:PATH=vecLib_INCLUDE_DIR-NOTFOUND
->
vecLib_INCLUDE_DIR:PATH=/Library/Developer/CommandLineTools/SDKs/MacOSX<your-version>.sdk/System/Library/Frameworks/Kernel.framework/Versions/A/Headers/vecLib
```

```bash
edit ../openpose/3rdparty/caffe/CMakeLists.txt
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fPIC -Wall -std=c++11")
->
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fPIC -Wall -std=c++17")
```
```
```
```
```

## Run

```bash
python demo.py
```

## Enjoy it~
