# Color_Merger_batch.py
# Dev: Igor Bonacossa Pereira.
# Email: i.bonacossapereira@uq.edu.au

# Bootstrap to extend modules search path #
from sys import path
import os.path
from java.lang.System import getProperty
jython_scripts = os.path.join(getProperty('user.home'), 'Jython_scripts')
path.append(jython_scripts)
#=========================================#



# Macro to run ColorMerger in opened images

from IBPlib.ij.ColorMerger import ColorMerger

cm = ColorMerger(False, False, False)
cm.run()