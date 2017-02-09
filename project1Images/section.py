from PIL import Image # This allows to import images from pillow and use them

def medianOdd(myList):    #stores the mylist in the variables listLenth
    listLength = len(myList) #Sort the list
    sortedValues = sorted(myList) #Location of middle value
    middleIndex = (listLength + 1)//2 - 1 #return the object
    return sortedValues[middleIndex] #when it finds what its looking for to exit the method

imgList = [] # to store images 

img1 = (Image.open("1.png")) # to open a certain image to use
img2 = (Image.open("2.png"))
imgList.append(Image.open("3.png"))
imgList.append(Image.open("4.png"))
imgList.append(Image.open("5.png"))
imgList.append(Image.open("6.png"))
imgList.append(Image.open("7.png"))
imgList.append(Image.open("8.png"))
imgList.append(Image.open("9.png"))
    
pictureWidth, picturwHeight = imgList[0].size

redPixelList = [] #to store the red pixel
greenPixelList = [] #to store the green pixel
bluePixelList = [] #to store the blue pixel

canvas = Image.new("RGB", (pictureWidth, picturwHeight)) #to make a new image canvas so that the finish product can go on it

for x in range(pictureWidth): # this loop is to check each pixel on all 9 images and take out the pixel 
    for y in range(picturwHeight): #that most have to make a picture without the guy
        for myImage in imgList: # to run this loop through every pixel in all 9 images
            myBlue, myGreen, myRed = myImage.getpixel((x,y)) # this gets the pixels
            redPixelList.append(myRed) # to get the list of pixels of this color
            greenPixelList.append(myGreen) # to get the list of all pixels of this color
            bluePixelList.append(myBlue) # to get the list of all pixels of this color
            
        medianRed = medianOdd(redPixelList)  # gets all the red pixels that are stored in the list and gets the median of them 
        medianGreen = medianOdd(greenPixelList)    # gets all the green pixels that are stored in the list and gets the median of them 
        medianBlue = medianOdd(bluePixelList)   # gets all the blue pixels that are stored in the list and gets the median of them 
            
        canvas.putpixel((x,y), (medianRed, medianGreen, medianBlue))  # To put the new pixels that we got from all images on the new one  
            
        redPixelList = [] #to close the stored list
        greenPixelList = []   
        bluePixelList = []    
            
canvas.save("newpic.png") # to make a new file for the new immage to in