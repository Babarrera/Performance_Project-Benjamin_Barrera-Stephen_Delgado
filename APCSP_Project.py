athlete_data = []
activity_levels = ["inactive", "active", "very_active"]

weight = float(input("Enter your weight: "))
goal = input("Enter your goal (lose/gain/maintain): ")
hours_active = float(input("Enter your hours_active: "))

def calories(weight, goal, hours_active):
    # clearer thresholds: <2 inactive, 2-<3 active, >=3 very_active
    if hours_active < 2:
        activity_level = "inactive"
    elif hours_active < 3:
        activity_level = "active"
    else:
        activity_level = "very_active"

    if goal == "lose":
        if activity_level == "inactive":
            cal = weight * 13 - 500
        elif activity_level == "active":
            cal = weight * 15 - 500
        else:
            cal = weight * 18 - 500
    elif goal == "gain":
        if activity_level == "inactive":
            cal = weight * 13 + 500
        elif activity_level == "active":
            cal = weight * 15 + 500
        else:
            cal = weight * 18 + 500
    else:  # maintain or unexpected
        if activity_level == "inactive":
            cal = weight * 13
        elif activity_level == "active":
            cal = weight * 15
        else:
            cal = weight * 18

    return cal

result = calories(weight, goal, hours_active)
print(f"Daily calorie recommendation: {result}")
