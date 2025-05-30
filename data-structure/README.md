# Get Started

```bash
mkdir build && cd build && cmake .. && -DCMAKE_INSTALL_PREFIX=dist
```
# How to run

```bash
cd build
make
./main.out
```
# How to deploy

- Add implementation files to `CMakeLists.txt`
- Run the following command:

```bash 
cd build
make install
```

# How to use package

```bash
g++ test.cpp -I./include -L./lib -l:libapp.a -o app.out
./app.out
```