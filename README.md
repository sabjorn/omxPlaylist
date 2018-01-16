# omxPlaylist
## About
This project is designed to provide a mechanism for playing groups of video files (a directory of files) in sequence (a playlist) using Python and [OMXPlayer](https://github.com/popcornmix/omxplayer). It is meant to be used on a Raspberry PI running Debian Linux.

Also provided is the ability to use `systemd` to auto-boot the playlist and install/uninstall scripts to make the setup easy.

A secondary intention of this project is to provide a simple example of how to setup a Raspberry PI for use as a simple service provider (a video player). The files contained in this repo should be easy enough to modify in order to create any other type of service (e.g. DHCP server, MongoDB, APACHE web server).

## Usage
This project used `systemd` to start `omxPlaylist.py` at startup. However, if the `install` script is not used, `omxPlaylist.py` can be run directly with:

```
python3 omxPlaylist.py [video_dir]
```

### Install
To `install`, run:

```
chmod u+x install.sh
sudo ./install.sh
```

## Uninstall
To `uninstall`, run:

```
chmod u+x install.sh
sudo ./uninstall.sh
```

Importantly, the `omxPlaylist.service` (`systemd` service which runs the script at boot) is hardcoded to use the `/media/omxPlaylist` directory as the source for video files. Videos can be copied or symlinked to this directory to play. Alternatively, `systemd/omxPlaylist.service` can be modified, replacing:

```
/media/omxPlaylist
```

with whichever directory you wish to have your videos. Then, re-run the `install.sh` script.

*Note*: For both `install.sh` and `uninstall.sh`, the `chmod` command is only required once.

