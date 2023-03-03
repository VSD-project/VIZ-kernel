import config
import os
import subprocess

cpu_count = os.cpu_count()

def system(command):
    subprocess.run(command, shell=True, check=True)

if config.arch == "amd64":
    system(f"cd arch/x86 && make -j {cpu_count}")
    system(f"cd arch/x86/amd64 && make -j {cpu_count}")
else: system(f"cd arch/{config.arch} && make -j {cpu_count}")
