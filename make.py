import config
import os
import subprocess
import importlib

class HELPER:
    bin_abs_path = str()
    mod_abs_path = str()

    def system(command): pass

cpu_count = os.cpu_count()

def system(command):
    subprocess.run(command, shell=True, check=True)

def compile(filename):
    extension = filename.split(".")
    path = extension[0].split("/")

    if extension[1] == "c":
        system("gcc -I src/include -c " + filename + " -o bin/" + path[-1] + ".o")
        print("[CC]  " + path[-1] + "." + extension[1])

    if extension[1] == "s":
        system("as -I include -c " + filename + " -o bin/" + path[-1] + ".o")
        print("[C++] " + path[-1] + "." + extension[1])

def compileDir(dir):
    for file in os.listdir(dir):
        if os.path.isdir(dir + "/" + file) == True:
            #recursive time
            compileDir(dir + "/" + file)
        if os.path.isdir(dir + "/" + file) == False:
            compile(dir + "/" + file)

if config.arch == "amd64": arch_module = importlib.import_module("arch.x86.build")
else: arch_module = importlib.import_module(f"arch.{config.arch}.build")