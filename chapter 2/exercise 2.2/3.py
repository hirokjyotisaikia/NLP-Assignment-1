# Q. If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?

from datetime import datetime, timedelta

# Define running speeds and distances
easy_pace_minutes_per_mile = 8.25
tempo_pace_minutes_per_mile = 7.2

easy_distance = 1  # miles
tempo_distance = 3  # miles

# Calculate total running time in minutes
total_running_time = (easy_distance * easy_pace_minutes_per_mile) + (tempo_distance * tempo_pace_minutes_per_mile) + (easy_distance * easy_pace_minutes_per_mile)

# Convert minutes to hours and minutes
hours = int(total_running_time // 60)
minutes = int(total_running_time % 60)

# Set start time as 6:52 am
start_time = "06:52:00"

# Add running time to start time
start_time_obj = datetime.strptime(start_time, "%H:%M:%S")
arrival_time_obj = start_time_obj + timedelta(minutes=total_running_time)

# Format arrival time as string
arrival_time = arrival_time_obj.strftime("%H:%M:%S")

# Print arrival time
print("You will arrive home for breakfast at:", arrival_time)

# Output: You will arrive home for breakfast at : 07:30:06