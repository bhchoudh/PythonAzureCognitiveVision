import json, requests, io
from PIL import Image, ImageDraw   

class clsBhasPythonAzureVision():

    def __init__(self,KEY,API_URL):
        self.KEY = KEY  
        self.API_URL = API_URL 
        self.imagedetail=''
        self.actualimage=''

#For Local image actual image is sent as octet , for remote only URL as JSON works
# Function for Computer Vision OCR  API call 
# ******************************************
    def BhasVisionOcr(self,selection, Local_img_url,Remote_img_url):
        params  = {'language': 'unk', 'detectOrientation': 'true'}
        if selection == 'R':
            actualimage = requests.get(Remote_img_url).content
            headers = {'Ocp-Apim-Subscription-Key': self.KEY,'contentType':'application/json','accept':'application/json'}
            response = requests.post(self.API_URL, params=params, headers=headers, json={'url': Remote_img_url})
        else:
            actualimage= open(Local_img_url,'rb').read()
            headers = {'Ocp-Apim-Subscription-Key': self.KEY,'Content-Type': 'application/octet-stream'}
            response = requests.post(self.API_URL, params=params, headers=headers, data=actualimage)
       
        resultdata= response.json()
        #ocrfile= open('ocrdata.json','a')
        for region in resultdata['regions']:
            #ocrfile.writelines(json.dumps(region['lines'],indent=4))
            for line in region['lines']:
                for word in line['words']:
                    self.imagedetail=self.imagedetail+'     '+word['text']
                self.imagedetail=self.imagedetail+'\n'
            print(self.imagedetail)    
        self.actualimage=actualimage
        return

# Function for Computer Vision Analyze API call 
# *********************************************
    def BhasVisionAnalyze(self,selection, Local_img_url,Remote_img_url):
        params = {'visualFeatures': 'Categories,Description,Color'}
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
        self.imagedetail=self.imagedetail+resultdata["description"]["captions"][0]["text"]
        self.actualimage=actualimage
        return

