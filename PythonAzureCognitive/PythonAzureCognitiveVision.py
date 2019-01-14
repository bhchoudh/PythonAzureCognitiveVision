import json, requests, io
from PIL import Image, ImageDraw       
import BhasImageHandling, BhasPythonAzureFace,BhasPythonAzureVision,BhasContentModeration

#Example Computer Vision API, Face detection , ContentModeration API using Azure 
#Content or image can be a local file or a URL 
#Module PIL is an allias of PILLOW , which is a latest fork of PIL ( being deprecated) for image handling

#Read from Access control file to get Azure service URLs and access keys & Image URL
fileref=open("c:/BhaskarWD/BhaskarCode/access.json")
data=json.load(fileref)     #OR data=json.loads(fileref.read())
FACE_BASE_URL=data['FACE']['BASE_URL']
FACE_KEY=data['FACE']['Key']
VISION_BASE_URL = data['VISION']['BASE_URL']
VISION_KEY = data['VISION']['Key']
CONTMOD_BASE_URL = data['CONTMOD']['BASE_URL']
CONTMOD_KEY = data['CONTMOD']['Key']

#Remote_img_url = data['IMAGE']['REMOTE_IMG']
#Local_img_url =data['IMAGE']['LOCAL_IMG']
#Local_OCR_IMG= data['IMAGE']['OCR_IMG']

#Take user input & depending on Vision, face or content moderation instantiate class objects accordingly
usecase = input('Select V-Vision / F-Face /OC-Optiocal Character /MT-ModerateText / MI- ModerateImage :-')
selection = input('Select (L)ocal / (R)emote / (F)ile image/content :-')
contentpath = input('Enter image/content path or URL:-')


if usecase == 'V':  #Image analysis using computer vision API
    VISION_API_URL =VISION_BASE_URL+'analyze'
    objVision=BhasPythonAzureVision.clsBhasPythonAzureVision(VISION_KEY,VISION_API_URL)
    #objVision.BhasVisionAnalyze(selection,Local_img_url,Remote_img_url)
    objVision.BhasVisionAnalyze(selection,contentpath)
    imagedetail=objVision.imagedetail
    actualimage=objVision.actualimage
    #call function from user defined class to perform image handling 
    objImage = BhasImageHandling.clsImageHandler()
    objImage.DrawImage(actualimage,imagedetail) 

elif usecase == 'OC':    # Optical character recognition using computer vision API
    #Local_img_url =Local_OCR_IMG
    VISION_API_URL =VISION_BASE_URL+'ocr'
    objCharacter=BhasPythonAzureVision.clsBhasPythonAzureVision(VISION_KEY,VISION_API_URL)
    #objCharacter.BhasVisionOcr(selection,Local_img_url,Remote_img_url)
    objCharacter.BhasVisionOcr(selection,contentpath)
    imagedetail=objCharacter.imagedetail
    actualimage=objCharacter.actualimage
    #call function from user defined class to perform image handling 
    objImage = BhasImageHandling.clsImageHandler()
    objImage.DrawImage(actualimage,imagedetail) 

elif usecase == 'MT':    # Text Content Moderation
    content= input("Insert local content:- ")
    CONTMOD_BASE_URL =CONTMOD_BASE_URL+'/ProcessText/Screen'
    objContMod=BhasContentModeration.clsBhasContentModeration(CONTMOD_KEY,CONTMOD_BASE_URL)
    objContMod.TextModerate(selection,content)
    #imagedetail=objCharacter.imagedetail
    #actualimage=objCharacter.actualimage
   
elif usecase == 'MI':    # Image Content Moderation
    CONTMOD_BASE_URL =CONTMOD_BASE_URL+'/ProcessImage/Evaluate'
    objContMod=BhasContentModeration.clsBhasContentModeration(CONTMOD_KEY,CONTMOD_BASE_URL)
    objContMod.ImageModerate(selection,contentpath)
    #imagedetail=objCharacter.imagedetail
    #actualimage=objCharacter.actualimage
    #call function from user defined class to perform image handling 
    #objImage = BhasImageHandling.clsImageHandler()
    #objImage.DrawImage(actualimage,imagedetail) 

else:                       # Calling face detection use case
    objFace=BhasPythonAzureFace.clsBhasAzureFace(FACE_KEY,FACE_BASE_URL)
    #objFace.BhasAzureFaceDetect(selection,Remote_img_url,Local_img_url)
    objFace.BhasAzureFaceDetect(selection,contentpath)
    imagedetail=objFace.imagedetail
    actualimage=objFace.actualimage
    #call function from user defined class to perform image handling 
    objImage = BhasImageHandling.clsImageHandler()
    objImage.DrawImage(actualimage,imagedetail) 
    



