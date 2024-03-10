Model Training: CSC_3730_Project.ipynb
This notebook contains the training and some testing of the model. It requires the data to be downloaded and the path to the dataset directory to be given. Example:
|-Project Folder
| |-CSC_3730_Project.ipynb
| |-dataset
| | |-train
| | | |-buildings
| | | | |-image.jpg
| | | | |-image2.jpg
| | | |-glaciers
| | | | |-image.jpg
| | | | |-image2.jpg
...
load_dataset("dataset/train")
Otherwise, running the cells one by one in order will be fine.
Image Size must be 150x150 or model will not run.
The notebook requires numpy, tensorflow, pillow, and matplotlib to run.


Demo: Demo.ipynb
This notebook loads models and code to run our trained models on input images specified.
|-Project Folder
| |-Demo.ipynb
| |-3Layers_64.keras
| |-4Layers_64.keras
| |-5Layers_64.keras
| | |-images
| | | |-img1.jpg
| | | |-img2.jpg
...
output("images/img1.jpg")
Run the cells in order and the above is an example of using our output function.
The notebook requires numpy, tensorflow, pillow, and matplotlib to run.

Links to Download Model:
3Layers ->	https://drive.google.com/file/d/1l58jsyFGigrRWozcUF4B2RhC7w04D6P8/view?usp=sharing
4Layers ->	https://drive.google.com/file/d/1fWlqJ1nkUxF9ajqg-eswZtP3Yfoj1OLd/view?usp=sharing
5Layers ->	https://drive.google.com/file/d/1Y_gTVuW_oTfWA2XprBokFmUAZojsyTgw/view?usp=sharing

Links to Download Data:
https://www.kaggle.com/datasets/puneet6060/intel-image-classification/data
