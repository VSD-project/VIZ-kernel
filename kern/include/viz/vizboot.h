//VIZ kernel loading protocol

#ifndef VIZ_VIZBOOT_H
#define VIZ_VIZBOOT_H

#include <viz/stdint.h>

typedef struct {
    void* addr;
    int width; //max x
    int height; // max y
    int pitch; // size of max y in bytes
    int pixel_width; //size of pixel in bytes
    int depth; //bits of colour
}vizboot_frambuffer_t;


typedef struct {
    int magic; //should be 0xFACDFACD
    vizboot_frambuffer_t framebuffer;
}vizboot_t;

void k_setup(vizboot_t *vizboot);

#endif