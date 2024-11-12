import requests

username = 'sarah_jones'  # Add your username
password = 'Sarah@12345'  # Add your password
base_url = 'http://127.0.0.1:8000/api/'

# Retrieve all courses
r = requests.get(f'{base_url}courses/')
courses = r.json()

# List available courses
available_courses = ', '.join([course['title'] for course in courses])
print(f'Available courses: {available_courses}')

# Enroll in each course
for course in courses:
    course_id = course['id']
    course_title = course['title']
    
    r = requests.post(
        f'{base_url}courses/{course_id}/enroll/',
        auth=(username, password)
    )
    
    if r.status_code == 200:
        # Successful request
        print(f'Successfully enrolled in {course_title}')
    else:
        print(f'Failed to enroll in {course_title}')
