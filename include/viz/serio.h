//Serial io function and type defintion

#ifndef VIZ_SERIO_H
#define VIZ_SERIO_H

#include <spinlock.h>

typedef struct {
    void (*tx)(char byte) = 0;
    void (*rx)(char byte);
    spinlock_t lock;
}serio;

#endif