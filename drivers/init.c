#include <viz/init.h>
#include <viz/driver.h>
#include <viz/stdint.h>
#include <viz/KERNEL_DRIVER_MAP.h>

void driver_subsystem_init(void) {    
    for (uint32_t x = 0; x < KERNEL_DRIVER_MAP_SIZE; x++) {
        KERNEL_DRIVER_MAP[x]->init_ptr();
    }
    
}