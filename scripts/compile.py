import config.config as config
import subprocess
import os

def compile(abs_path_of_file):
    object_name = abs_path_of_file.replace(os.path.abspath("."), "").replace("/", "_")

    file_extension = abs_path_of_file.split(".")[-1]

    if file_extension == "c":
        print(f"compiling {abs_path_of_file} with object name of {object_name.replace('.c', '.o')} and file extension of {file_extension}")
        subprocess.run(f"{config.CC} {config.CC_FLAGS} -c {abs_path_of_file} -o bin/{object_name.replace('.c', '.o')}", shell=True)

def recursive_compile(abs_path_of_folder):
    for file in os.listdir(abs_path_of_folder):
        if os.path.isdir(f"{abs_path_of_folder}/{file}"):
            recursive_compile(f"{abs_path_of_folder}/{file}")
        else:
            compile(f"{abs_path_of_folder}/{file}")