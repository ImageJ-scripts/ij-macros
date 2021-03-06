#@File[] (label="ROI folder", style="file") roi_files
#@File	(label="Results folder", style="directory") csvPath
# Bootstrap to extend modules search path #
from sys import path
import os.path
from java.lang.System import getProperty
jython_scripts = os.path.join(getProperty('user.home'), 'Jython_scripts')
path.append(jython_scripts)
#=========================================#

from ij import (IJ, ImagePlus)
from ij.gui import Roi
from ij.io import Opener
from IBPlib.ij.Utils.Files import buildList

def normalized_roi_length(roi_path, pixel_scaling, normalization_fn=None):
	'''
	Returns the scaled measure of the input roi performing the normalization
	function if provided. 
	'''
	opener = Opener()
	roi = opener.openRoi(roi_path)
	scaled_measure = roi.getLength()/pixel_scaling
	if callable(normalization_fn):
		return normalization_fn(scaled_measure)
	return measure

if __name__ in ("__builtin__", "__main__"):
	'''
	Use case where multiple rois are measured, scaled and normalized.
	Measurements being saved then to a csv file.
	'''
	rois = []
	for i in roi_files:
		if i.isDirectory():
			rois.append(buildList(i.getPath(), ".roi"))
		elif i.isFile() and i.getName().lower().endswith(".roi"):
			rois.append(i.getPath())
	scale = 3.1 # pixels/micrometers
	cutdistance = 50 # distance from cell body in micrometers
	lengths = (normalized_roi_length(roi, scale, lambda x: x-cutdistance) for roi in rois)
	
	resultspath = os.path.join(csvPath.getPath(),"regrowth_1.csv")
	with open(resultspath, "w") as csvfile:
		for row in lengths:
			line = "{0}\n".format(row)
			csvfile.write(line)
	IJ.log("Results were saved to {0}".format(resultspath))