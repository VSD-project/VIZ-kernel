//Serial io function and type defintion

#ifndef VIZ_SERIO_H
#define VIZ_SERIO_H

#include <viz/spinlock.h>

typedef struct {
    char addr; //optional in most cases
    void (*tx)(char byte);
    char (*rx)(void);
    spinlock_t lock;
}serio_t;

#endif