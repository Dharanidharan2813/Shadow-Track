# Copyright (c) 2026, Dharanidharan and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class ShodowAssignment(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		from shadow_track.resource_management.doctype.evaluation_log.evaluation_log import EvaluationLog
		from shadow_track.resource_management.doctype.learning_log.learning_log import LearningLog

		amended_from: DF.Link | None
		employee: DF.Link | None
		end_date: DF.Date | None
		evaluation_log: DF.Table[EvaluationLog]
		evaluation_score: DF.Float
		final_decision: DF.Literal["Not Ready", "Ready"]
		learning_log: DF.Table[LearningLog]
		manager: DF.Link | None
		mentor: DF.Link | None
		project: DF.Link | None
		start_date: DF.Date | None
		status: DF.Literal[
			"Draft,", "Pending Approval,", "In Training,", "Evaluation Pending", "Completed", "Extended"
		]
	# end: auto-generated types

	pass
