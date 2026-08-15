# Importing the random module needed for the random() function
import random

# Define exercise lists for each muscle group
chest_exercises = ["Bench Press", "Incline Dumbbell Press", "Chest Fly", "Push-ups", "Cable Crossover",
                   "Dumbbell Pull-over", "Dip", "Decline Press"]
arms_exercises = ["Bicep Curl", "Triceps Dip", "Side Lateral Raise", "Triceps Dumbbell Kickback", "Triceps Pushdown",
                  "Overhead Triceps Extension", "Reverse Fly", "High Plank"]
legs_exercises = ["Romanian Deadlift", "Squat", "Calf Raises", "Lunge", "Leg Press", "Leg Extension", "Split Squat",
                  "Good Morning"]
back_exercises = ["Barbell Deadlift", "Single-arm dumbbell row", "Pull-up", "Lat Pull-Down",
                  "Roman Chair Back Extension", "Seated Cable Row", "Cable Reverse Fly", "Wide dumbbell bent-over row"]

# This dictionary maps muscle groups to exercise lists.
EXERCISE_GROUPS = {
    "chest": chest_exercises,
    "arms": arms_exercises,
    "legs": legs_exercises,
    "back": back_exercises
}

# This dictionary maps the sets, reps and rest time for each goal.
GOALS = {
    "muscle": {"sets": 4, "reps": 10, "rest": 180},
    "strength": {"sets": 3, "reps": 4, "rest": 90},
    "endurance": {"sets": 5, "reps": 15, "rest": 30}
}

# This function is created to get the training length from the user and validate input
def get_training_length():
    while True: # Loop until valid input is provided
        try:
            # Ask user to input training duration in months and convert it to an integer
            months_training = int(input("How long have you been training? (in months, number only) "))
            if months_training >= 0: # Ensure positive input
                return months_training # Exit loop with valid input
            else:
                print("Please enter a positive number.") # Error message for negative numbers
        except ValueError:
            print("Invalid input. Please enter a number only.") # Error message for non-numeric input

# This function is created to determine the competency level of the user and
# set the number of exercises based on the competency level.
def get_competency_level(months):
    # Use conditionals to categorize user into a competency levels
    if months <= 12:
        return "beginner", 4
    elif 12 < months <= 24:
        return "intermediate", 6
    else:
        return "advanced", 8

# This function is created to get muscle groups from user and validate input.
def get_muscle_groups():
    while True: # Loop until valid input is provided
        # Ask user to input the muscle group and convert it to a string.
        muscle_input = str(input("Which muscle groups do you want to train today? (chest, arms, legs, back) \n"
                                 "Separate by comma for multiple muscle groups. "))
        # Take the user input, split it into a list, trim spaces, and convert each entry to lowercase.
        groups = [item.strip().lower() for item in muscle_input.split(',')]
        # Check for validity: Ensure all input groups are in EXERCISE_GROUPS
        if all(items in EXERCISE_GROUPS for items in groups):
            return groups
        else:
            print("Invalid input. Please enter valid muscle groups separated by commas. ")

# This function is created to get the user's fitness goal and validate input.
def get_fitness_goal():
    while True: # Loop until valid input is provided
        # Ask user to input their goal, then trim spaces, and convert it to lowercase.
        goal = input("What is your goal? (muscle, strength, endurance) \n"
                     "If your goal is to gain muscle mass, please type MUSCLE.\n"
                     "If your goal is to become stronger, please type STRENGTH.\n"
                     "If your goal is to improve your endurance, please type ENDURANCE. ").strip().lower()
        if goal in GOALS: # Check if input is valid
            return goal
        else:
            print("Invalid input. Please enter a valid goal.")


# This is where the main program starts
# Brief introduction
print("This program is designed to help you with your workout routine.")
# Ask the user its name and greet user
name = input("Can I please have your name? ").strip().capitalize()
print(f"Hello, {name}. I will ask you a few important questions to determine your workout for today. \n"
      f"Please pay attention to what the question asks. ")

# Gather user inputs by calling the defined functions
length_training = get_training_length()
competency_level, num_exercises = get_competency_level(length_training)
muscle_groups = get_muscle_groups()
fitness_goal = get_fitness_goal()

# Calculate exercises per group to ensure that the workout includes each muscle group
exercises_per_group = num_exercises // len(muscle_groups)
remaining_exercises = num_exercises % len(muscle_groups)

# Collect exercises, ensuring each muscle group is present
selected_exercises = []
for group in muscle_groups:
    group_exercises = random.sample(EXERCISE_GROUPS[group], exercises_per_group)
    selected_exercises.extend(group_exercises)

# Add remaining exercises randomly from selected groups to match num_exercises exactly
if remaining_exercises > 0:
    extra_exercises = random.sample(
        [exercise for group in muscle_groups for exercise in EXERCISE_GROUPS[group] if
            exercise not in selected_exercises],
        remaining_exercises
    )
    selected_exercises.extend(extra_exercises)

# Get sets, reps, and rest based on the fitness goal
sets = GOALS[fitness_goal]["sets"]
reps = GOALS[fitness_goal]["reps"]
rest = GOALS[fitness_goal]["rest"]

# Print the workout routine
print(f"\n{name}, here is your workout routine:")
for exercise in selected_exercises:
    print(f"  - {exercise}")
print(
    f"\nAccording to your goal, perform {sets} sets of {reps} reps for each exercise,"
    f" resting {rest} seconds between sets.")

print("\nHave a great workout!")