all:
	cd kern && python3 make.py

debugiso: all
	if [ -d "iso" ]; then \
		rm -rf iso; \
	fi
	mkdir iso

	cp kern/vizkern.bin iso/vizkern.bin
	cp limine.cfg iso/limine.cfg
	cp limine-cd-efi.bin iso/limine-cd-efi.bin
	cp limine-cd.bin iso/limine-cd.bin
	cp limine.sys iso/limine.sys

	xorriso -as mkisofs -b limine-cd.bin -no-emul-boot -boot-load-size 4 -boot-info-table --efi-boot limine-cd-efi.bin -efi-boot-part --efi-boot-image --protective-msdos-label iso -o viz.iso
	limine-deploy viz.iso

qemu:
	qemu-system-x86_64 -bios bios64.bin -cdrom viz.iso