#! /usr/bin/env python3

# Sawyer tuck script
# This is basically a wrapper around go_to_joint_angles.py which calls
# set_joint_speed.py when the tuck is complete.

import os
import sys

mydir = os.path.dirname(__file__)

# Set the joint angles correctly ...
os.system(mydir + '/go_to_joint_angles.py ' + ' '.join(sys.argv[1::]))
# ... then reset the joint speed to defaults.
os.system(mydir + '/set_joint_speed.py')
