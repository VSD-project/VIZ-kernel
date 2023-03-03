#ifndef VIZ_SPINLOCK_H
#define VIZ_SPINLOCK_H

#include <viz/mutex.h>

typedef struct {
    mutex_t mutex
}spinlock_t;

void spin_lock_init(spinlock_t* lock);

#endif