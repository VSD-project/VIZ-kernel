import config
import os
import subprocess
import importlib

if os.path.isdir("bin"): os.rmdir("bin")
os.mkdir("bin")

def system(command):
    subprocess.run(command, shell=True, check=True)

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

skip_dir = ["include", ".git", ".vscode", "bin", "__pycache__"]

for dir in os.listdir("."):
    if os.path.isdir(dir):
        if dir in skip_dir: pass
        
        elif dir == "arch":
            if config.CONFIG.arch == "amd64":
                #build legacy x86 code
                HELPER.mod_abs_path = os.path.abspath("arch/x86")
                arch_module = importlib.import_module("arch.x86.build")
                arch_module.main(HELPER)

                #build actual amd64 code
                HELPER.mod_abs_path = os.path.abspath("arch/x86/amd64")
                arch_module = importlib.import_module(f"arch.x86.{config.CONFIG.arch}.build")
                arch_module.main(HELPER)
            else: HELPER.mod_abs_path = os.path.abspath(f"arch/{config.CONFIG.arch}"); arch_module = importlib.import_module(f"arch.{config.CONFIG.arch}.build"); arch_module.main(HELPER)
        
        else: HELPER.mod_abs_path = os.path.abspath(dir); module = importlib.import_module(f"{dir}.build"); module.main(HELPER)
