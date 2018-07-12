import json, requests, io
from PIL import Image, ImageDraw       
import BhasImageHandling, BhasPythonAzureFace,BhasPythonAzureVision

#Example Computer Vision API & Face detection API using Azure 
#Module PIL is an allias of PILLOW , which is a latest fork of PIL ( being deprecated) for image handling

#Read from Access control file to get Azure service URLs and access keys & Image URL
fileref=open("c:/BhaskarWD/access.json")
data=json.load(fileref)     #OR data=json.loads(fileref.read())
FACE_BASE_URL=data['FACE']['BASE_URL']
FACE_KEY=data['FACE']['Key']
VISION_BASE_URL = data['VISION']['BASE_URL']
VISION_KEY = data['VISION']['Key']
Remote_img_url = data['IMAGE']['REMOTE_IMG']
Local_img_url =data['IMAGE']['LOCAL_IMG']
Local_OCR_IMG= data['IMAGE']['OCR_IMG']

#Take user input & depending on Vision or face , instantiate class objects accordingly
usecase = input('Select V-Vision / F-Face :-')
selection = input('Select Local / Remote image :-')

if usecase == 'V':
    purpose = input('Select choice of vision api -analyze / ocr :-')
    VISION_API_URL =VISION_BASE_URL+purpose
    objVision=BhasPythonAzureVision.clsBhasPythonAzureVision(VISION_KEY,VISION_API_URL)

#   Depending on Vision API , respective function from class file is called 
    if purpose=='analyze':
        objVision.BhasVisionAnalyze(selection,Local_img_url,Remote_img_url)
    else:
        Local_img_url =Local_OCR_IMG
        objVision.BhasVisionOcr(selection,Local_img_url,Remote_img_url)
    
    imagedetail=objVision.imagedetail
    actualimage=objVision.actualimage
    
else:                       # Calling face detection use case
    objFace=BhasPythonAzureFace.clsBhasAzureFace(FACE_KEY,FACE_BASE_URL)
    objFace.BhasAzureFaceDetect(selection,Remote_img_url,Local_img_url)
    imagedetail=objFace.imagedetail
    actualimage=objFace.actualimage
    
#call function from user defined class to perform image handling 
objImage = BhasImageHandling.clsImageHandler()
objImage.DrawImage(actualimage,imagedetail) 


