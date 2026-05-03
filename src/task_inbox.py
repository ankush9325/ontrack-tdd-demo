def get_student_tasks(student_id):
    """
    Returns a list of tasks for a given student.
    
    Args:
        student_id (str): The student's ID
        
    Returns:
        list: List of task dictionaries, or empty list if student not found
    """
    # Mock data for testing
    mock_data = {
        "S12345": [
            {"id": 1, "name": "Task 1", "status": "Submitted", "due_date": "2025-05-10"},
            {"id": 2, "name": "Task 2", "status": "Not Submitted", "due_date": "2025-05-17"}
        ]
    }
    
    # Return empty list for invalid input
    if not student_id or student_id == "":
        return []
    
    return mock_data.get(student_id, [])
