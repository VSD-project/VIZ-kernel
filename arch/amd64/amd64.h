#ifndef ARCH_AMD64_H
#define ARCH_AMD64_H

#include <viz/stdint.h>

// Write a byte of data to an output port.
static inline void outb(uint16_t port, uint8_t data)
{
    asm volatile ("outb %0, %1" : : "a" (data), "d" (port));
}

// Write a word of data to an output port.
static inline void outw(uint16_t port, uint16_t data)
{
    asm volatile ("outw %0, %1" : : "a" (data), "d" (port));
}

// Write a double word of data to an output port.
static inline void outl(uint16_t port, uint32_t data)
{
    asm volatile ("outl %0, %1" : : "a" (data), "d" (port));
}

// Read a byte of data from an input port.
static inline uint8_t inb(uint16_t port)
{
    uint8_t data;
    asm volatile ("inb %1, %0" : "=a" (data) : "d" (port));
    return data;
}

// Read a word of data from an input port.
static inline uint16_t inw(uint16_t port)
{
    uint16_t data;
    asm volatile ("inw %1, %0" : "=a" (data) : "d" (port));
    return data;
}

// Read a double word of data from an input port.
static inline uint32_t inl(uint16_t port)
{
    uint32_t data;
    asm volatile ("inl %1, %0" : "=a" (data) : "d" (port));
    return data;
}

#endif