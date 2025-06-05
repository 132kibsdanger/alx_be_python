task = input("Enter your task: ")
priority = input("Enter the task priority (high/medium/low): ")
time_bound  = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        if time_bound == "yes":
            print(f"{task} is a high priority task that requires immediate attention today.")
        else:
            print(f"{task} is a high priority task that should be completed as soon as possible.")

    case "medium":
        if time_bound == "yes":
            print(f"{task} is a medium priority task that needs to be completed before the deadline.")
        else:
            print(f"{task} is a medium priority task that should be completed soon.")

    case "low":
        if time_bound == "yes":
            print(f"{task} is a low priority task that can be completed before the deadline.")
        else:
            print(f"{task} is a low priority task. Consider completing it when you have free time.")

    case _:
        print("Invalid priority level. Please enter high, medium, or low.")
print("Thank you for using the daily reminder system.")
print("Have a productive day!")
