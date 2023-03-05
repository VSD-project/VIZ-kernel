class CONFIG:
    arch = "amd64"
    toolchain_prefix = "x86_64-none-elf"
    cc_flags = "-mno-red-zone -O3"

    #even if a driver disable is set to false, aslong as the disable is defined, the driver will still be disabled
    #mark a disable as a comment to enable the driver instead of using false
    disable_driver_input_ibm_ps2 = True