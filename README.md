# Plant Identification

The goal of this project was to provide an application that was capable of identifying a variety of plant species specifically within Alberta due to the diverse ecosystem and to provide a better solution for repopulating those ecosystems during construction projects.

Images were gathered from publically available sources from a variety of groups within this project. The images for the Canada Buffaloberry were collected using an API script that takes images in the public domain from a source of peer-reviewed plant images. These images were then manually labelled with plant names and bounding boxes by the groups that collected them. A YOLOv10 Object Detection model was trained using these images, saved, and then accessed through a Gradio demo.

### Repo Structure
- Canada Buffalo Berry collection script: using python to scrape images from the site
- YOLOv10 training notebook: This jupyter notebook contains the code for training/saving the model
- Image & structure Formatting: This python file took all the folders from the groups and properly places them into the strucutre required by YOLO for training purposes, adjusts labels where necessary and also removes any images with missing label files
- Gradio demo file: This file contains the code required for launching the Gradio demo for testing the model
