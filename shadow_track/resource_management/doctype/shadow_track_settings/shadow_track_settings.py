# Copyright (c) 2026, Dharanidharan and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class ShadowTrackSettings(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		maximum_shadow_duration: DF.Int
		minimum_passing_score: DF.Float
		notification_preferences: DF.Check
		notify_prefers: DF.Literal["Daily", "Weekly", "Monthly", "Quarterly", "Yearly"]
		reminder_intervals_for_evaluation: DF.Int
	# end: auto-generated types

	pass
