#include <viz/init.h>
#include <viz/driver.h>
#include <viz/stdint.h>

extern uint64_t driver_start;
extern uint64_t driver_end;

void driver_subsystem_init(void) {    
    driver_definition *x = (driver_definition *)&driver_start;
    x->init_ptr();
    
}