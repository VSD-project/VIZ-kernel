#DO NOT RUN, THIS IS JUST FOR GITHUB WORKFLOWS

cd ~
mkdir build-gcc
mkdir build-bin
wget https://ftp.gnu.org/gnu/binutils/binutils-2.40.tar.xz -O binutils.tar.xz
wget https://ftp.gnu.org/gnu/gcc/gcc-12.2.0/gcc-12.2.0.tar.xz -O gcc.tar.xz
tar -xf binutils.tar.xz
tar -xf gcc.tar.xz