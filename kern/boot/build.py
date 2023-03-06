import os

class HELPER:
    bin_abs_path = str()
    mod_abs_path = str()
    cpu_count = int()
    toolchain_prefix = str()

    class config: pass

    def system(command): pass

def main(helper: HELPER):
    if helper.config.boot_protocol == "limine":
        print(f"[gcc] limine.c")
        helper.system(f"{helper.config.cc_compiler} -I {helper.mod_abs_path}/../include -c {helper.mod_abs_path}/limine.c -o {helper.bin_abs_path}/boot_limine.o {helper.config.cc_flags}")
