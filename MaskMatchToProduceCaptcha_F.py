from PIL import Image as image
import operator

finalIm = image.open("C:/Users/default.DESKTOP-43PHGMT/Desktop/New folder (9)/binary2.gif")

keys=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

# Matching mask Image with Captcha

letterlist=[]

for y in range(finalIm.size[1]):
    for x in range(finalIm.size[0]):

        for key in keys:

            maskImage = image.open("C:/Users/default.DESKTOP-43PHGMT/Desktop/New folder (9)/maskImages/"+key+".gif")

            maxX = x + maskImage.size[0]
            maxY = y + maskImage.size[1]
            match=0
            total=0
            flag = 0

            if(maxY > finalIm.size[1]):
                continue
            if(maxX > finalIm.size[0]):
                continue

            for j in range(y,maxY):
                for i in range(x,maxX):
                
                    captchaPixel = finalIm.getpixel((i,j))
                    maskImagePixel = maskImage.getpixel((i-x,j-y))

                    if (captchaPixel == 0 and maskImagePixel == captchaPixel):
                        match=match+1
                        total=total+1
                    elif captchaPixel == 0:
                        total=total+1
                    if (maskImagePixel == 0 and maskImagePixel != captchaPixel):
                        flag = 1
                        break
                        
                if(flag):
                    break
            if(flag == 0):
                print(str(match/total)+" "+str(key))
                if(match/total>0.82):
                    letterlist.append([key,maxX])

   
letterlist.sort(key=lambda x: x[1])

finalCaptcha = ""

for letter in letterlist:
    finalCaptcha = finalCaptcha + letter[0]

print(finalCaptcha)