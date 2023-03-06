class CONFIG:
    arch = "amd64"
    
    toolchain_prefix = "x86_64-none-elf"
    
    boot_protocol = "limine"

    cc_compiler = "clang --target=x86_64-none-elf"
    ld = "ld.lld"
    #cc_compiler = "x86_64-none-elf-gcc"
    
    cc_flags  = "-mno-red-zone -O3 -nostdlib -mcmodel=kernel -ffreestanding -fno-stack-protector -fno-stack-check -fno-lto -fno-pie -fno-pic -m64 -march=x86-64 -mabi=sysv -mno-80387 "
    cc_flags += "-mno-mmx -mno-sse -mno-sse2"

    #even if a driver disable is set to false, aslong as the disable is defined, the driver will still be disabled
    #mark a disable as a comment to enable the driver instead of using false
    
    disable_driver_input_ibm_ps2 = True