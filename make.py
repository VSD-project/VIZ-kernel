import config
import os
import subprocess
import importlib

cpu_count = os.cpu_count()

def system(command):
    subprocess.run(command, shell=True, check=True)

if config.arch == "amd64": arch_module = importlib.import_module("arch.x86.build")
else: arch_module = importlib.import_module(f"arch.{config.arch}.build")
