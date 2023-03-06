# VIZ kernel
kernel for the VSD project <br/>

## supported archs
- [x] amd64 (WIP)
- [ ] aarch64 (planned)
- [ ] riscv64 (planned)

Note: i686 is dead and has been for 2 decades, all i686 legacy crud that amd64 needs is handled in amd64 and a seperate arch will not be made <br/>

## supported boot protocols
- [x] limine (WIP, calls internal vizboot functions)
- [ ] vizboot

Currently the kernel gets bootstrapped by a chainloader module that translates another protocol to the vizboot protocol and parses it to the kernel
