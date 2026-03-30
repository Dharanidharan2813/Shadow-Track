# Copyright (c) 2026, Dharanidharan and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class ManagerProfile(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		amended_from: DF.Link | None
		hr: DF.Link | None
		manager_email: DF.Data | None
		manager_name: DF.Data | None
		manager_phone: DF.Data | None
	# end: auto-generated types

	pass
