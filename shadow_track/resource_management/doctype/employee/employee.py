# Copyright (c) 2026, Dharanidharan and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Employee(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		from shadow_track.resource_management.doctype.employee_skill_table.employee_skill_table import (
			EmployeeSkillTable,
		)

		amended_from: DF.Link | None
		assigned_project: DF.Link | None
		current_status: DF.Literal["Shadow", "Active", "In-Active"]
		employee_email: DF.Data
		employee_joined_date: DF.Date | None
		employee_name: DF.Data
		employee_phone_number: DF.Data | None
		employee_role: DF.Literal["", "Intern", "Developer", "Tester", "Analyst", "Data Engineer"]
		employee_skill_table: DF.Table[EmployeeSkillTable]
		experiences_level: DF.Literal["", "Fresher", "Intermediate", "Expert"]
		year_of_experiences: DF.Int
	# end: auto-generated types

	pass
