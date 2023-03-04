/*
IBM PS/2 keyboard driver
*/

#include <viz/spinlock.h>

#if defined(__x86_64__) || defined(__i386__)

#include <private/arch/x86/io.h>

int driver_input_ibm_ps2_kbd_addr;

void driver_input_ibm_ps2_kbd_tx(char byte) {x86_outb(driver_input_IBM_ps2_kbd_addr, byte);}

void input_IBM_ps2_kbd_init(void) {
    input_IBM_ps2_kbd_addr = 0x60;
}

#else
#error ATEMPT TO BUILD PS2 KBD DRIVER ON UNSUPPORTED ARCH
#endif

