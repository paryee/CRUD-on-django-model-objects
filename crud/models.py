from django.db import models
from django.utils.timezone import now

# Define your models from here:
# User model
class User(models.Model):
    first_name = models.CharField(null=False, max_length=30, default='john')
    last_name = models.CharField(null=False, max_length=30, default='doe')
    dob = models.DateField(null=True)
    email = models.EmailField(null=False, max_length=254, unique=True, default='john.doe@gmail.com')
    location = models.CharField(null=True, max_length=100, default='Ghana')

    # Create a toString method for object string representation
    def __str__(self):
        return self.first_name + " " + self.last_name

# Instructor model
class Instructor(User):
    full_time = models.BooleanField(default=True)
    total_learners = models.IntegerField()

    # Create a toString method for object string representation
    def __str__(self):
        return f"First name: {self.first_name}, Last name: {self.last_name}, Is full time: {self.full_time}, Total Learners: {self.total_learners}"

# Course model
class Course(models.Model):
    name = models.CharField(null=False, max_length=100, default='online course')
    description = models.CharField(max_length=500)
    # Many-To-Many relationship with Instructors
    instructors = models.ManyToManyField(Instructor)
    # Many-To-Many relationship with Learners via Enrollment relationship
    learners = models.ManyToManyField('Learner', through='Enrollment')

    def __str__(self):
        return f"Name: {self.name}, Description: {self.description}"

# Lesson model
class Lesson(models.Model):
    title = models.CharField(max_length=200, default="title")
    course = models.ForeignKey(Course, null=True, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.title

# Learner model
class Learner(User):
    STUDENT = 'student'
    DEVELOPER = 'developer'
    DATA_SCIENTIST = 'data_scientist'
    DATABASE_ADMIN = 'dba'
    OCCUPATION_CHOICES = [
        (STUDENT, 'Student'),
        (DEVELOPER, 'Developer'),
        (DATA_SCIENTIST, 'Data Scientist'),
        (DATABASE_ADMIN, 'Database Admin')
    ]
    # Occupation Char field with defined enumeration choices
    occupation = models.CharField(
        null=False,
        max_length=20,
        choices=OCCUPATION_CHOICES,
        default=STUDENT
    )
    # Social link URL field
    social_link = models.URLField(max_length=200)

    # Create a toString method for object string representation
    def __str__(self):
        return f"First name: {self.first_name}, Last name: {self.last_name}, Date of Birth: {self.dob}, Occupation: {self.occupation}, Social Link: {self.social_link}"

# Enrollment model
class Enrollment(models.Model):
    learner = models.ForeignKey(Learner, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_enrolled = models.DateField(default=now)

    def __str__(self):
        return f"Learner: {self.learner}, Course: {self.course}, Date Enrolled: {self.date_enrolled}"
