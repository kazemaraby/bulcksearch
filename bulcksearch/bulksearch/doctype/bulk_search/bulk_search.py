# Copyright (c) 2023, kazem and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils.xlsxutils import (
	read_xls_file_from_attached_file,
	read_xlsx_file_from_attached_file,
)
from frappe.utils.xlsxutils import make_xlsx

		
class BulkSearch(Document):
	@frappe.whitelist()
	def get_data(self):
		try:  
			#  [ [] , []]
			rows=[]
			self.sales_orders=[]
			file_extension = self.so_sheet.split(".")
			if file_extension[1] == "xlsx":
				rows = read_xlsx_file_from_attached_file(file_url=self.so_sheet)
				for i in range(1,len(rows)):
					if frappe.db.exists("Sales Order",rows[i][0]):
						so = frappe.get_doc("Sales Order",rows[i][0])
						self.append("sales_orders",{
							"sales_order":rows[i][0],
							"customer":so.customer
						}) 
			else:
				frappe.throw(_("you can only upload .xlsx files"))
		except Exception as ex:
			print(str(ex))

@frappe.whitelist()
def download_template():
	data = [["name"],["SAL-ORD-2023-00002"]]
	xlsx_file = make_xlsx(data, "tempdata")
	frappe.response["filename"] = "tempdata" + ".xlsx"
	frappe.response["filecontent"] = xlsx_file.getvalue()
	frappe.response["type"] = "binary"
