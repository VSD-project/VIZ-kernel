import os

class HELPER:
    bin_abs_path = str()
    mod_abs_path = str()
    cpu_count = int()
    toolchain_prefix = str()

    class config: pass

    def system(command): pass
    def read_config(file): pass

def main(helper: HELPER):
    print(helper.read_config("driver.config"))