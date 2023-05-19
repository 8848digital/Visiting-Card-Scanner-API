# Copyright (c) 2023, scanner and contributors
# For license information, please see license.txt
import frappe
import json
from frappe.model.document import Document
from scanner.scanner.API.visiting_card_api import get_visiting
from frappe.model.document import Document


class Scanner(Document):
	def validate(self ,method=None):
		# print("event function",type(self.scan_image1))
		if self.has_value_changed("scan_image1") and (self.scan_image1 == 1):
			print("Running for scan_image1")
			self.visiting_data("image1")

		if self.has_value_changed("scan_image2") and (self.scan_image2 == 1):
			print("Running for scan_image2")
			self.visiting_data("image2")
		

	def visiting_data(self, fieldname):
		print("***")
		try:
			doc_name = self.name
			print("Name",doc_name)
			response = get_visiting(self, fieldname)
			frappe.logger('scanner').exception(response)
			data = response['result']
			print("data",data)
			pred = data[0]['prediction']
			
			for i in pred:
				self.append("visitings_data",{
				"label" : i['label'],
				"ocr_text" : i['ocr_text']
			})
			
		except Exception as e:
			frappe.logger('scanner').exception(e)


	
	
			