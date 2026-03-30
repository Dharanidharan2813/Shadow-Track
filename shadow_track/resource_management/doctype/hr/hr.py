# Copyright (c) 2026, Dharanidharan and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class HR(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		hr_email: DF.Data | None
		hr_name: DF.Data | None
		hr_phone: DF.Data | None
	# end: auto-generated types

	pass
