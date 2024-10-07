planner = {
    "Slaap": 8,
    "Werk":  8,
    "Ontspan": 8
}
dag = 24
for activiteit, tijd in planner.items():
    print(f"ik {activiteit} {tijd} uur op een dag")
    dag = dag - tijd

print(f"je hebt {dag} uur over op de dag")