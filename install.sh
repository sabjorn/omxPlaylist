#!/usr/bin/env bash

if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root" 
   exit 1
fi

echo "Installing omxPlayer to /usr/bin"
cp ./python/omxPlaylist.py /usr/bin/
chmod u+x /usr/bin/omxPlaylist.py

echo "Installing OmxPlaylist Service"
cp ./systemd/omxPlaylist.service /etc/systemd/system #may need to check /sys/systemd
systemctl enable omxPlaylist.service

echo "Creating Video Directory (/media/omxPlaylist), \
copy video files (or make symlinks) to this dir."
mkdir -p /media/omxPlaylist

exit 0