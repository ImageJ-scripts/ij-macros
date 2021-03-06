# Color_Merger_batch.py
# Dev: Igor Bonacossa Pereira.
# Email: i.bonacossapereira@uq.edu.au

#@File (label="Images folder", style="directory") img_folder
#@File (label="Save folder", style="directory") save_folder
#@String (label="Images extension", value=".jpg") ext

# Bootstrap to extend modules search path #
from sys import path
import os
from java.lang.System import getProperty
jython_scripts = os.path.join(getProperty('user.home'), 'Jython_scripts')
path.append(jython_scripts)
#=========================================#

# GUI for getting parameters to run ColorMerger in batch mode.

from IBPlib.ij.ColorMerger import ColorMerger

savefolder = save_folder.getPath()
imgfolder = img_folder.getPath()

if not os.path.isdir(savefolder):
	try:
		os.makedirs(savefolder)
	except Exception as e:
		print(e.args[0])

cm = ColorMerger(savefolder, imgfolder, ext)
cm.run()