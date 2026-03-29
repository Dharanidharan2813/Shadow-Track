# Copyright (c) 2026, Dharanidharan and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class EvaluationLog(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		communication: DF.Rating
		final_decision: DF.Literal["", "Ready", "Not Ready"]
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		task_handling: DF.Rating
		technical_skill: DF.Rating
	# end: auto-generated types

	pass
