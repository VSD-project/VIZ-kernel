# viz kernel
Version 0.02 alpha

## differences from 0.01
Redesign of driver subsystem <br>
Designed to be scalable from smaller systems to larger systems (MCUs to servers) <br>
Unix like externally but may not internally handle the system like Unix <br>

## subdirs
```
bin - object files
config - kernel and build system configuration files
scripts - build system
viz - standard headers
arch - architecture specfic code and drivers
drivers - cross platform drivers (pci/e)
fs - handles filesystems, both real(drives) and virtual(devfs)
kernel - middle man code to bind driver/arch code to a standard api, also handles multiple protocols
```

## boot to userspace todo list
- [x] boot
- [ ] setup early tty console for kernel
- [ ]
- [ ]
- [ ]
- [ ]
- [ ]
- [ ]