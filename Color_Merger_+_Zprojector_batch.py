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
from IBPlib.ij.Projector import Projector

savefolder = save_folder.getPath()
imgfolder = img_folder.getPath()
save_folders = [os.path.join(savefolder, folder) for folder in ["colormeged", "z-projections"]]

for directory in save_folders:
	if not os.path.isdir(directory):
		try:
			os.makedirs(directory)
		except Exception as e:
			print(e.args[0])

projector = Projector(save_folders[1], imgfolder, ext)
postProcessingMethod = projector.doprojection
cm = ColorMerger(save_folders[0], imgfolder, ext,)

cm.run(postProcessingMethod=postProcessingMethod)