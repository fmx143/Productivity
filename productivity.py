# Day 2 of Moon Dev bootcamp, productivity app with visual alarm.
import json 
import time 
from datetime import datetime, timedelta
from termcolor import cprint
import random
from config import file_path

# Function to load tasks from a JSON file
def load_tasks():
    with open(file_path, 'r') as f:
        tasks = json.load(f)
    return tasks 

# Function to generate a schedule with start and end times for each task
def get_taks_schedule(tasks):
    task_start_time = datetime.now()
    schedule = []
    for task, minutes in tasks.items():
        end_time = task_start_time + timedelta(minutes=minutes)
        schedule.append((task, task_start_time, end_time))
        task_start_time = end_time 
    return schedule 

# Main function to load tasks, generate a schedule, and monitor the current task
def main():
    tasks = load_tasks()
    schedule = get_taks_schedule(tasks)
    current_index = 0 

    # Continuously monitor the current task
    while True:
        now = datetime.now()
        current_task, start_time, end_time = schedule[current_index]
        remaining_time = end_time - now 
        remaining_minutes = int(remaining_time.total_seconds() // 60)

        print('')

        # Iterate over the schedule to display task statuses
        for index, (task, s_time, e_time) in enumerate(schedule):
            if index < current_index:
                # task is completed 
                print(f'{task} done: {e_time.strftime("%H:%M")}')
            elif index == current_index:
                # curent task 
                if remaining_minutes < 2:
                    cprint('{task} < 2m left!', 'white', 'on_red', attrs=['blink'])
                elif remaining_minutes < 5:
                    cprint(f'{task} - {remaining_minutes} mins', 'white', 'on_red')
                else:
                    cprint(f'{task} - {remaining_minutes} mins', 'white', 'on_blue')
            else:
                print(f'{task} @ {s_time.strftime("%H:%M")}')

        # List of motivational reminders
        list_of_reminders = [
            "i have a 1000 percent algo",
            "time is irrelevant, keep swimin",
            "every day i get better",
            "rest at the end",
            "jobs not finished", 
            "deal was already made",
            "best algo trader in the world",
        ]

        # Select a random reminder and print it
        random_reminder = random.choice(list_of_reminders)
        print('✨' + random_reminder)

        # Check if the current task is completed
        if now >= end_time:
            current_index += 1 
            if current_index >= len(schedule):
                cprint("all tasks are completed", 'white', 'on_green')
                break 

        # Sleep for 30 seconds before the next iteration
        time.sleep(30)

# Run the main function
main()
