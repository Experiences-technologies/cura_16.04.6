#!/usr/bin/python2.7
# -*- coding: utf-8 -*

import os
import subprocess

subprocess.call(["cp","preferences.ini",os.path.expanduser("~/Library/Application Support/Cura/15.04.6")])
subprocess.call(["cp","current_profile.ini",os.path.expanduser("~/Library/Application Support/Cura/15.04.6")])
subprocess.call(["cp","ultimaker_platform.stl","/Applications/Cura/Cura.app/Contents/Resources/meshes"])
subprocess.call(["cp","1_pla.ini","/Applications/Cura/Cura.app/Contents/Resources/quickprint/materials"])
subprocess.call(["cp","2_abs.ini","/Applications/Cura/Cura.app/Contents/Resources/quickprint/materials"])
subprocess.call(["cp","3_hdglass.ini","/Applications/Cura/Cura.app/Contents/Resources/quickprint/materials"])
subprocess.call(["cp","1_low.ini","/Applications/Cura/Cura.app/Contents/Resources/quickprint/profiles"])
subprocess.call(["cp","2_normal.ini","/Applications/Cura/Cura.app/Contents/Resources/quickprint/profiles"])
subprocess.call(["cp","3_high.ini","/Applications/Cura/Cura.app/Contents/Resources/quickprint/profiles"])
subprocess.call(["cp","4_ulti.ini","/Applications/Cura/Cura.app/Contents/Resources/quickprint/profiles"])
subprocess.call(["cp","switchfil1vers2.py","/Applications/Cura/Cura.app/Contents/Resources/plugins"])
subprocess.call(["cp","switchfil2vers1.py","/Applications/Cura/Cura.app/Contents/Resources/plugins"])
