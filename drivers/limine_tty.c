//limine fb to virtual tty console
#include <viz/driver.h>
#include <viz/limine.h>

static volatile struct limine_framebuffer_request driver_limine_tty_framebuffer_request = {
    .id = LIMINE_FRAMEBUFFER_REQUEST,
    .revision = 0
};

int driver_limine_virt_tty_init(void) {
    if (driver_limine_tty_framebuffer_request.response == 0) {return 1;}//bootloader did not return a framebuffer

    int* fb = driver_limine_tty_framebuffer_request.response->framebuffers[0]->address;

    for (int y = 0; y < driver_limine_tty_framebuffer_request.response->framebuffers[0]->height; y++) {
        for (int x = 0; x < driver_limine_tty_framebuffer_request.response->framebuffers[0]->width; x++) {
            fb[x + (y * driver_limine_tty_framebuffer_request.response->framebuffers[0]->width)] = 0x303040;
        }
    }

    return 0;
}

driver_definition driver_limine_virt_tty = {
    .subsystem_type = SUBSYS_INTERNAL,
    .device_type = DEV_TTY,
    .init_ptr = &driver_limine_virt_tty_init
};

const uint64_t driver_limine_virt_tty_pointer __attribute__((section("drivers"))) = (uint64_t)&driver_limine_virt_tty;