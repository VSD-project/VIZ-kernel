//start kernel with limine

#include "limine.h"
#include <viz/vizboot.h>

vizboot_t translated_protocol;



static volatile struct limine_framebuffer_request framebuffer_request = {
    .id = LIMINE_FRAMEBUFFER_REQUEST,
    .revision = 0
};

void _start(void) {
    if (framebuffer_request.response == 0) {for(;;);}
    if (framebuffer_request.response->framebuffer_count == 0) {for(;;);}

    translated_protocol.framebuffer->addr = framebuffer_request.response->framebuffers[0]->address;

    k_setup(&translated_protocol);

    for(;;);
}