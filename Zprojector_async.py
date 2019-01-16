# Zprojector.py
# IBP
# i.bonacossapereira@uq.edu.au

#@File (label="Images folder", style="directory") img_folder
#@File (label="Save folder", style="directory") save_folder
#@String (label="Images extension", value=".tif") _extension
#@String (label="Projection method", choices={"max","min","avg","sum", "sd", "median"}) method
#@Boolean (label="Open folder when done?") openFolder

# Bootstrap to extend modules search path #
from sys import path
import os.path
from java.lang.System import getProperty
jython_scripts = os.path.join(getProperty('user.home'), 'Jython_scripts')
path.append(jython_scripts)
#=========================================#

import threading

from time import clock

from java.awt import Desktop

import ij.gui.GenericDialog
import ij.io.FileSaver
from ij import IJ, CompositeImage, ImagePlus
from ij.plugin import ZProjector
from IBPlib.ij.Utils.Files import buildList

def run():
	
	__version__ = 1.0

	IJ.log("\n### ZProjector v{0} started.".format(__version__))	
	img_list = buildList(img_folder.getPath(), extension=_extension)

	dialog = ij.gui.GenericDialog("Zprojector.py")
	dialog.addMessage("There are {0} images to be processed.\n Proceed?".format(len(img_list)))
	dialog.showDialog()
	if dialog.wasCanceled():
		IJ.log("Canceled by the user.")
		return

	projectorthreads = []
	for img in img_list:
		thread = threading.Thread(target=doprojection, args=(img,))
		projectorthreads.append(thread)
		thread.daemon = True
		thread.start()
	
	notDone = True
	t_ini = clock()
	timeout = 1800 # max execution time in seconds

	while notDone: # loop to check threads status
		elapsed = (clock() - t_ini)
		threads_life = [t.isAlive() for t in projectorthreads]
		if elapsed > timeout:
			IJ.error("ZProjector timedout.")
			break
		elif not any(threads_life):
			notDone = False
			
	IJ.log("\n## Done projecting")		
	if openFolder:
		Desktop.getDesktop().open(save_folder)

def doprojection(imgpath):
	IJ.log("# Processing {0}...".format(impTitle))
	save_path = save_folder.getPath()
	imp = ImagePlus(imgpath)
	impTitle = imp.getTitle()
	composite_imp = CompositeImage(imp, 1)
	projection = ZProjector.run(composite_imp, method)
	save_string = os.path.join(save_path, impTitle)
	try:
		ij.io.FileSaver(projection).saveAsTiff(save_string)
		IJ.log("## {0} Done processing ".format(impTitle))
	except:
		IJ.log("ij.io.FileSaver raised an exception while trying to save img '{0}' as '{1}'.Skipping image."
				.format(impTitle, save_string))
	
if __name__ in ("__builtin__", "__main__"):
	run()
