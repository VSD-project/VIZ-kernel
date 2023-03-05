import os

class HELPER:
    bin_abs_path = str()
    mod_abs_path = str()
    cpu_count = int()
    toolchain_prefix = str()

    class config: pass

    def system(command): pass

helper = HELPER

#f"disable{abs_file_path.replace(os.path.abspath('.') , '').replace( '/','_' ).split('.')[0]}"

def compile(abs_file_path):
    print(f"disable{abs_file_path.replace(os.path.abspath('.') , '').replace( '/','_' ).split('.')[0]}")
    for object in dir(helper.config):
        print(object)
    
def recursive_compile(abs_folder_path):
    for file in os.listdir(abs_folder_path):
        if os.path.isdir(f"{abs_folder_path}/{file}"):
            recursive_compile(f"{abs_folder_path}/{file}")
        else:
            compile(f"{abs_folder_path}/{file}")


def main(temp_helper: HELPER):
    helper = temp_helper
    recursive_compile(helper.mod_abs_path)
    print(dir(helper.config))
