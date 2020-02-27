#@File (label="Parameters file: ", style="extensions:json", required=true) param_file

# Boilerplate to extend modules search path #
from sys import path
import os.path
from java.lang.System import getProperty
jython_scripts = os.path.join(getProperty('user.home'), 'Jython_scripts')
path.append(jython_scripts)
#=========================================#

from IBPlib.ij.Routines import batch_parameters
from IBPlib.ij.Routines import tracing_and_linescanning

params_dict = batch_parameters.load(param_file.toString())
tracing_and_linescanning.batch_profile_from_threshold(params_dict)