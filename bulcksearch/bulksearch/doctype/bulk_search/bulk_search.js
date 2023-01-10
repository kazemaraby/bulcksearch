// Copyright (c) 2023, kazem and contributors
// For license information, please see license.txt

frappe.ui.form.on('Bulk Search', {
	// refresh: function(frm) {

	// }
	search:(frm)=>{
			if(frm.doc.so_sheet !=''){
				frappe.call({
					method:"get_data",
					doc:frm.doc,
					callback(r){
						frm.refresh_fields("sales_orders")
					}	
				})
			}else{
				frappe.throw(__("You must select sheet first"))
			}
	},
	download_template:(frm)=>{
		window.open("/api/method/bulcksearch.bulksearch.doctype.bulk_search.bulk_search.download_template")
		// frappe.call({
		// 	method:"download_template",
		// 	doc:frm.doc,
		// 	callback(r){
		// 			console.log(r)
		// 	}
		// })
	}
});
