# Workout Recommendation Program PYTHON

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

> This project was originally created as part of a college programming course and was one of my first Python programs.

## About the program

The Workout Recommendation Program helps users create a customized strength-training session based on their experience, selected muscle groups, and fitness goal.

The program asks the user for:

- Their name;
- Number of months of training experience;
- Muscle group or groups they want to train;
- Fitness goal: muscle growth, strength, or endurance.

It then determines the user's competency level and randomly selects an appropriate number of exercises from a library organized by muscle group. The final workout includes exercises, sets, repetitions, and rest periods.

## How It Works

The competency levels depends on the how much training experience does the user have:

| Competency level | Training experience | Number of exercises |
|---|---:|---:|
| Beginner | ≤ 12 months | 4 |
| Intermediate | 12–24 months | 6 |
| Advanced | ≥ 24 months | 8 |

The sets, repetitions, and rest periods depend on the user's fitness goal:

| Fitness goal | Sets | Repetitions | Rest |
|---|---:|---:|---:|
| Strength | 3 | 4 | 90 seconds |
| Endurance | 5 | 15 | 30 seconds |
| Muscle growth | 4 | 10 | 180 seconds |

## Example Scenarios

### Beginner

A user with 3 months of experience selects arms and strength as their goal. The program generates four unique arm exercises with the recommended sets, repetitions, and rest period for strength training.

### Intermediate

A user with 15 months of experience selects chest and legs with endurance as their goal. The program generates six exercises—three for the chest and three for the legs—with the recommendations for endurance training.

### Advanced

A user with 30 months of experience selects back and muscle growth as their goal. The program generates eight unique back exercises with the recommendations for muscle growth.

## Program Logic

The program:

1. Collects and validates the user's training experience.
2. Determines the user's competency level.
3. Collects and validates the selected muscle groups.
4. Collects and validates the fitness goal.
5. Divides the exercises among the selected muscle groups.
6. Randomly selects unique exercises.
7. Retrieves the appropriate sets, repetitions, and rest time.
8. Displays the customized workout.

## Python Concepts Demonstrated

- Functions
- Conditional statements
- Lists and dictionaries
- Loops
- User input and input validation
- Random selection
- String manipulation

## Example Output

<img width="712" height="360" alt="image" src="https://github.com/user-attachments/assets/bc2c07bb-3a77-4bd0-b11a-d7282939208a" />
