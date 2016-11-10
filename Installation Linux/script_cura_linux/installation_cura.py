#!/usr/bin/python2.7
# -*- coding: utf-8 -*

import os
import subprocess

subprocess.call(["cp","preferences.ini",os.path.expanduser("~/.cura/15.04.6")])
subprocess.call(["cp","current_profile.ini",os.path.expanduser("~/.cura/15.04.6")])
subprocess.call(["cp","ultimaker_platform.stl","/usr/share/cura/resources/meshes"])
subprocess.call(["cp","1_pla.ini","/usr/share/cura/resources/quickprint/materials"])
subprocess.call(["cp","2_abs.ini","/usr/share/cura/resources/quickprint/materials"])
subprocess.call(["cp","3_hdglass.ini","/usr/share/cura/resources/quickprint/materials"])
subprocess.call(["cp","1_low.ini","/usr/share/cura/resources/quickprint/profiles"])
subprocess.call(["cp","2_normal.ini","/usr/share/cura/resources/quickprint/profiles"])
subprocess.call(["cp","3_high.ini","/usr/share/cura/resources/quickprint/profiles"])
subprocess.call(["cp","4_ulti.ini","/usr/share/cura/resources/quickprint/profiles"])
subprocess.call(["cp","switchfil1vers2.py","/usr/share/cura/plugins"])
subprocess.call(["cp","switchfil2vers1.py","//usr/share/cura/plugins"])
