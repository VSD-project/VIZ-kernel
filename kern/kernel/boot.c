#include <viz/vizboot.h>
#include <viz/stdint.h>

void k_setup(vizboot_t *vizboot) {
    
    unsigned long *framebuffer = (unsigned long*)vizboot->framebuffer->addr;

    framebuffer[0] = 255;
    framebuffer[1] = 255; 
    framebuffer[2] = 255;

    for(;;);
}