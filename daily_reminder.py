# daily_reminder.py

def get_task_info():
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()
    return task, priority, time_bound

def generate_reminder(task, priority, time_bound):
    reminder = f"'{task}' is a {priority} priority task"
    
    match priority:
        case 'high':
            reminder += " that requires immediate attention!"
        case 'medium':
            reminder += ". Try to complete it soon."
        case 'low':
            reminder += ". Consider completing it when you have free time."
        case _:
            reminder += "."
    
    if time_bound == 'yes':
        reminder += " that requires immediate attention today!"
    
    return reminder

def main():
    task, priority, time_bound = get_task_info()
    reminder = generate_reminder(task, priority, time_bound)
    print(f"\nReminder: {reminder}")

if __name__ == "__main__":
    main()
