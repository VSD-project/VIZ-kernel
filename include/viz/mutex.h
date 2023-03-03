#ifndef VIZ_MUTEX_H
#define VIZ_MUTEX_H

#ifdef __GNUC__
// Check if __sync_val_compare_and_swap is defined
#if (__GNUC__ > 4 || (__GNUC__ == 4 && __GNUC_MINOR__ >= 1))
#define HAS_ATOMIC_OPS 1
#endif
#endif

#ifndef HAS_ATOMIC_OPS
#error COMPILER DOESNT DEFINE ATOMIC BUILTINS
#endif

typedef struct {
    int lock;
}mutex_t;

#endif
