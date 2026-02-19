# APCSP Project: Program for athlete's sepcificallly to help us and other wreslters

athlete_data = []
# Collect the user's' input so you can use it for later
weight = float(input("Enter your weight: "))
goal = input("Enter your goal (lose/gain/maintain): ")
hours_active = float(input("Enter your hours_active: "))
workouts = {
        "push": "Bench Press 3x10, Shoulder Press 3x10, Tricep Dips 3x12",
        "pull": "Pull Ups 3x10, Barbell Rows 3x10, Bicep Curls 3x12",
        "legs": "Squats 3x10, Lunges 3x12, Leg Press 3x10",
        "core": "Planks 3x60sec, Crunches 3x20, Leg Raises 3x15",
        "full body": "Squats 3x10, Bench Press 3x10, Pull Ups 3x10, Planks 3x60sec",
        "cardio": "Run 2 miles, Jump Rope 5 min, Sprints 10x40 yards"
    }

#This function asks how active you are based on hours active I created this because I can use this data in 2 other functions
def hours_active_level(hours):
    if hours < 2:
        return "inactive"
    elif hours < 3:
        return "active"
    else:
        return "very_active"
activity_level = hours_active_level(hours_active)
athlete_data.append({"Activity Level": activity_level})

#This function calculates your calorie needs based on weight, goal, and activity level 
def calorie_count(weight, goal, hours_active):
    activity_level = hours_active_level(hours_active)
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

result = calorie_count(weight, goal, hours_active)
print(f"Daily calories: {result}")

# Based on how active you are this will tell you how much you should be sleeping
def how_much_you_should_sleep(hours_active):
    if hours_active < 2:
        return "7-8 hours of sleep"
    elif hours_active < 3:
        return "8-9 hours of sleep"
    else:
        return "9-10 hours of sleep" 
result = how_much_you_should_sleep(hours_active)
print(f"Dailey sleep: {result}")

def want_to_know_how_much_water_to_drink(weight, hours_active):
    answer = input("Do you want to know how much water you should drink? (yes/no): ")
    if answer == "yes":
        return f"You should drink {weight * 0.5 + hours_active * 24} ounces of water daily."
    else:     
        return "It's important to drink water"
result = want_to_know_how_much_water_to_drink(weight, hours_active)
print(result)

def want_a_workout_plan():
    while True:
        already_has_plan = input("Does your school already have a workout plan for you? (yes/no): ")
        if already_has_plan == "yes":
            another = input("That's good, do you want me to create a workout plan? (yes/no): ")
            if another == "yes":
                workout_type = input("What type of workout do you want? (push/pull/legs/core/full body/cardio - enter ones you want separated by commas): ")
                selected = [w.strip() for w in workout_type.split(",")]
                plan = ""
                for w in selected:
                    if w in workouts:
                        plan += f"\n{w.upper()}: {workouts[w]}"
                    else:
                        plan += f"\n{w}: No plan found for this type"
                return f"Here is your workout plan on top of your school plan: {plan}"
            elif another == "no":
                return "Okay"
            else:
                print("Invalid input, please type yes or no.")
        elif already_has_plan == "no":
            want_plan = input("Do you want me to generate a workout plan for you? (yes/no): ")
            if want_plan == "yes":
                workout_type = input("What type of workout do you want? (push/pull/legs/core/full body/cardio - enter ones you want separated by commas): ")
                selected = [w.strip() for w in workout_type.split(",")]
                plan = ""
                for w in selected:
                    if w in workouts:
                        plan += f"\n{w.upper()}: {workouts[w]}"
                    else:
                        plan += f"\n{w}: No plan found for this type"
                return f"Here is your workout plan: {plan}"
            elif want_plan == "no":
                return "Okay, make sure you are staying active on your own!"
            else:
                print("Invalid input, please type yes or no.")
        else:
            print("Invalid input, please type yes or no.")

result = want_a_workout_plan()
print(result)
