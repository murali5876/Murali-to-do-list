from datetime import datetime
import calendar
from colorama import Fore, Style, init

# Initialize colorama
init()

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task, due_date=None, description=None):
        if due_date:
            try:
                due_date = datetime.strptime(due_date, "%Y%m%d").strftime("%Y-%m-%d")
            except ValueError:
                print(Fore.RED + '\nInvalid date format. Please enter a valid date (YYYYMMDD).' + Style.RESET_ALL)
                return

        self.tasks.append({'task': task, 'completed': False, 'due_date': due_date, 'description': description})
        print(Fore.GREEN + f'\nTask "{task}" added to the to-do list.' + Style.RESET_ALL)

    def view_tasks(self):
        if not self.tasks:
            print(Fore.YELLOW + '\nNo tasks in the to-do list.' + Style.RESET_ALL)
        else:
            print(Fore.CYAN + '\nTo-Do List:\n' + Style.RESET_ALL)
            for index, task_info in enumerate(self.tasks, start=1):
                status = 'Completed' if task_info['completed'] else 'Not Completed'
                due_date = f'Due Date: {task_info["due_date"]}' if task_info['due_date'] else 'No Due Date'
                description = f'Description: {task_info["description"]}' if task_info['description'] else 'No Description'
                print(Fore.WHITE + f'{index}. {task_info["task"]} - {status} - {due_date} - {description}' + Style.RESET_ALL)
            print()  # Add an empty line after displaying tasks

    def remove_task(self, task_index):
        try:
            task_index = int(task_index)
            if 1 <= task_index <= len(self.tasks):
                removed_task = self.tasks.pop(task_index - 1)
                print(Fore.GREEN + f'\nTask "{removed_task["task"]}" removed from the to-do list.' + Style.RESET_ALL)
            else:
                print(Fore.RED + 'Invalid task index.' + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + '\nInvalid input. Please enter a valid task index.' + Style.RESET_ALL)

    def complete_task(self, task_index):
        try:
            task_index = int(task_index)
            if 1 <= task_index <= len(self.tasks):
                self.tasks[task_index - 1]['completed'] = True
                print(Fore.GREEN + f'\nTask marked as completed.' + Style.RESET_ALL)
            else:
                print(Fore.RED + 'Invalid task index.' + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + '\nInvalid input. Please enter a valid task index.' + Style.RESET_ALL)

    def update_task(self, task_index, new_task):
        try:
            task_index = int(task_index)
            if 1 <= task_index <= len(self.tasks):
                update_due_date = colored_input('Do you want to update the due date? (yes/no): ', Fore.YELLOW).lower() == 'yes'

                if update_due_date:
                    due_date, description = get_calendar_input()
                    self.tasks[task_index - 1]['due_date'] = due_date
                    self.tasks[task_index - 1]['description'] = description
                else:
                    self.tasks[task_index - 1]['task'] = new_task

                print('Task updated.')
            else:
                print('Invalid task index.')
        except ValueError:
            print('Invalid input. Please enter a valid task index.')

def get_calendar_input():
    present_date = datetime.now()
    print(Fore.CYAN + f'\nPresent Date: {present_date.strftime("%Y-%m-%d")}' + Style.RESET_ALL)

    year = int(colored_input(Fore.YELLOW + 'Enter the year: ' + Style.RESET_ALL))
    month = int(colored_input(Fore.YELLOW + 'Enter the month (1-12): ' + Style.RESET_ALL))

    cal = calendar.monthcalendar(year, month)
    print(Fore.CYAN + '\nCalendar:' + Style.RESET_ALL)
    print(Fore.CYAN + ' Mo Tu We Th Fr Sa Su' + Style.RESET_ALL)
    for week in cal:
        week_str = ''
        for d in week:
            if d == 0:
                week_str += '   '
            else:
                week_str += f'{d:2} '
        print(week_str)

    while True:
        day = colored_input(Fore.YELLOW + 'Enter the day (or "m" to change month, "y" to change year): ' + Style.RESET_ALL)
        if day.lower() == 'm':
            month = int(colored_input(Fore.YELLOW + 'Enter the new month (1-12): ' + Style.RESET_ALL))
            cal = calendar.monthcalendar(year, month)
            print(Fore.CYAN + '\nCalendar:' + Style.RESET_ALL)
            print(Fore.CYAN + ' Mo Tu We Th Fr Sa Su' + Style.RESET_ALL)
            for week in cal:
                week_str = ''
                for d in week:
                    if d == 0:
                        week_str += '   '
                    else:
                        week_str += f'{d:2} '
                print(week_str)
        elif day.lower() == 'y':
            year = int(colored_input(Fore.YELLOW + 'Enter the new year: ' + Style.RESET_ALL))
            cal = calendar.monthcalendar(year, month)
            print(Fore.CYAN + '\nCalendar:' + Style.RESET_ALL)
            print(Fore.CYAN + ' Mo Tu We Th Fr Sa Su' + Style.RESET_ALL)
            for week in cal:
                week_str = ''
                for d in week:
                    if d == 0:
                        week_str += '   '
                    else:
                        week_str += f'{d:2} '
                print(week_str)
        else:
            try:
                day = int(day)
                if 1 <= day <= 31:
                    description = colored_input(Fore.YELLOW + 'Enter task description: ' + Style.RESET_ALL)
                    return f'{year:04}{month:02}{day:02}', description
                else:
                    print(Fore.RED + 'Invalid day. Please enter a number between 1 and 31.' + Style.RESET_ALL)
            except ValueError:
                print(Fore.RED + 'Invalid input. Please enter a valid day or choose "m" or "y".' + Style.RESET_ALL)

def colored_input(prompt, color=Fore.WHITE):
    user_input = input(color + prompt + Style.RESET_ALL)
    return user_input

def welcome_message():
    print(Fore.GREEN + f"Welcome, to Murali To-Do List App." + Style.RESET_ALL)
    print(Fore.GREEN + "Press Enter to continue..." + Style.RESET_ALL)
    input()

def main():
    welcome_message()
    todo_list = TodoList()

    while True:
        print(Fore.CYAN + '\nSELECT YOUR OPTION:' + Style.RESET_ALL)
        print(Fore.CYAN + '1. Add Task' + Style.RESET_ALL)
        print(Fore.CYAN + '2. View Tasks' + Style.RESET_ALL)
        print(Fore.CYAN + '3. Remove Task' + Style.RESET_ALL)
        print(Fore.CYAN + '4. Mark Task as Completed' + Style.RESET_ALL)
        print(Fore.CYAN + '5. Update Task' + Style.RESET_ALL)
        print(Fore.CYAN + '6. Exit' + Style.RESET_ALL)

        choice = colored_input('Enter your choice (1-6): ', Fore.YELLOW)

        if choice == '1':
            task = colored_input('Enter the task name: ', Fore.YELLOW)
            print(Fore.CYAN + f'Using the calendar for due date (current month: {datetime.now().strftime("%B %Y")})' + Style.RESET_ALL)
            due_date, description = get_calendar_input()
            todo_list.add_task(task, due_date, description)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            task_index = colored_input('Enter the task index to remove: ', Fore.YELLOW)
            todo_list.remove_task(task_index)
        elif choice == '4':
            task_index = colored_input('Enter the task index to mark as completed: ', Fore.YELLOW)
            todo_list.complete_task(task_index)
        elif choice == '5':
            task_index = colored_input('Enter the task index to update: ', Fore.YELLOW)
            new_task = colored_input('Enter the new task name to update: ', Fore.YELLOW)
            todo_list.update_task(task_index, new_task)
        elif choice == '6':
            print(Fore.BLUE + f'Exiting the Murali To-Do List App. Thank you for using it!' + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + 'Invalid choice. Please enter a number between 1 and 6.' + Style.RESET_ALL)

if __name__ == '__main__':
    main()
