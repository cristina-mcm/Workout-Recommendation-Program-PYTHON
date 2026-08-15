# Workout Recommendation Program PYTHON

> This project was originally created as part of a college programming course and was one of my first Python programs.

## About the program

Whether new to strength training or a seasoned pro, everyone can experience the desire to switch up their training routine. The problem to solve is to help them in saving time by suggesting exercises for a workout session tailored to their preferred muscle group. I will create a program that will output a list of exercises, including the number of sets, repetitions and rest between sets.

When executed, the program will first ask the user a few questions related to their level of competence, the muscle group they want to train and their goal: gaining muscles, improving strength or improving endurance.

Next, based on the responses the program will randomize the exercise names from a library of exercise that are sorted according to the muscle group they belong to. The number of exercises the program will display will depend on the number of months they train. The program will determine the user's competency level by analyzing their answers to the questions, then suggest the ideal number of exercises along with the recommended sets, reps, and rest time.
Thus, the program will display a set number of exercises, sets, reps, and rest time customized for the user.

## Scenarios

#### Scenario 1: A person that has been training for 3 months wants to train their arms, and their goal is to become stronger.
1.	Input: 3 months of training, arms muscle group, goal: strength.
2.	Based on their training length, the program will set the competency level to beginner and the number of exercises to 4. As the user is interested in training their arms, a list will be generated containing 4 unique arm exercises chosen from a selection of arm exercises. Based on their goal: strength, the program will retrieve the required sets, rep and rest. 
3.	Output: a list of 4 exercises for the arms muscle group, the recommended sets for strength:3, repetitions:4, rest:90 seconds 

#### Scenario 2: A person that has been training for 15 months wants to train their chest and legs, and their goal is to improve endurance.
1.	Input: 15 months of training, chest and legs muscle groups, goal: endurance.
2.	Based on their training length it will set the competency level to intermediate and the number of exercises to 6. As the user is interested in training their chest and legs, a list will be generated containing 6 unique exercises from a selection of chest and legs exercises. The program will also ensure that the user gets 3 chest exercises and 3 legs exercises. Based on their goal: endurance, the program will retrieve the required sets, rep and rest.
3.	Output: a list of 6 exercises total:3 for the chest muscle group and 3 for legs muscle group, , the recommended sets for endurance:5, repetitions:15, rest:30 seconds

#### Scenario 3: A person that has been training for 30 months wants to train their back, and their goal is to gain muscle mass.
1.	Input: 30 months of training, back muscle group, goal: muscle.
2.	Based on their training length, the program will set the competency level to advanced and the number of exercises to 8. As the user is interested in training their back, a list will be generated containing 8 unique back exercises chosen from a selection of back exercises. Based on their goal: muscle, the program will retrieve the required sets, rep and rest.
3.	Output: a list of 8 exercises for the back muscle group, the recommended sets for muscle:4, repetitions:10, rest:180 seconds 

## Pseudocode
chest_exercises = list of 8 chest exercises.\
arms_exercises = list of 8 arm exercises.\
legs_exercises = list of 8 leg exercises.\
back_exercises = list of 8 back exercises.\
EXERCISE_GROUPS = dictionary mapping the muscle groups to their corresponding exercise list.

GOALS = dictionary mapping the sets, repetitions, and rest time to each fitness goal

**Function get_competency_level(months):**\
Ask user to input training duration in months\
Store the answer in length_training\
If the training length is less than 12 months\
Set the competency_level to beginner and num_exercises to 4\
Else If the training length is between 12 and 24 months\
Set the competency_level to intermediate and num_exercises to 6\
Else\
Set the competency_level to advanced and num_exercises to 6\
Return the competency_level and num_exercises

**Function get_muscle_group()** \
Ask user to input the muscle group they want to train today\
Store the answer in muscle_input\
groups = transforms the user’s answer into a list of the muscle groups\
Check that the muscle groups are valid\
If all muscle groups in the groups list are in in exercise_groups\
Return groups\
Else\
Prompt the input again

**Function get_fitness_goal()**\
Ask user to input their fitness goal\
Store the answer in training_goal\
If the training_goal is in the GOALS\
Return the fitness goal\
Else\
Prompt the input again

**Main program**\
Ask for the user’s name and greet them.\
Call get_competency_level() to ask for months of training\
Get competency level\
Get num_exercises\
Call get_muscle_groups()\
Get the selected muscle groups\
Call get_fitness_goal()\
Get the user’s fitness goal\
Calculate exercises per group by dividing num_exercises to len(muscle_groups)\
Create an empty list selected_exercises\
Add exercises to the selected_exercises ensuring that each group is represented\
Retrieve the sets, reps and rest from the GOALS dictionary\
Use the print() function to display the selected_exercises list\
Use the print() function to display the sets, reps and rest related to the fitness goal of the user\
Print a final message

## Output

<img width="712" height="360" alt="image" src="https://github.com/user-attachments/assets/bc2c07bb-3a77-4bd0-b11a-d7282939208a" />

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
