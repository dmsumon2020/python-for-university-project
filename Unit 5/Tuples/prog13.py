def weekly_average(values):
    total = sum(values)
    average = total / len(values)
    return average


def check_goal(value, goal):
    if value >= goal:
        return True
    else:
        return False


steps = [8000, 6500, 7200]
calories = [450, 350, 500]
exercise_minutes = [35, 25, 40]

average_steps = weekly_average(steps)
average_calories = weekly_average(calories)
average_minutes = weekly_average(exercise_minutes)

steps_goal = check_goal(8000, 7000)
calories_goal = check_goal(450, 400)
exercise_goal = check_goal(35, 30)

print("Average steps:", average_steps)
print("Average calories:", average_calories)
print("Average exercise minutes:", average_minutes)

print("Steps goal met:", steps_goal)
print("Calories goal met:", calories_goal)
print("Exercise goal met:", exercise_goal)