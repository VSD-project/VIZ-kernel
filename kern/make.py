import config
import os
import subprocess
import importlib

def system(command):
    subprocess.run(command, shell=True, check=True)

if os.path.isdir("bin"): system("rm -rf bin")
os.mkdir("bin")

class HELPER:
    bin_abs_path = str()
    mod_abs_path = str()
    cpu_count = int()
    toolchain_prefix = str()

    class config: pass

    def system(command): pass

HELPER.cpu_count = os.cpu_count()
HELPER.system = system
HELPER.bin_abs_path = os.path.abspath("bin")
HELPER.toolchain_prefix = config.CONFIG.toolchain_prefix
HELPER.config = config.CONFIG

skip_dir = ["include", ".git", ".vscode", "bin", "__pycache__", ".github"]

for dir in os.listdir("."):
    if os.path.isdir(dir):
        if dir in skip_dir: pass
        
        elif dir == "arch": HELPER.mod_abs_path = os.path.abspath(f"arch/{config.CONFIG.arch}"); arch_module = importlib.import_module(f"arch.{config.CONFIG.arch}.build"); arch_module.main(HELPER)
        
        else: HELPER.mod_abs_path = os.path.abspath(dir); module = importlib.import_module(f"{dir}.build"); module.main(HELPER)

print(f"[{config.CONFIG.ld}] -T kernel.ld -o vizkern.bin bin/*.o")
system(f"{config.CONFIG.ld} -T kernel.ld -o vizkern.bin bin/*.o")