# Download Ubuntu 24.04 cloud image
wget https://cloud-images.ubuntu.com/releases/24.04/release/ubuntu-24.04-server-cloudimg-amd64.img

# Create VM with ID 900
qm create 900 --memory 2048 --net0 virtio,bridge=vmbr0 --scsihw virtio-scsi-pci --name "ubuntu-24.04-template"

# Import disk to storage
qm importdisk 900 ubuntu-24.04-server-cloudimg-amd64.img local-lvm

# Attach disk to VM
qm set 900 --scsi0 local-lvm:vm-900-disk-0

# Add cloud-init drive
qm set 900 --ide2 local-lvm:cloudinit

# Set boot order
qm set 900 --boot c --bootdisk scsi0

# Enable QEMU guest agent
qm set 900 --agent enabled=1

# Setup Mac German keyboard
mkdir -p /var/lib/vz/snippets
cat << EOF > /var/lib/vz/snippets/mac-german-keyboard.yaml
#cloud-config
keyboard:
  layout: de
  variant: mac
  model: macintosh
locale: de_DE.UTF-8
runcmd:
  - localectl set-keymap de-mac
  - dpkg-reconfigure -f noninteractive keyboard-configuration
  - apt update
  - apt install -y qemu-guest-agent
  - systemctl start qemu-guest-agent
EOF
qm set 900 --cicustom "vendor=local:snippets/mac-german-keyboard.yaml"

# Set user and password
qm set 900 --ciuser ubuntu --cipassword 'ChangeMe!'

# Setup IP address
qm set 900 --ipconfig0 ip=dhcp

# Copy SSH key
if [ ! -f ~/.ssh/id_ed25519_martin.pub ]; then
    echo "Error: SSH key ~/.ssh/id_ed25519_martin.pub not found"
    exit 1
fi
qm set 900 --sshkeys ~/.ssh/id_ed25519_martin.pub

# Convert to template
qm template 900

# Clean up
rm ubuntu-24.04-server-cloudimg-amd64.img
