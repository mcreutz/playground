Proxmox VM USB Dongle Setup Guide
1. Proxmox Passthrough Configuration

    Plug the dongle into a USB 2.0 port on the physical server (or use a USB 2.0 extension cable).

    Open the Proxmox web interface and select your target VM.

    Go to the Hardware tab, click Add, and select USB Device.

    Choose Use USB Vendor/Device ID and select your dongle from the dropdown list.

    Ensure the Use USB3 checkbox is explicitly unchecked.

    Perform a full shutdown and start of the VM from the Proxmox interface.

2. Driver Installation

    Minimal cloud images do not include USB serial drivers by default. Install them inside the VM:

    bash
    sudo apt update
    sudo apt install linux-modules-extra-$(uname -r)

3. Persistent Driver Configuration

    Ensure the driver loads automatically every time the VM boots.

    Open the modules file:

    bash
    sudo nano /etc/modules

    Add the driver name (cp210x for Sonoff dongles) on a new line at the bottom of the file.

    Save and exit.