import json, requests, io
from PIL import Image, ImageDraw  

class clsImageHandler():
    
    def DrawImage(self, actualimage,imagedetail):
        #Image processing => get image content from URL , convert bytes to PIL image object & draw text inside image
        localimage= io.BytesIO(actualimage)
        image = Image.open(localimage)
        d = ImageDraw.Draw(image)
        d.text((10,10), imagedetail,  fill=(255,255,255,128))
        image.show()
        return
    
    

   





