#pypi.org

#pipi.org/project/cowsay

# package manger -- > pip
#pip is used to install packagess

#PS C:\Users\alwin\Desktop\cs50_python> pip install cowsay

import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("hello," + sys.argv[1])
    
 
    cowsay.trex("hello," + sys.argv[1])

    cowsay.octopus("hello" + sys.argv[1])
