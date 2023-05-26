import frappe
import requests
import os

def get_visiting(self,fieldname):
    url = 'https://app.nanonets.com/api/v2/OCR/Model/' + self.secret + '/LabelUrls/?async=false'
    headers = {'accept': 'application/x-www-form-urlencoded'}
    path = os.getcwd()
    site = frappe.local.site
    if img:=self.get(fieldname):
        file_path = f'{path}/{site}/public{img}'
    # if self.image2:
    #     file_path = f'{path}/{site}/public{self.image2}'
    files = {'file': open(file_path, 'rb')}
    response = requests.post(url, auth=requests.auth.HTTPBasicAuth(self.key, ''), files=files)
    return response.json()
