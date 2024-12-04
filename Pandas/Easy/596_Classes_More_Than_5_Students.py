"""

Question: Classes more than 5 students

Summary: Write a function that identifies all the classes that have at least five students. 
You can return the result in any order.

Method: Group the 'courses' DataFrame by 'class' and count the number of students in each class. 
Filter the grouped result to include only classes with at least five students.

Time complexity: O(n)
Space complexity: O(n)
"""

import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    # Group by 'class' and count the number of students in each class
    student_count = courses.groupby("class")["student"].count().reset_index()
    # Filter the classes that have at least five students
    filt = student_count[student_count["student"] >= 5][["class"]]
    return filt


# Example usage
courses_data = {
    'student': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
    'class': ['Math', 'English', 'Math', 'Biology', 'Math', 'Computer', 'Math', 'Math', 'Math']
}
courses = pd.DataFrame(courses_data)

result = find_classes(courses)
print(result)
