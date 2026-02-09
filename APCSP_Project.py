 #list: stores athletes profile data
athlete_data = []
# Student Developed Procedure
def calulate_calories(weight, goal, activity_level):
    """
    Calculates daily calorie needs based on weight, goal, and activity level.
    
    Parameters:
        weight (float): Current weight in pounds
        goal (str): Weight goal - "maintain", "gain", or "lose"
        activity_level (str): Activity level - "low", "moderate", or "high"
    
    Returns:
        int: Recommended daily calories
    """
# Base  metabolic rate caluclation
base_calories = weight * 12

# Selection: Adjust nased on activiety level\
if activity_level == "low":
    calories = base_calories * 1.2
elif activity_level == "moderate":
    calories = base_calories * 1.5
else: # High activity level
    calories = base_calories * 1.8

# Selection: Adjust Based on goal 
if goal == "lose"
calories = calories - 500
elif goal == "gain":
    calories = calories + 500
    # if maintain, no change needed

    return int(calories)

    #student-developed procedure with parameter
    def calculate_sleep(training_hours):
        """
        Calculates recommended sleep hours based on training intensity
        
        Parameters:
            training_hours (float): Hours of training per day
        
        Returns:
            float: Recommended sleep hours
        """
        base_sleep = 7.0

        # Selection: Adjust sleep based on training hours
        if training_hours > 2:
            sleep_hours += 2
        elif training_hours > 1:
            sleep_hours += 1

        return sleep_hours
