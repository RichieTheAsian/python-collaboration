#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 12:25:29 2024

@author: richie
"""

class Task:
    def __init__(self, name):
        self.name = name
        self.is_completed = False

    def mark_completed(self):
        self.is_completed = True

    def __str__(self):
        return f"{self.name} - {'Completed' if self.is_completed else 'Pending'}"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, name):
        self.tasks.append(Task(name))
        print(f"Task '{name}' added.")
        
    def view_tasks(self):
        if not self.tasks:
            print("No tasks to show.")
            return
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")
    
    def mark_completed(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1].mark_completed()
            print(f"Task '{self.tasks[task_number - 1].name}' marked as completed.")
        else:
            print("Invalid task number.")

    def delete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Task '{removed_task.name}' deleted.")
        else:
            print("Invalid task number.")

def main():
    todo_list = ToDoList()

    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Mark a task as completed")
        print("4. Delete a task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task_name = input("Enter the name of the task: ")
            todo_list.add_task(task_name)

        elif choice == '2':
            todo_list.view_tasks()

        elif choice == '3':
            task_number = int(input("Enter the number of the task to mark as completed: "))
            todo_list.mark_completed(task_number)

        elif choice == '4':
            task_number = int(input("Enter the number of the task to delete: "))
            todo_list.delete_task(task_number)

        elif choice == '5':
            print("Exiting To-Do List App.")
            break

        else:
            print("Invalid choice, please try again.")
