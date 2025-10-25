## Adding the nomodeset Kernel Parameter
(https://pve.proxmox.com/wiki/Installation#nomodeset_kernel_param)

Problems may arise on very old or very new hardware due to graphics drivers. If the installation hangs during boot, you can try adding the nomodeset parameter. This prevents the Linux kernel from loading any graphics drivers and forces it to continue using the BIOS/UEFI-provided framebuffer.

On the Proxmox VE bootloader menu, navigate to Install Proxmox VE (Terminal UI) and press e to edit the entry. Using the arrow keys, navigate to the line starting with linux, move the cursor to the end of that line and add the parameter nomodeset, separated by a space from the pre-existing last parameter.

Then press Ctrl-X or F10 to boot the configuration.
