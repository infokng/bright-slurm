# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 14:39:55 2023

@author: Karan
"""

import os
import random
from photoshop import Session
import argparse

# Argument parser
parser = argparse.ArgumentParser(description='Process multiple images using Photoshop')
parser.add_argument('-f', '--folder', type=str, help='Folder path where images are located')
parser.add_argument('-n', '--num_images', type=int, default=1, help='Number of images to process at once')
args = parser.parse_args()

# Folder path where images are located
folder_path = args.folder

# Number of images to process at once
num_images = args.num_images

# Get list of all files in the folder
image_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

with Session() as ps:
    for image_file in image_files[:num_images]:
        # Open an image
        doc = ps.app.open(image_file)

        # Perform a resize operation
        ps.app.activeDocument.resizeImage(200,200)
        # Perform a crop operation
        ps.app.activeDocument.crop([0, 0, 200, 200])
        
        # Change the color of the background and foreground.
        foregroundColor = ps.SolidColor()
        foregroundColor.rgb.red = 255
        foregroundColor.rgb.green = 0
        foregroundColor.rgb.blue = 0
        ps.app.foregroundColor = foregroundColor
        
        backgroundColor = ps.SolidColor()
        backgroundColor.rgb.red = 0
        backgroundColor.rgb.green = 0
        backgroundColor.rgb.blue = 0
        ps.app.backgroundColor = backgroundColor
        
        
        # Perform a rotation operation
        ps.app.activeDocument.rotateCanvas(45)

        
        # Save the image with a random number in the file name
        random_number = str(random.randint(1, 10000))
        file_name, file_extension = os.path.splitext(image_file)
        new_file_name = file_name + "_" + random_number + file_extension
        save_options = ps.JPEGSaveOptions(quality=12)
        doc.saveAs(new_file_name, save_options)
        

        # Close the image
        doc.close()
    ps.app.quit()                
