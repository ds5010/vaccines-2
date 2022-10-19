#Sophia Cofone 2.26.22
#https://stackoverflow.com/questions/753190/programmatically-generate-video-or-animated-gif-in-python
#https://imageio.readthedocs.io/en/stable/examples.html
#This is option 2 for how we could make a gif. 
#The function actually reads a folder for the images so the user would not have to change anything, but its important that the files are named correctly when they are saved/created
#Sophia Cofone 2.26.22
#https://stackoverflow.com/questions/753190/programmatically-generate-video-or-animated-gif-in-python
#https://imageio.readthedocs.io/en/stable/examples.html
#This is option 2 for how we could make a gif. 
#The function actually reads a folder for the images so the user would not have to change anything, but its important that the files are named correctly when they are saved/created


#Updated 10/19/22 by Robert Lalani

import imageio as iio
import os
import datetime

def create_gif(filename_save):
    """This function creates a gif animation from a folder of png images
    Parameters:
        filename_save: str, the filename to save the gif as
    """
    #makes a list of im NumPy arrays based on a list of .png images (read from folder)
    
    images = list()
    dates = os.listdir('img')
    dates = [x[:-4] for x in dates]
    day_time_list = [] 
    for ts in dates:
        try:
            day_time_list.append(datetime.datetime.strptime(ts,'%m-%d-%Y'))
        except:
            continue 
    #day_time_list = [datetime.datetime.strptime(ts,'%m-%d-%Y') for ts in dates]
    day_time_list.sort()
    sorted_dates = [datetime.datetime.strftime(ts,'%m-%d-%Y') for ts in day_time_list]
    sorted_dates = [x+'.png' for x in sorted_dates]
    print(sorted_dates) 
    
    


    #this part looks at the img directory and reads in all the files that end with .png (only going to bring in those)
    #for filename in sorted(os.listdir('img')):]
    for filename in sorted_dates: 
        if filename[-4:] == '.png' and not filename == 'comparison.png':
            f = os.path.join('img',filename)
            im = iio.imread(f)
            images.append(im)

    #making the gif from the pngs
    iio.mimsave(filename_save,images,duration = 1)

if __name__ == "__main__":
    create_gif('img/animation.gif')
