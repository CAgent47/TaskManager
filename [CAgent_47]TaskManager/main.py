import os
import datetime
import json

class Tasks:
    def __init__(self, task):
        self.task = task
        self.time = datetime.datetime.now()

    def to_doc(self):
        return {
            "Task": self.task,
            "Time": self.time.isoformat()
        }

configuration = 'config.json'

def read_json():
    if os.path.exists(configuration):
        with open(configuration, 'r') as conf:
            try:
                data = json.load(conf)
                if isinstance(data, list):
                    return data
                else:
                    return []
            except json.JSONDecodeError:
                return []
    else:
        with open(configuration, 'w') as createnew:
            json.dump([], createnew)
        return []

def save_Task(tasks):
    with open(configuration, 'w') as wconf:
        json.dump(tasks, wconf, indent=4)

def showTasks(task_list):
    if not task_list:
        print("No tasks found.")
        return
    for index, tasksInList in enumerate(task_list, 1):
        print(f'{index}: {tasksInList["Task"]} ({tasksInList["Time"]})')

def deleteAllTask():
    if os.path.exists(configuration):
        result = input('Are you sure you want to delete ALL tasks? (y/n): ')
        if result.lower() == 'y':
            with open(configuration, 'w') as f:
                json.dump([], f, indent=4)
            print("All tasks deleted.")
            return True
        else:
            print("Deletion cancelled.")
            return False
    return False

def main():
    task_list = read_json()
    MAXIMUM = 100

    new_Task = input('Enter your task: ')

    if not new_Task.strip():
        print("Invalid value. Task cannot be empty.")
        exit(1)

    if len(task_list) >= MAXIMUM:
        print("ERROR: Maximum tasks reached!")
        if deleteAllTask():
            task_list = []
        else:
            exit(0)
    else:
        mmber_task = Tasks(new_Task)
        task_list.append(mmber_task.to_doc())
        save_Task(task_list)
        print("Task saved successfully!")
        
        show = input('Do you want to show tasks? (y/n): ')
        if show.lower() == 'y':
            showTasks(task_list)
        else:
            print("Exiting...")

if __name__ == '__main__':
    main()
