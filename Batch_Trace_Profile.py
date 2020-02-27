#@String (label="Threshold method:", choices={"Iso", "Huang", "Li", "Internodes"}, style="listBox") th_method
#@File[] (label="Select the images to work on...", style="extensions:png/jpg/tif") imgs
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
	params_dict = batch_parameters.load(param_file.toString())
else:
	imgs_path_list = [img.toString() for img in imgs]
	params_dict = batch_parameters.save(raw_images=imgs_path_list,
		th_method=th_method,
		stroke_width=stroke_width,
		output_folder=output_folder.toString(),
		analysis_ch=analysis_ch,
		tracing_ch=tracing_ch)
tracing_and_linescanning.batch_run(context, params_dict)