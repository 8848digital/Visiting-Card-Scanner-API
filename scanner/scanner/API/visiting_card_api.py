import frappe
import requests
import os

def get_visiting(self,fieldname):
    url = 'https://app.nanonets.com/api/v2/OCR/Model/ddc44799-2556-4762-85f5-8a83aa110cff/LabelUrls/?async=false'
    headers = {'accept': 'application/x-www-form-urlencoded'}
    path = os.getcwd()
    site = frappe.local.site
    if img:=self.get(fieldname):
        file_path = f'{path}/{site}/public{img}'
    # if self.image2:
    #     file_path = f'{path}/{site}/public{self.image2}'
    files = {'file': open(file_path, 'rb')}
    response = requests.post(url, auth=requests.auth.HTTPBasicAuth('9bf2973c-f54e-11ed-84a6-1a90630ee22b', ''), files=files)
    return response.json()
