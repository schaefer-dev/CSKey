#! /usr/bin/env python3

import os.path
import platform
import sys
import subprocess

layout_filename = "CSLayout.keylayout"
icon_filename = "CSLayout.icns"

if platform.system() == "Darwin":  # check if Mac
  target = '/Library/Keyboard\\ Layouts/'
  command = f"sudo cp {layout_filename} {target}"
  command2 = f"sudo cp {icon_filename} {target}"
  if os.geteuid() != 0:
    print("We need to copy the layout file to `/Library/Keyboard\ Layouts/`. This requires root privileges, so your OS will ask you for your password.")
    print("After copying, you will need to open Apple > System Preferences > Keyboard > Input Sources, click the little \"+\", go to \"others\" and select the CSKeyboardLayout. Voilà!")
    os.system(command)
    os.system(command2)
else: 
  print("Sorry, We currently only support Mac. You need to install the layout manually.")


