#Sophia Cofone 2.26.22
#https://stackoverflow.com/questions/753190/programmatically-generate-video-or-animated-gif-in-python
#https://imageio.readthedocs.io/en/stable/examples.html
#This is option 2 for how we could make a gif. 
#The function actually reads a folder for the images so the user would not have to change anything, but its important that the files are named correctly when they are saved/created

import imageio as iio
import os
import glob  #changes from meghDev
import time #changes from meghDev

def create_gif(filename_save):
    """This function creates a gif animation from a folder of png images
    Parameters:
        filename_save: str, the filename to save the gif as
    """
    #makes a list of im NumPy arrays based on a list of .png images (read from folder)
    images = list()

    #Changes from meghDev
    dir_name = 'img/'
    list_of_files = filter( os.path.isfile,
                        glob.glob(dir_name + '*') )
    
    list_of_files = sorted( list_of_files,
                        key = os.path.getmtime) 
    #to here
    
    #this part looks at the img directory and reads in all the files that end with .png (only going to bring in those)
    for filename in list_of_files:  #changes from meghDev        #sorted(os.listdir('img')):
        if filename[-4:] == '.png' and not filename == 'comparison.png':
            f = os.path.join('img',filename)
            im = iio.imread(f)
            images.append(im)

    #making the gif from the pngs
    iio.mimsave(filename_save,images,duration = 1)

if __name__ == "__main__":
    create_gif('img/animation.gif')
