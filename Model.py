from flask import Flask, request, jsonify, make_responde
import json

tasks = [
    {
        'id': 1,
        'name': "task1",
        "description": "This is task 1"
    },
    {   "id": 2,
        'name': "task1",
        "description": "This is task 2"
    },
    {
        'id': 3,
        'name': "task1",
        "description": "This is task 3"
    }
]

class Mode():
    def jsonReturn():
        return tasks
