# APCSP Project: Program for athlete's sepcificallly to help us and other wreslters

athlete_data = []
# Collect the user's' input so you can use it for later
weight = float(input("Enter your weight: "))
goal = input("Enter your goal (lose/gain/maintain): ")
hours_active = float(input("Enter your hours_active: "))

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
        weight * 0.5 + hours_active * 24
        return f"You should drink {weight * 0.5 + hours_active * 24} ounces of water daily."
    else:     
        return "It's important to stay hydrated"
result = want_to_know_how_much_water_to_drink(weight, hours_active)
print(result)

def want_a_workout_plan(answer):
    answer = input("Your school already has a workout plan(true/false): ")
    if answer == "true":
        return "That's good I can still generate a workout for you"
    else:
        answer = input("Do you want me to generate a workout plan for you? (yes/no): ")
        if answer == "yes":
            return "Good do you want a workout plan for Push, Pull, Legs, core, full body, cardio? (enter the ones you want separated by commas): "
