# omxPlaylist
## About
This project is designed to provide a mechanism for playing groups of video files (a directory of files) in sequence (a playlist) using Python and [OMXPlayer](https://github.com/popcornmix/omxplayer). It is meant to be used on a Raspberry PI running Debian Linux.

Also provided is the ability to use `systemd` to auto-boot the playlist and install/uninstall scripts to make the setup easy.

A secondary intention of this project is to provide a simple example of how to setup a Raspberry PI for use as a simple service provider (a video player). The files contained in this repo should be easy enough to modify in order to create any other type of service (e.g. DHCP server, MongoDB, APACHE web server).

## Project Status
This project is in early development. Much of the necessary code was lost and will be re-written from scratch.