# User Story: Student Task Inbox

## As a student
I need a function that shows me all my submitted tasks in one place.

## Why
Currently, students must click through multiple pages to find submission status. 
This wastes time and causes missed deadlines.

## How it should behave
- Given a valid student ID, return a list of tasks with their submission status
- Show tasks even if no submission exists (status: "Not Submitted")
- Return an empty list if student ID doesn't exist
- Each task includes: ID, name, submission status, due date

## Example
Input: student_id = "S12345"
Output: [
    {"id": 1, "name": "Task 1", "status": "Submitted", "due_date": "2025-05-10"},
    {"id": 2, "name": "Task 2", "status": "Not Submitted", "due_date": "2025-05-17"}
]
