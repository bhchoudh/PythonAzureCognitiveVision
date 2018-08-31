import json, requests, io
from PIL import Image, ImageDraw       

class clsBhasAzureFace():
    def __init__(self,KEY,API_URL):
        self.KEY = KEY  
        self.API_URL = API_URL 
        self.imagedetail=''
        self.actualimage=''

#For Local image actual image is sent as octet , for remote only URL as JSON works

# Function for Face Detect API call 
# *********************************************       
    def BhasAzureFaceDetect(self,selection,Remote_img_url,Local_img_url):
        params = {'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses'}   # Optional Params:- 'returnFaceId': 'true','returnFaceLandmarks': 'false',
        if selection == 'R':
            actualimage = requests.get(Remote_img_url).content
            headers = {'Ocp-Apim-Subscription-Key': self.KEY,'contentType':'application/json','accept':'application/json'}
            response = requests.post(self.API_URL, params=params, headers=headers, json={'url': Remote_img_url})
        else:
            actualimage= open(Local_img_url,'rb').read()
            headers = {'Ocp-Apim-Subscription-Key': self.KEY,'Content-Type': 'application/octet-stream'}
            response = requests.post(self.API_URL, params=params, headers=headers, data=actualimage)

        resultdata= response.json()
        print(json.dumps(resultdata,indent=4))
        for item in resultdata:
            self.imagedetail =self.imagedetail+item['faceAttributes']['gender']+' '+ str(item['faceAttributes']['age'])+'  '

        self.actualimage=actualimage
        file=open('imagedetail.json','w')
        file.write(json.dumps(resultdata,indent=4))
        return

