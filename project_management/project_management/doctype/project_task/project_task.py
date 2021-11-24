# -*- coding: utf-8 -*-
# Copyright (c) 2021, nilima and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class ProjectTask(Document):
	def on_update(self):
		new_task = frappe.get_all("Project Task",fields=['name','_assign'])
		assignee = new_task[0]._assign
		frappe.sendmail(recipients=assignee,subject="Project Task assigned", message='task assigned!')