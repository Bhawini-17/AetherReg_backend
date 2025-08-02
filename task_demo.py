from task_agent import generate_tasks

text = "All banks must submit the KYC compliance report by 30th September 2025. Failure to comply will result in penalties."

tasks = generate_tasks(text)

print("📌 Extracted Tasks:\n", tasks)
