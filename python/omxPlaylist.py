#!/usr/bin/env python3
#

# import modules used here -- sys is a very standard one
import sys, argparse, logging

from os import listdir
from os.path import isfile, join

import subprocess

omx_command = ['omxplayer', "-o", "hdmi", "-b"]


def generatePlaylist(inpath):
    return [f for f in listdir(inpath) if isfile(join(inpath, f))]


# Gather our code in a main() function
def main(args, loglevel):
    logging.basicConfig(format="%(levelname)s: %(message)s", level=loglevel)

    #[omx_command.append(f) for f in args.remaining] # add extra OMX commands to end, sort of janky
    playlist = generatePlaylist(args.directory)

    for f in playlist:
        full_path = args.directory + "/" + f
        full_command = omx_command + args.remaining + [full_path]

        stdout = subprocess.PIPE
        if args.debug:
            stdout = False

        proc = None
        try:
            logging.debug("playing: {0}".format(full_path))
            proc = subprocess.run(full_command, check=True, stdin=subprocess.PIPE, stdout=stdout, close_fds=True)
        except KeyboardInterrupt:
            if proc is not None:
                proc.kill()
            logging.info("Keyboard Interrupt")
            sys.exit()
        except Exception as e:
            logging.exception()

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Does a thing to some stuff.",
        epilog="As an alternative to the commandline, params can be placed in a file, one per line, and specified on the commandline like '%(prog)s @params.conf'.",
        fromfile_prefix_chars='@')
    # TODO Specify your real parameters here.
    parser.add_argument(
        "directory",
        help="pass ARG to the program",
        metavar="ARG")
    parser.add_argument(
        "-d",
        "--debug",
        help="increase output verbosity",
        action="store_true")
    parser.add_argument(
        'remaining',
        help="catch all other arguments to be passed to OMXplayer",
        nargs=argparse.REMAINDER)
    args = parser.parse_args()

    # Setup logging
    if args.debug:
        loglevel = logging.DEBUG
    else:
        loglevel = logging.INFO

    main(args, loglevel)
