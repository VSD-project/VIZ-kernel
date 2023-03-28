import config.config as config
import subprocess
import os

def compile(abs_path_of_file):
    object_name = abs_path_of_file.replace(os.path.abspath("."), "").replace("/", "_")

    file_extension = abs_path_of_file.split(".")[-1]

    if file_extension == "C":
        subprocess.run(f"{config.CC} {config.CC_FLAGS} -c {abs_path_of_file} -o bin/{object_name}", shell=True)