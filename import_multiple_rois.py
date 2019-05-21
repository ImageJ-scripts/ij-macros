#@File[] (label="ROI folder", style="file", style="extensions:roi") roi_files

from ij import (IJ, ImagePlus)
from ij.plugin.frame import RoiManager
from ij.io import Opener

def import_multiple_rois(roi_files):
	rois = [f.getPath() for f in roi_files if f.exists() and f.getName().lower().endswith("roi")]
	opener = Opener()
	rm = RoiManager.getRoiManager()
	if not rm.getInstance():
		rm.reset()
	[rm.addRoi(opener.openRoi(r)) for r in rois]
	
if __name__ in ("__builtin__", "__main__"):
	import_multiple_rois(roi_files)