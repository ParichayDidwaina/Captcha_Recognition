from PIL import Image as image

im = image.open("C:/Users/default.DESKTOP-43PHGMT/Desktop/New folder (9)/captchaImages/5.gif")
finalIm = image.new("P",im.size,255)

#Removing Lines and converting to back and white

for y in range(1,im.size[1]-1):
    for x in range(im.size[0]):
        upperpixel = im.getpixel((x,y-1))
        lowerpixel = im.getpixel((x,y+1))
        pix = im.getpixel((x,y))
        if(pix==1 and (pix==upperpixel or pix==lowerpixel)):
            finalIm.putpixel((x,y),0)
     
finalIm.save("C:/Users/default.DESKTOP-43PHGMT/Desktop/New folder (9)/binary2.gif")
finalIm.show()
