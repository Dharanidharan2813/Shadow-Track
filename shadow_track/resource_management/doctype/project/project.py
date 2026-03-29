# Copyright (c) 2026, Dharanidharan and contributors
# For license information, please see license.txt

# import frappe
from frappe.utils.nestedset import NestedSet


class Project(NestedSet):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		amended_from: DF.Link | None
		assigned_manger: DF.Link | None
		is_group: DF.Check
		lft: DF.Int
		old_parent: DF.Link | None
		parent_project: DF.Link | None
		project_name: DF.Data | None
		required_skill_set: DF.SmallText | None
		rgt: DF.Int
		status: DF.Literal["Active", "In-Active"]
	# end: auto-generated types

	pass
