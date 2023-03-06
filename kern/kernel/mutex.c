#include <viz/mutex.h>

void mutex_init(mutex_t* mutex) {
    mutex->lock = 0;
}

void mutex_lock(mutex_t* mutex) {
    int oldval;
    do {
        oldval = __sync_val_compare_and_swap(&mutex->lock, 0, 1);
    } while (oldval != 0);
}

void mutex_unlock(mutex_t* mutex) {
    __sync_lock_release(&mutex->lock);
}
