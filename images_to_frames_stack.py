#@File (label="Images folder", style="directory") imgdir
#@String (label="Images extension", value=".tif") ext
#@Boolean (label="Save the stack?") save
#@String (visibility=MESSAGE, value="Select save if you want to keep to stack containing the images to be traced on disk.") msg


# Bootstrap to extend modules search path #
from sys import path
import os.path
from java.lang.System import getProperty
jython_scripts = os.path.join(getProperty('user.home'), 'Jython_scripts')
path.append(jython_scripts)
#=========================================#

from IBPlib.ij.Utils.Files import buildList
from  IBPlib.ij.Utils import ThreadedFileSaver

from ij import (IJ, ImagePlus, ImageStack)
from ij.plugin import ZProjector

def prepare_batchtracing(imgdir, savestack=False):
	'''
	Method for preparing images for batch tracing with Simple Neurite Tracer.
	When savestack is true it saves the resulting stack to the images folder while opening the stack for tracing
	'''
	title = "tracing_stack.tiff" # Title of the final image stack.
	imgdir = imgdir.getPath()
	imglist = buildList(imgdir, ext)
	if not imglist:
		raise IOError("No {0} were found in {0}.".format(ext, imgdir))
	method = "max"
	implist = []
	for img in imglist:
		imp = ImagePlus(img)
		if imp.isStack():
			imp = ZProjector.run(imp, method)
		implist.append(imp)
	stack = ImageStack(
		implist[0].getWidth(),
		implist[0].getHeight())
	[stack.addSlice(img.getProcessor()) for img in implist]
	stackimp = ImagePlus(title, stack)
	IJ.run(stackimp, "Properties...", "slices=1 frames={0}".format(stackimp.getStackSize()))
	if savestack:
		IJ.log("# Saving tracing stack...")
		save_string = os.path.join(imgdir, title)
		fs = ThreadedFileSaver.ThreadedFileSaver(stackimp, save_string, "saveAsTiff")
		fs.start()
	stackimp.show()


if __name__ in ("__builtin__", "__main__"):
	prepare_batchtracing(imgdir, save)