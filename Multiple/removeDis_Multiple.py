from PIL import Image as image

for i in range(0,20):
    im = image.open("C:/Users/default.DESKTOP-43PHGMT/Desktop/New folder (9)/captchaImages/"+str(i)+".gif")
    newIm = image.new("P",im.size,255)
    finalIm = image.new("P",im.size,255)

    #Creating Binary Image

    for y in range(1,im.size[1]-1):
        for x in range(im.size[0]):
            pix = im.getpixel((x,y))
            if(pix==1):
                newIm.putpixel((x,y),0)


    #Removing Lines

    for y in range(1,im.size[1]-1):
        for x in range(im.size[0]):
            upperpixel = im.getpixel((x,y-1))
            lowerpixel = im.getpixel((x,y+1))
            pix = im.getpixel((x,y))
            if(pix==1 and (pix==upperpixel or pix==lowerpixel)):
                finalIm.putpixel((x,y),0)
        
            

    finalIm.save("C:/Users/default.DESKTOP-43PHGMT/Desktop/New folder (9)/Multiple/Multiple_distortions_removed/"+str(i)+".gif")


