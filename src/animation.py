#Sophia Cofone 2.26.22
#https://stackoverflow.com/questions/753190/programmatically-generate-video-or-animated-gif-in-python
#https://imageio.readthedocs.io/en/stable/examples.html
#This is option 2 for how we could make a gif. 
#The function actually reads a folder for the images so the user would not have to change anything, but its important that the files are named correctly when they are saved/created

import imageio as iio
import os
from datetime import datetime

#define a new funtion to transfer string date type into datetime type
def sortdate(strdate):
    strdate.sort(key=lambda date: datetime.strptime(date, "%m-%d-%Y.png"))
    return strdate

def create_gif(filename_save):
    """This function creates a gif animation from a folder of png images
    Parameters:
        filename_save: str, the filename to save the gif as
    """
    #makes a list of im NumPy arrays based on a list of .png images (read from folder)
    images = list()

    #this part looks at the img directory and reads in all the files that end with .png (only going to bring in those)
    #read file names of all scatter images.
    strdates=[]
    for filename in os.listdir('img'):
        if filename[-4:] == '.png' and not filename == 'comparison.png':
            strdates.append(filename)
    #trasfer string type filenames to datetime type. sort files according to the date.
    for strdate in sortdate(strdates):        
            f = os.path.join('img',strdate)
            im = iio.imread(f)
            images.append(im)

    #making the gif from the pngs
    iio.mimsave(filename_save,images,duration = 1)

if __name__ == "__main__":
    create_gif('img/animation.gif')
