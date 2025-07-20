while True:
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ")
    time_bound = input("Is it time-bound? (yes/no): ")

    match priority:
        case 'high':
            if time_bound == 'yes':
                print(f"'{task}' is a high priority task that requires your immediate attention today!")
            else:
                print(f"'{task}' is important, but you can handle it when you're less busy")

        case 'medium':
            if time_bound == 'yes':
                print(f"'{task}' is a medium priority task. Try to complete it before the day ends")
            else:
                print(f"'{task}' is a moderate task. Plan to do it soon, but it's not urgent")

        case 'low':
            if time_bound == 'yes':
                print(f"'{task}' is a low priority task, but don't forget - it needs to be done today.")
            else:
                print(f"'{task}' can wait. Consider doing it when you have spare time")


    again = input("Do you want to enter another task? (yes/no): ")
    if again != 'yes':
            break