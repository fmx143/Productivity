# Day 2 of Moon Dev bootcamp, productivity app with visual alarm.

import time
import json
from datetime import datetime, timedelta
from termcolor import cprint
import random

# loading tasks from json file
def load_task():
    with open('C:\Users\loick\Visual Studio Code\tasks.json', 'r') as file:
        tasks = json.load(file)
    return tasks

