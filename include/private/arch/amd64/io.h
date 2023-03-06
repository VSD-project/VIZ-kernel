/*
defintions for handling and using the io bus on x86 cpus
*/

#ifndef VIZ_PRIVATE_ARCH_X86_IO_H
#define VIZ_PRIVATE_ARCH_X86_IO_H

void x86_outb(char addr, char byte);
char x86_inb(char addr);

#endif