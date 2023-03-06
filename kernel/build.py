import os

class HELPER:
    bin_abs_path = str()
    mod_abs_path = str()
    cpu_count = int()
    toolchain_prefix = str()

    class config: pass

    def system(command): pass

def main(helper: HELPER):
    for file in os.listdir(helper.mod_abs_path):
        if os.path.isdir(f"{helper.mod_abs_path}/{file}") == False:
            if file.split(".")[-1] == "c":
                print(f"[gcc] {file}")
                helper.system(f"{helper.config.cc_compiler} -I {helper.mod_abs_path}/../include -c {helper.mod_abs_path}/{file} -o {helper.bin_abs_path}/kernel_{file.split('.')[0]}.o {helper.config.cc_flags}")
