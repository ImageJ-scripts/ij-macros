# Bootstrap to extend modules search path #
from sys import path
import os.path
from java.lang.System import getProperty
jython_scripts = os.path.join(getProperty('user.home'), 'Jython_scripts')
path.append(jython_scripts)
#=========================================#

from IBPlib.ij.Colortags import Colortags

# GUI for editing the user color tags to be used in ColorMerger

t = Colortags()
t.edit()