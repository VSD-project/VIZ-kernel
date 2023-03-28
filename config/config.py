import os

'''
suported targets:

thumbv6m-none-eabi

'''

target = "thumbv6m-none-eabi"
mcpu = "cortex-m0plus" #can just be an empty string

CC = "clang"
CC_FLAGS = f"--target={target} -mcpu={mcpu} -mthumb -I {os.path.abspath('.')}/config -I {os.path.abspath('.')}/viz -O1"