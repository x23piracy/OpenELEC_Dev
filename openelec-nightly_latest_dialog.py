import xbmc
import sys
import xbmcgui
import subprocess

VERSION=sys.argv[1]

dialog = xbmcgui.Dialog()
i = dialog.yesno("An Update is Available", "New Build "+VERSION+" available Install?")

if i == 1:
    subprocess.call("/storage/script/openelec-nightly_latest.sh -q", shell=True)
