frappe.listview_settings['Project Task'] = {
	get_indicator : function(doc) {
        return [__(doc.status),{
			"WIP":"blue",
    		"Under QA":"red",
   			"Completed":"green",
    		"New":"yellow"
		}[doc.Status],"Status,=," + doc.Status];
	}
};
