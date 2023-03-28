import scripts.compile as compile
import config.config as config
import os

compile.recursive_compile(os.path.abspath("drivers"))
compile.recursive_compile(os.path.abspath("fs"))
compile.recursive_compile(os.path.abspath("kernel"))
compile.recursive_compile(os.path.abspath(f"arch/{config.arch}"))