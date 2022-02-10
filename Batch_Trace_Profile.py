#@String (label="Threshold method:", choices={"Iso", "Huang", "Li", "Internodes"}, style="listBox") th_method
#@File[] (label="Select the images to work on...", style="extensions:png/jpg/tif/ics") imgs
#@Integer  (label="Tracing channel:", style="spinner") tracing_ch
#@Integer  (label="Analysis channel:", style="spinner") analysis_ch
#@Integer  (label="Trace width (px):", style="spinner") stroke_width
#@File (label="Output folder:", style="directory") output_folder
#@String (visibility=MESSAGE, required=false, value="If you desire to continue a previous analysis please select a parameter file." ) param_label
#@File (label="Parameters file: ", style="extensions:json", required=false) param_file
#@Context context

# Boilerplate to extend modules search path #
from sys import path
import os.path
from java.lang.System import getProperty
jython_scripts = os.path.join(getProperty('user.home'), 'Jython_scripts')
path.append(jython_scripts)
#=========================================#

from IBPlib.ij.Routines import batch_parameters
from IBPlib.ij.Routines import tracing_and_linescanning

# Create params file if none is suplied, else load it.
if param_file:
	bp = batch_parameters.Batch_Parameters.from_json(param_file.toString())
else:
	imgs_path_list = [img.toString() for img in imgs]
	batch_schema = tracing_and_linescanning.get_batch_schema()
	if not output_folder.exists():
		output_folder.mkdir()
	bp = batch_parameters.Batch_Parameters(batch_schema, tracing_and_linescanning.__BATCH_NAME__)
	bp.set("raw_images", imgs_path_list)
	bp.set("th_method", str(th_method))
	bp.set("stroke_width", stroke_width)
	bp.set("output_folder", str(output_folder.toString()))
	bp.set("analysis_ch", analysis_ch)
	bp.set("tracing_ch", tracing_ch)
	bp.to_json_file(output_folder.toString())
	
tracing_and_linescanning.batch_run(context, bp)