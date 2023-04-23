#ifndef VIZ_DRIVER_H
#define VIZ_DRIVER_H
#include <viz/stdint.h>

//subsystem types
#define SUBSYS_INTERNAL 0
#define SUBSYS_PCI 1

//device types
#define DEV_TTY 0

typedef struct driver_definition {
    uint8_t subsystem_type;
    uint8_t device_type;

    uint16_t vendor_id;
    uint16_t model_id;
    
    int (*init_ptr)(void);
    uint64_t device_function_table_addr;
} driver_definition;

typedef struct dev_tty_function_table {
    void (*out_func_ptr)(char*);
}dev_tty_function_table;

#endif