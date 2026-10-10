def weekly_average(steps, calories, exercise_minutes):
    average_steps = sum(steps) / len(steps)
    average_calories = sum(calories) / len(calories)
    average_minutes = sum(exercise_minutes) / len(exercise_minutes)
    return average_steps, average_calories, average_minutes


def check_goals(
    steps,
    calories,
    exercise_minutes,
    step_goal=7000,
    calorie_goal=400,
    exercise_goal=30,
):
    return (
        steps >= step_goal,
        calories >= calorie_goal,
        exercise_minutes >= exercise_goal,
    )


steps = [8000, 6500, 7200]
calories = [450, 350, 500]
exercise_minutes = [35, 25, 40]

averages = weekly_average(steps, calories, exercise_minutes)
goals = check_goals(8000, 450, 35)

print("Weekly averages:", averages)
print("Goals met:", goals)