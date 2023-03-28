import os

'''
suported targets:

thumbv6m-none-eabi

'''

load_kernel_into_addr = 0x20000000

arch = "arm32"

target = "thumbv6m-none-eabi"
mcpu = "cortex-m0plus" #can just be an empty string

CC = "clang"
CC_FLAGS = f"--target={target} -mcpu={mcpu} -mthumb -I {os.path.abspath('.')}/config -I {os.path.abspath('.')}/viz -O1"