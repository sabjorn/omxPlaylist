#!/usr/bin/env bash

if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root" 
   exit 1
fi

echo $PWD
echo "Removing omxPlayer from /usr/bin"
rm /usr/bin/omxPlaylist.py

echo "Removing OmxPlaylist Service"
rm /etc/systemd/system/omxPlaylist.service #may need to check /sys/systemd

echo "Do you wish to remove video directory (/media/omxPlaylist)?"
select yn in "Yes" "No"; do
    case $yn in
        Yes ) rm -fr /media/omxPlaylist; break;;
        No ) exit;;
    esac
done

exit 0