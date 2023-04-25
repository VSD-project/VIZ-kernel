#include <viz/driver.h>
#include <viz/stdint.h>
uint64_t KERNEL_DRIVER_MAP_SIZE = 1;
extern driver_definition driver_limine_virt_tty;
driver_definition* KERNEL_DRIVER_MAP[1] = {&driver_limine_virt_tty};