# Copyright (c) 2026, Dharanidharan and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class MentorProfile(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		from shadow_track.resource_management.doctype.mentees_active_list.mentees_active_list import (
			MenteesActiveList,
		)

		active_mentees_count: DF.Int
		amended_from: DF.Link | None
		expertise_areas: DF.SmallText | None
		maximum_shadow_capacity: DF.Int
		mentees_active_list: DF.Table[MenteesActiveList]
		mentor_email: DF.Data
		mentor_name: DF.Data
		mentor_number: DF.Data | None
	# end: auto-generated types

	pass
