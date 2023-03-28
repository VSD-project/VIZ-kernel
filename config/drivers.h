#ifndef KERNEL_CONFIG_DRIVERS_H
#define KERNEL_CONFIG_DRIVERS_H

#if defined(__thumb__) && defined(__TARGET_ARCH_ARM) && (__TARGET_ARCH_ARM == 6) //thumbv6m specific drivers

#define RP2040 //enable the rp2040 driver

#endif

#endif