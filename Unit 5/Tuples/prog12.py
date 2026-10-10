def calculate_weekly_averages(total_steps, total_calories, total_minutes, days=7):
    """Calculates the daily average for steps, calories, and exercise minutes."""
    avg_steps = total_steps / days
    avg_calories = total_calories / days
    avg_minutes = total_minutes / days
    return avg_steps, avg_calories, avg_minutes

def check_daily_goal(steps, target_steps=10000):
    """Determines if the daily step goal was met."""
    if steps >= target_steps:
        return "Goal Met! Great job."
    else:
        return "Goal Not Met. Keep pushing!"

# Example usage of the custom functions
weekly_steps_total = 73500
weekly_calories_total = 17500
weekly_minutes_total = 210

avg_s, avg_c, avg_m = calculate_weekly_averages(weekly_steps_total, weekly_calories_total, weekly_minutes_total)
print(f"Daily Averages - Steps: {avg_s}, Calories: {avg_c}, Minutes: {avg_m}")

status = check_daily_goal(11200)
print(status)