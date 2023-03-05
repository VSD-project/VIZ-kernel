#DO NOT RUN, THIS IS JUST FOR GITHUB WORKFLOWS

sudo apt install libgmp-dev libmpfr-dev libmpc-dev

cd ~
mkdir toolchain
mkdir build-gcc
mkdir build-bin
wget https://ftp.gnu.org/gnu/binutils/binutils-2.40.tar.xz -O binutils.tar.xz
wget https://ftp.gnu.org/gnu/gcc/gcc-12.2.0/gcc-12.2.0.tar.xz -O gcc.tar.xz
tar -xf binutils.tar.xz
tar -xf gcc.tar.xz

mv gcc-12.2.0 gcc
mv binutils-2.40 bin

cd build-bin
../bin/configure --prefix=/home/runner/toolchain --target=x86_64-none-elf --with-sysroot --disable-nls --disable-werror
make -j 2
sudo make install -j 2

cd ../build-gcc
../gcc/configure --prefix=/home/runner/toolchain --target=x86_64-none-elf --disable-nls --enable-languages=c --without-headers
make -j 2
sudo make install -j 2

export PATH="$HOME/toolchain/bin:$PATH"

echo $PATH