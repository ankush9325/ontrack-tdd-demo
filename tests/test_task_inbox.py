import unittest
import sys
import os

# Add the src directory to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.task_inbox import get_student_tasks

class TestTaskInbox(unittest.TestCase):
    
    def test_valid_student_returns_tasks(self):
        """Test that a valid student ID returns the expected number of tasks"""
        student_id = "S12345"
        tasks = get_student_tasks(student_id)
        
        # We expect 2 tasks for this student
        self.assertEqual(len(tasks), 2)
        
        # Check first task has required fields
        first_task = tasks[0]
        self.assertIn("id", first_task)
        self.assertIn("name", first_task)
        self.assertIn("status", first_task)
        self.assertIn("due_date", first_task)
    
    def test_invalid_student_returns_empty_list(self):
        """Test that invalid student ID returns empty list"""
        tasks = get_student_tasks("INVALID_ID")
        self.assertEqual(tasks, [])
    
    def test_empty_string_returns_empty_list(self):
        """Test that empty string returns empty list"""
        tasks = get_student_tasks("")
        self.assertEqual(tasks, [])
