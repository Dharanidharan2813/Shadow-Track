# Copyright (c) 2026, Dharanidharan and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class EmployeeSkillTable(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		employee_skills: DF.Data
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		skill_rating: DF.Rating
	# end: auto-generated types

	pass
