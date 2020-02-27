# Zprojector_batch.py
# IBP
# i.bonacossapereira@uq.edu.au

#@File (label="Images folder", style="directory") img_folder
#@File (label="Save folder", style="directory") save_folder
#@String (label="Images extension", value=".tif") ext
#@String (label="Projection method", choices={"max","min","avg","sum", "sd", "median"}) method

# Bootstrap to extend modules search path #
from sys import path
import os.path
from java.lang.System import getProperty
jython_scripts = os.path.join(getProperty('user.home'), 'Jython_scripts')
path.append(jython_scripts)
#=========================================#

from IBPlib.ij import Projector

savefolder = save_folder.getPath()
imgfolder = img_folder.getPath()
if not os.path.isdir(savefolder):
	try:
		os.makedirs(savefolder)
	except Exception as e:
		print(e.args[0])
projector = Projector.Projector(savefolder, imgfolder, ext, method)
projector.run()