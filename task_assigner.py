from datetime import datetime

# Dummy department mapping by compliance area keywords
DEPARTMENT_KEYWORDS = {
    "KYC": "Compliance Department",
    "AML": "Anti-Money Laundering Team",
    "report": "Reporting Officer",
    "audit": "Audit Department",
    "loan": "Credit Risk Team",
    "cyber": "IT Security Team",
    "account": "Finance Department",
    "training": "HR Department",
}

def assign_task(obligation_text: str, compliance_area: str = "", deadline: str = "") -> dict:
    assigned_to = "General Compliance Team"

    text = f"{obligation_text} {compliance_area}".lower()
    for keyword, dept in DEPARTMENT_KEYWORDS.items():
        if keyword.lower() in text:
            assigned_to = dept
            break

    try:
        parsed_deadline = datetime.strptime(deadline, "%d %B %Y")
    except:
        try:
            parsed_deadline = datetime.strptime(deadline, "%B %Y")
        except:
            parsed_deadline = deadline  

    return {
        "task": obligation_text,
        "assigned_to": assigned_to,
        "due_date": parsed_deadline if isinstance(parsed_deadline, datetime) else "Unknown"
    }
