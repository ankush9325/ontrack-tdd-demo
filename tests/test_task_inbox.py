import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.task_inbox import get_student_tasks

class TestTaskInbox(unittest.TestCase):
    
    def test_valid_student_returns_tasks(self):
        student_id = "S12345"
        tasks = get_student_tasks(student_id)
        # INTENTIONAL FAILURE - expecting wrong number
        self.assertEqual(len(tasks), 999)  # This will FAIL!
    
    def test_invalid_student_returns_empty_list(self):
        tasks = get_student_tasks("INVALID_ID")
        self.assertEqual(tasks, [])
    
    def test_empty_string_returns_empty_list(self):
        tasks = get_student_tasks("")
        self.assertEqual(tasks, [])
