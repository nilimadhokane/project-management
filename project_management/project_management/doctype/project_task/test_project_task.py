# -*- coding: utf-8 -*-
# Copyright (c) 2021, nilima and Contributors
# See license.txt

import frappe
import frappe.defaults
import unittest


class TestProjectTask(unittest.TestCase):
    def test_doctype_created(self):
        task1 = frappe.get_doc({
        "doctype": "Project Task",
        "task_title" : "Test Project Task 1",
        "project_id" : "11-21-001"
        })
        task1.insert()
        self.assertTrue(frappe.db.exists("Project Task","Test Project Task 1"))

    def test_user(self):
        frappe.set_user("nilima.d@indictranstech.com")
        task1 = frappe.get_doc({
        "doctype" : "Project Task",
        "task_title" : "Test Project Task 2",
        "project_id" : "11-21-001",
        "owner": "nilima@gmail.com"
        })
        task1.insert()

        admin_user = frappe.db.get_all("Project Task",fields=['name','owner'])
        self.assertEqual(admin_user[0].owner,task1.owner)

    def test_not_allow_devloper(self):
        frappe.set_user("nilima.d@indictranstech.com")
        task1 = frappe.get_doc({
        "doctype" : "Project Task",
        "task_title" : "Test Project Task 3",
        "project_id" : "11-21-001",
        "owner": "nilima.d@indictranstech.com"
        })
        task1.insert()
        doc = frappe.get_doc("Project Task",frappe.db.get_value("Project Task",{"task_title" : "Test Project Task 3"}))
        self.assertFalse(frappe.has_permission("Project Task",doc=task1))


         






