class HELPER:
    bin_abs_path = str()
    mod_abs_path = str()
    cpu_count = int()
    toolchain_prefix = str()

    class config: pass

    def system(command): pass

def main(helper: HELPER):
    try: helper.config.disable_ps2_kbd
    except:
        helper.system(f"{helper.toolchain_prefix}-gcc -I {helper.mod_abs_path}/../include -c {helper.mod_abs_path}/input/ibm_ps2.c -o {helper.bin_abs_path}/ibm_ps2.o")