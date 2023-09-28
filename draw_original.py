# Final Project
# Isabelle Kwan and Gurleen Kang
# November 23, 2022

import cmpt120image
import random

def recolorImage(img,color):
    """Recolours all non-white pixels"""
    newImage = cmpt120image.getBlackImage(len(img),len(img[0]))
    newR = color[0]
    newG = color[1]
    newB = color[2]
    for row in range(len(img)):
            for col in range(len(img[0])):
                pixel = img[row][col]
                newPixel = newImage[row][col]
                r = pixel[0]
                g = pixel[1]
                b = pixel[2]
                if r < 245 and g < 245 and b < 245:
                    newPixel[0] = newR
                    newPixel[1] = newG
                    newPixel[2] = newB
                else:
                    newPixel[0] = pixel[0]
                    newPixel[1] = pixel[1]
                    newPixel[2] = pixel[2]
                    
    return newImage
  

def minify(img):
    """ Shrinks image by half (length and width) """
    height = len(img)   # Number of rows
    width = len(img[0]) # Number of columns
    minImg = cmpt120image.getBlackImage(int(height/2),int(width/2))
    minImgr = 0
    minImgc = 0
    
    for row in range(0,height,2):
        minImgc = 0
        
        for col in range(0,width,2):
            # Add all 2x2 pixels RGB values
            newR =(img[row][col][0] + img[row][col + 1][0] + img[row + 1][col][0]
                        + img[row + 1][col + 1][0])
            newG =(img[row][col][1] + img[row][col + 1][1] + img[row + 1][col][1]
                        + img[row + 1][col + 1][1])
            newB =(img[row][col][2] + img[row][col + 1][2] + img[row + 1][col][2]
                        + img[row + 1][col + 1][2])
            # Calculate average and assign to pixels in new canvas
            minImg[minImgr][minImgc] = [int(newR/4),int(newG/4),int(newB/4)]
            # Move down the row 
            minImgc += 1
        # Move to next row after iterating through the previous one
        minImgr += 1

    return minImg

  
def mirror(img):
    """Flips image on y-axis"""
    newImage = cmpt120image.getBlackImage(len(img),len(img[0]))
    length = int(len(newImage[0]))-1
    for row in range(len(img)):
            for col in range(len(img[0])):
                pixel = img[row][col]
                newImage[row][length-col] = pixel
        
    return newImage

  
def drawItem(canvas,item,row,col):
    """Draws item on canvas at given coordinates"""
    for imagerow in range(len(item)):
            for imagecol in range(len(item[0])):
                pixel = item[imagerow][imagecol]
		# draw non white pixels:
                r = pixel[0]
                g = pixel[1]
                b = pixel[2]
                if r < 245 and g < 245 and b < 245:
                    canvas[imagerow + row][imagecol + col] = pixel

    return canvas

  
def distributeItems(canvas,item,n):
    """Draws item on canvas at random coordinates, n-times"""
    for i in range(n):
        rand_row = random.randint(0,len(canvas)-len(item))
        rand_col = random.randint(0,len(canvas[0])-len(item[0]))
        drawItem(canvas,item,rand_row,rand_col)
        
    return canvas
 










    

