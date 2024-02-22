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
