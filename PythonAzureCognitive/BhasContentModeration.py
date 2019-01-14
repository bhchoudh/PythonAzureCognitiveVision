import json, requests, io

class clsBhasContentModeration():

    def __init__(self,KEY,API_URL):
        self.KEY = KEY  
        self.API_URL = API_URL 

#Function for Image moderation ( as of now only URL based image works)                
    def ImageModerate(self,selection, contentpath):
        params = {'CacheImage': 'False'}
        if selection == 'R':
            content = {"DataRepresentation":"URL","Value":contentpath}
            headers = {'Content-Type': 'application/json','Ocp-Apim-Subscription-Key': self.KEY}
            response = requests.post(self.API_URL, params=params, headers=headers, json=content)
        else:   # NOT  TESTED YET
            content = open(contentpath,'rb').read()
            headers = {'Content-Type': 'image-jpeg','Ocp-Apim-Subscription-Key': self.KEY}
            response = requests.post(self.API_URL, params=params, headers=headers, data=content)        
        
        resultdata= response.json()
        print(json.dumps(resultdata,indent=4))
        return

#Function for Text Moderation 
    def TextModerate(self,selection, content):
        content = '{'+content+'}'
        headers = {'Content-Type': 'text/plain','Ocp-Apim-Subscription-Key': self.KEY}
        params = {'autocorrect': 'TRUE','PII': 'TRUE','classify': 'True'}
        response = requests.post(self.API_URL, params=params, headers=headers, json=content)
        resultdata= response.json()
        print(json.dumps(resultdata,indent=4))
        return



