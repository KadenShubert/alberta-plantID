import Filter_observations
import additional_Images
import get_images
import os

# Set directory
os.chdir(os.path.dirname(__file__))

# Process observations
print('====='*5,'| Running "Filter_observations.py" |','====='*5)
Filter_observations.main()
print('====='*5,'| Running "additional_Images.py" |','====='*5)
additional_Images.main()
print('====='*5,'| Running "get_images.py" |','====='*5)
get_images.main()    