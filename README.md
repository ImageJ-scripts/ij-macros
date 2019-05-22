# IBPlib.imagej-macros


To use the macros in this repo follow the instructions bellow:

### FOR VISNODE1 USERS


1. Download [IBPlib](https://github.com/ImageJ-scripts/Libraries/archive/master.zip) and extract the contents from the Libraries-master folder into the following directory structure:
`\clusterdata\{your username}\Jython_scripts\` *The path should match exactly this pattern, else the macros won't run.

2. Download the wanted macro from [IBPlib.imagej-macros](https://github.com/ImageJ-scripts/ij-macros) to your prefered location in visnode1.

3. Open imageJ and go into `Plugins>New>Macro`. A text editor from imageJ will popup.

4. In the aforementioned text editor go into `File>Open` and select the script that you have downloaded in step `2`. The script will be loaded in a tab in the text editor.

5. In the script tab press the `Run` button in the lower left corner and this will start the macro.



### FOR ANY OTHER USER


1. Download [IBPlib](https://github.com/ImageJ-scripts/Libraries/archive/master.zip) and extract the contents from the Libraries-master folder into your user directory:
`...\{your username}\Jython_scripts\`

2. Download the wanted macro from [IBPlib.imagej-macros](https://github.com/ImageJ-scripts/ij-macros) to your imageJ plugins/macros folder.

3. Start imageJ and go into `Plugins>Macros` to select your desired macro.



#### Color_Merger


This macro merges separate channels of a given image into a composite image using tags set by you to define the  color of each channel.

On your first run it will prompt you to type the desired tags to be used as criteria to define the channel colors.

It uses the title of the images to define which channels belongs to the same image.

For instance, an image named `image1_A488` belongs to the same "root" image as one named `image1_A543`. If the user set `A488` to be used as a tag for the green color and `A543` to be used as a tag for the magenta color the resulting merge will be a composite of 2 channels using the colors associated with each tag.

This macro comes in 2 versions, a hotkey and a batch version.

The hotkey version `Color_merger.py` will only merge opened images and it will try to merge all opened images that have the same "root" title.

The batch version `Color_merger_batch.py` prompts the user for a images `source` folder, a desired `save folder` and the `extension` of the images.

It will then try to load and merge all of the images of the selected extension and save the resulting composites in the `save folder` all at once.



#### Edit_color_tags.py


This script is used to edit the user color tags to be used in `Color_merger`.

It displays a dialog for the user to set the desired tags.



#### Zprojector_batch.py


This macro generate Z-projections of image stacks.

It works in the same way as `Color_merger` but for generating projections.


## images_to_frames_stack.py


This function creates a frames stack using the images inside the selected folder opening the resulting stack after completion.

Optionally it saves the stack in the same folder.


## import_multiple_rois.py


This macro allows the user to import multiple roi files into the roi manager even when no images are open.


## normalized_roi_length.py


This function measures the length of roi in a ".roi" file, scales the pixels and performs a normalization function if provided.