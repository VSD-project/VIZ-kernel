import config
import os
import subprocess

def compile(file: str):
    file_extension = file.split(".")[-1]
    file_prefix = file.split(".")[0]
    
    if file_extension == "c":
        print(f"[CC] {file}")
        os.system(f"{config.CC} {config.CCFLAGS} -c {file} -o bin/{file_prefix.replace('/', '_')}.o")
        #subprocess.run(f"{config.CC} {config.CCFLAGS} -c {file} -o bin/{file_prefix.replace('/', '_')}.o", shell=True)

def compile_dir(folder_path: str):
    for file in os.listdir(folder_path):
        if os.path.isdir(f"{folder_path}/{file}") == True:
            compile_dir(f"{folder_path}/{file}")
        else:
            compile(f"{folder_path}/{file}")
    
subprocess.run("rm -rf bin && mkdir bin", shell=True)

compile_dir(f"arch/{config.ARCH}")
compile_dir(f"init")
compile_dir(f"drivers")

subprocess.run(f"{config.LD} {config.LD_FLAGS} -T kernel.ld bin/* -o viz.bin", shell=True)