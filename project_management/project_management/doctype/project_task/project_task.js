// Copyright (c) 2021, nilima and contributors
// For license information, please see license.txt

frappe.ui.form.on('Project Task', {
	refresh: function(frm) {
		frm.add_custom_button(__('Get Email Address of Manager'),function(){
			frappe.msgprint(frm.doc.email);
		},__("Utilities"));

	}
});

