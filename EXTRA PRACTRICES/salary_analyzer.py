def department_summary(employees):
    if employees == []:
        return {}

    data = {}

    for emp in employees:
        dept = emp["department"]

        if dept not in data:
            data[dept] = {
                "count": 0,
                "total": 0,
                "highest": emp["salary"],
                "top": emp["name"]
            }

        data[dept]["count"] += 1
        data[dept]["total"] += emp["salary"]

        if emp["salary"] > data[dept]["highest"]:
            data[dept]["highest"] = emp["salary"]
            data[dept]["top"] = emp["name"]

    result = {}

    for dept in sorted(data):
        count = data[dept]["count"]
        average = round(data[dept]["total"] / count, 2)
        top_name = data[dept]["top"]

        result[dept] = (count, average, top_name)

    return result


employees = [
    {"name": "Karan", "department": "Engineering", "salary": 74000},
    {"name": "Anas", "department": "Sales", "salary": 54000},
    {"name": "Arnold", "department": "IT", "salary": 30000},
    {"name": "Rehan", "department": "Engineering", "salary": 82000},
    {"name": "Tisha", "department": "Sales", "salary": 61000},
    {"name": "Saad", "department": "Engineering", "salary": 69000},
    {"name": "Khushi", "department": "IT", "salary": 7000}
]

print(department_summary(employees))
