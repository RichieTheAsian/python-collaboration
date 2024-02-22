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
