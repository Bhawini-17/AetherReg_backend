# test_assigner.py

from task_assigner import assign_task

obligation_text = "Submit KYC compliance report by 30th September 2025."
compliance_area = "KYC"
deadline = "30 September 2025"

assignment = assign_task(obligation_text, compliance_area, deadline)

print("\n📌 Assigned Task:")
print(f"Task        : {assignment['task']}")
print(f"Assigned to : {assignment['assigned_to']}")
print(f"Due Date    : {assignment['due_date']}")
