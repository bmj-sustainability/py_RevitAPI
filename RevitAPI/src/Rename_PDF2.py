#===============================================================================
# Set up
#===============================================================================
# Standard:
from config.config import *
import re
import logging.config
import unittest

import os

from collections import defaultdict
import sys

import csv
#===============================================================================
# Other modules
#===============================================================================

#===============================================================================
# Logging
#===============================================================================
print(ABSOLUTE_LOGGING_PATH)
logging.config.fileConfig(ABSOLUTE_LOGGING_PATH)
myLogger = logging.getLogger()
myLogger.setLevel("DEBUG")

#===============================================================================
# Main script
#===============================================================================
logging.info("Python version : {}".format(sys.version))

def rename():
    logging.debug("Start")
    
    folder = r"C:\Users\jon\Desktop\PDF Print"
    os.chdir(folder)
    
    for i,filename in enumerate(os.listdir(folder)):
        #if filename.startswith("cheese_"):
        #    os.rename(filename, filename[7:])
        #new_name = filename.replace("C_PDF IKEA_DATA_DATA - Sheet - ","")
        #new_name = filename.replace("C_Users_jon_Documents_DATA - Sheet - ","")
        #new_name = filename.replace("C_Users_jon_Documents_DATA - Sheet - ","")
        new_name = filename.replace("C_PDF NEW_x - Sheet - ","")
        
        new_name = new_name.replace("--","")

        print(filename)
        print(new_name)
        
        #full_path
        if 1:
            try:
                os.rename(filename, new_name)
            except FileExistsError:
                print("File exists")
                pass
        
        #print(i,filename)
        
    logging.debug("Done")

def flip_name():
    logging.debug("Start")
    
    folder = r"C:\Users\jon\Desktop\PDF Print"
    os.chdir(folder)
    
    for i,filename in enumerate(os.listdir(folder)):
        #if filename.startswith("cheese_"):
        #    os.rename(filename, filename[7:])
        root = os.path.splitext(filename)[0]
        elements = root.split(" - ")
        flipped = [elements[1],elements[0]] 
        new_name = " - ".join(flipped)
        #print(elements, new_name)
        new_name = new_name + ".pdf"
        print(filename, new_name)

        print(filename)
        print(new_name)
        
        if 1:
            try:
                os.rename(filename, new_name)
            except FileExistsError:
                print("File exists")
                pass
        
        #print(i,filename)
        
    logging.debug("Done")


if __name__ == '__main__':
    #rename()
    
    flip_name()
