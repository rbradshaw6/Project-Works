#Robert Bradshaw and John Yi
#rbradshaw6@gatech.edu
#"We worked on the homework assignment alone, using only this semester's course materials."


from Myro import *
from Graphics import *
import math


def imageTint():
    x = takePicture()
    image = makePicture(x)
    for pixel in getPixels(image):
        r, g, b = getRGB(pixel)
        setRed(pixel,255)
    show(image)

#imageTint("RA_colorswap_source.gif")


def multipleExposure(image1,image2):
    pic1 = makePicture(image1)
    pic2 = makePicture(image2)
    swag = 0
    for panicAttackIsTheBestProgressiveMetalSong in range(0,getWidth(pic2)):
        dank = 0
        for justKiddingBatteryByMetallicaIsTheBestSong in range(0,getHeight(pic2)):
            redValue = (getRed(getPixel(pic1,swag,dank)) + getRed(getPixel(pic2,swag,dank)))/2
            greenValue = (getGreen(getPixel(pic1,swag,dank)) + getGreen(getPixel(pic2,swag,dank)))/2
            blueValue = (getBlue(getPixel(pic1,swag,dank)) + getBlue(getPixel(pic2,swag,dank)))/2
            color = makeColor(redValue,greenValue,blueValue)
            setColor(getPixel(pic1,panicAttackIsTheBestProgressiveMetalSong,justKiddingBatteryByMetallicaIsTheBestSong),color)
            dank = dank + 1
            print(getPixel(pic1,swag,dank))
        swag = swag + 1
    show(pic1)

def greenScreen(image,replace):
    pic1 = makePicture(image)
    pic2 = makePicture(replace)
    swag = 0
    for x in range(0,getWidth(pic1)):
        dank = 0
        for y in range(0,getHeight(pic1)):

            dank = dank + 1
            picpix = getPixel(pic1,swag,dank)
            r,g,b = getRGB(picpix)


            if g > b and g > r:
                pic2pix = getPixel(pic2,swag,dank)
                r1,g1,b1 = getRGB(pic2pix)
                color = makeColor(r1,g1,b1)
                setColor(getPixel(pic1,swag,dank),color)
        swag = swag + 1
        show(pic1)

def combine(image,image2):
    pic1 = makePicture(image)
    pic2 = makePicture(image2)
    heights = [getHeight(pic1),getHeight(pic2)]

    maxHeight = max(heights)
    combined = makePicture((getWidth(pic1)+getWidth(pic2)+10),maxHeight)

    swag = 0
    for x in range(0,getWidth(pic1)):
        dank = 0
        for y in range(0,getHeight(pic1)):
            dank = dank + 1

            firstPix = getPixel(pic1,swag,dank)
            r,g,b = getRGB(firstPix)

            color = makeColor(r,g,b)
            setColor(getPixel(combined,swag,dank),color)


        swag = swag + 1

    swag1 = swag
    print(swag1)
    print(getWidth(pic2))
    for x in range(swag1,(swag1+getWidth(pic2))):
         dank = 0
         for y in range(0,getHeight(pic2)):
            dank = dank + 1
            secondPix = getPixel(pic2,swag1,dank)
            r1,g1,b1 = getRGB(secondPix)

            color1 = makeColor(r1,g1,b1)
            setColor(getPixel(combined,(swag1),dank),color1)

         swag1 = swag1 + 1
    show(combined)

def makeBright():
    pic=takePicture()
    savePicture(pic,'makeBright_before.jpg')
    for pixel in getPixels(pic):
        r,g,b = getRGB(pixel)
        d=(r+120,g+120,b+120)
        setRGB(pixel,d)
    savePicture(pic,'makeBright_after.jpg')

def makeDark():
    pic = makePicture("RA_colorswap_source.gif")
    pic = takePicture()
    savePicture(pic,'makeDark_before.jpg')
    piclist = []
    for x in range(6):
        for pixel in getPixels(pic):
            r,g,b = getRGB(pixel)
            d=(r-100,g-100,b-100)
            setRGB(pixel,d)
        piclist.append(pic)
        savePicture(piclist,'makeDark_after.gif')



def fade():
    piclist=[]
    for x in range(6):
    pic=takePicture()
    for pixel in getPixels(pic):
        r,g,b = getRGB(pixel)
        black=(0,0,0)
        d=(r-30*x,g-30*x,b-30*x)
        if x<5:
            setRGB(pixel,d)
        elif x==5:
            setRGB(pixel,black)
    piclist.append(pic)
    savePicture(piclist,'fade.gif') 

def overlay():
    pic=takePicture()
    savePicture(pic,'overlay_before.jpg')
    for x in range(100,200):
        for y in range(100,200):
            pix=getPixel(pic,x,y)
            setRed(pix,255)
            setGreen(pix,0)
            setBlue(pix,0)
    savePicture(pic,'overlay_after.jpg')
