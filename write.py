# Django specific settings
import os
from datetime import date
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from crud.models import *

# Your code starts from here:

def write_instructors():
    # Add instructors
    user_john = User(first_name='John', last_name='Doe', dob=date(1962, 7, 16), email='john.doe1@gmail.com')
    user_john.save()
    instructor_john = Instructor(user_ptr=user_john, full_time=True, total_learners=30050)
    instructor_john.save()

    instructor_yan = Instructor(first_name='Yan', last_name='Luo', dob=date(1962, 7, 16), full_time=True, total_learners=30050, email='yan.luo@gmail.com')
    instructor_yan.save()

    instructor_joy = Instructor(first_name='Joy', last_name='Li', dob=date(1992, 1, 2), full_time=False, total_learners=10040, email='joy.li@gmail.com')
    instructor_joy.save()

    instructor_peter = Instructor(first_name='Peter', last_name='Chen', dob=date(1982, 5, 2), full_time=True, total_learners=2002, email='peter.chen@gmail.com')
    instructor_peter.save()

    print("Instructor objects all saved... ")

def write_courses():
    # Add Courses
    course_cloud_app = Course(name="Cloud Application Development with Database",
                              description="Develop and deploy application on cloud")
    course_cloud_app.save()

    course_python = Course(name="Introduction to Python",
                           description="Learn core concepts of Python and obtain hands-on "
                                       "experience via a capstone project")
    course_python.save()

    print("Course objects all saved... ")

def write_lessons():
    # Add lessons
    lesson1 = Lesson(title='Lesson 1', content="Object-relational mapping project")
    lesson1.save()

    lesson2 = Lesson(title='Lesson 2', content="Django full stack project")
    lesson2.save()

    print("Lesson objects all saved... ")

def write_learners():
    # Add Learners
    learner_james = Learner(first_name='James', last_name='Smith', dob=date(1982, 7, 16),
                            occupation='data_scientist',
                            social_link='https://www.linkedin.com/james/')
    learner_james.save()
    learner_mary = Learner(first_name='Mary', last_name='Smith', dob=date(1991, 6, 12), occupation='dba',
                           social_link='https://www.facebook.com/mary/')
    learner_mary.save()
    learner_robert = Learner(first_name='Robert', last_name='Lee', dob=date(1999, 1, 2), occupation='student',
                             social_link='https://www.facebook.com/robert/')
    learner_robert.save()
    learner_david = Learner(first_name='David', last_name='Smith', dob=date(1983, 7, 16),
                            occupation='developer',
                            social_link='https://www.linkedin.com/david/')
    learner_david.save()
    learner_john = Learner(first_name='John', last_name='Smith', dob=date(1986, 3, 16),
                           occupation='developer',
                           social_link='https://www.linkedin.com/john/')
    learner_john.save()
    print("Learner objects all saved... ")
    #<HINT> Add more learners objects#
    #...

def clean_data():
    # Delete all data to start from fresh
    Enrollment.objects.all().delete()
    Lesson.objects.all().delete()
    Course.objects.all().delete()
    Instructor.objects.all().delete()
    User.objects.all().delete()
    print("Existing data cleaned...")

# Clean any existing data first
clean_data()
write_courses()
write_instructors()
write_lessons()
