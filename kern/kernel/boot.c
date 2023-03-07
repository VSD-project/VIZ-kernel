#include <viz/vizboot.h>
#include <viz/stdint.h>

void k_setup(vizboot_t *vizboot) {

    int* framebuffer = vizboot->framebuffer.addr;

    for (int y = 0; y < vizboot->framebuffer.height; y++) {
        for (int x = 0; x < vizboot->framebuffer.width; x++) {
            framebuffer[(x * vizboot->framebuffer.pixel_width) + (y * vizboot->framebuffer.width)] = 0x303040;
        }
    }


    for(;;);
}