#generates the driver array used by the kernel to map its internal drivers
from elftools.elf.elffile import ELFFile
import subprocess

def find_all_symbols(filename):
    with open(filename, 'rb') as f:
        elffile = ELFFile(f)
        for section in elffile.iter_sections():
            if section.name == '.symtab':
                symtab = section
                break
        else:
            # No symbol table found
            return []
        symbols = []
        for symbol in symtab.iter_symbols():
            symbols.append(symbol.name)
        return symbols


def get_valid_driver_symbols():
    # Example usage:
    valid = []
    symbols = find_all_symbols("kernel.o")
    for symbol in symbols:
        if "driver_" in symbol:
            for init_func in symbols:
                if init_func == f"{symbol}_init":
                    valid.append(symbol)
    return valid

def create_c_file(valid_driver_list: list):
    file  = f"#include <viz/driver.h>\n"
    file += f"#include <viz/stdint.h>\n"
    file += f"uint64_t KERNEL_DRIVER_MAP_SIZE = {len(valid_driver_list)};\n"

    for x in range(len(valid_driver_list)):
        file += f"extern driver_definition {valid_driver_list[x]};\n"

    file += f"driver_definition* KERNEL_DRIVER_MAP[{len(valid_driver_list)}] = {{"
    temp_str = ""
    for x in range(len(valid_driver_list)):
        if x != 0:
            temp_str += ", "
        temp_str += valid_driver_list[x]
    file += f"&{temp_str}"
    file += f"}};"
    return file

def create_h_file(valid_driver_list: list):
    file  = f"#include <viz/driver.h>\n"
    file += f"#include <viz/stdint.h>\n"
    file += f"uint64_t KERNEL_DRIVER_MAP_SIZE;\n"
    file += f"driver_definition* KERNEL_DRIVER_MAP[1];\n"
    return file

def test():
    with open('build/KERNEL_DRIVER_MAP.c', 'w') as f:
        f.write(create_c_file(get_valid_driver_symbols()))
    with open('viz/KERNEL_DRIVER_MAP.h', 'w') as f:
        f.write(create_h_file(get_valid_driver_symbols()))