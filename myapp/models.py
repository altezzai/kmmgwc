from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='department_photos/', blank=True, null=True)
    
    def __str__(self):
        return self.name
    
# class Employee(models.Model):
#     POSITION_CHOICES = [
#         ("Principal","Principal"),
#         ("Head Of Department & Professor", "Head Of Department & Professor"),
#         ("Head of the Department & Associate Professor","Head of the Department & Associate Professor"),
#         ("Professor", "Professor"),
#         ("Associate Professor", "Associate Professor"),
#         ("Assistant Professor", "Assistant Professor"),
#         ("Guest Lecturer", "Guest Lecturer"),
#         ("Office Staff", "Office Staff"),
#     ]

#     name = models.CharField(max_length=255)
#     photo = models.ImageField(upload_to='photos/')
#     position = models.CharField(max_length=255)
#     qualification = models.TextField()
#     department = models.ForeignKey('Department', on_delete=models.CASCADE, null=True, blank=True)
#     def __str__(self):
#         return self.name
from django.db import models

class Employee(models.Model):
    POSITION_CHOICES = [
        ("Principal", "Principal"),
        ("Head Of Department & Professor", "Head Of Department & Professor"),
        ("Head of the Department & Associate Professor", "Head of the Department & Associate Professor"),
        ("Professor", "Professor"),
        ("Associate Professor", "Associate Professor"),
        ("Assistant Professor", "Assistant Professor"),
        ("Guest Lecturer", "Guest Lecturer"),
        ("Senior Superintendent","Senior Superintendent"),
        ("Head Accountant","Head Accountant"),
        ("Clerk ","Clerk "),
        ("Librarian","Librarian"),
        ("Office Staff", "Office Staff"),
    ]

    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)
    position = models.CharField(max_length=255, choices=POSITION_CHOICES)
    qualification = models.TextField(null=True, blank=True)
    department = models.ForeignKey('Department', on_delete=models.CASCADE, null=True, blank=True)

    # New optional fields
    seniority = models.DateField(null=True, blank=True)
    total_work_experience = models.CharField(max_length=255, null=True, blank=True)
    seminars_conferences_organised = models.TextField(null=True, blank=True)
    publications = models.TextField(null=True, blank=True)
    books_published = models.TextField(null=True, blank=True)
    papers_presented = models.TextField(null=True, blank=True)
    awards_honours = models.TextField(null=True, blank=True)
    personal_webpage = models.URLField(null=True, blank=True)
    additional_responsibilities = models.TextField(null=True, blank=True)
    phd_mphil_projects_guided = models.TextField(null=True, blank=True)
    major_minor_projects = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class NSSPhoto(models.Model):
    image = models.ImageField(upload_to='nss/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
class Activity(models.Model):
    name = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

class ActivityPhoto(models.Model):
    activity = models.ForeignKey(Activity, related_name='photos', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='photos/')
#     def __str__(self):
#         return f"{self.name} ({self.department.name})"  # Show department name in admin panel

class Event(models.Model):
    title = models.CharField(max_length=200)
    time = models.TimeField()
    date = models.DateField()
    description = models.TextField()
    venue = models.CharField(max_length=200)
    url = models.URLField()

    def __str__(self):
        return self.title

class News(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    image = models.ImageField(upload_to='news_images/', null=True, blank=True)
    def __str__(self):
        return self.title
class NewsImage(models.Model):
    news_article = models.ForeignKey(News, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='news_images/')

class Notification(models.Model):
    category = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    description = models.TextField()
    file = models.FileField(upload_to='uploads/', null=True, blank=True)

    def __str__(self):
        return self.title

class Exam(models.Model):
    category = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    description = models.TextField()
    # time = models.TimeField()
    # date = models.DateField()
    file = models.FileField(upload_to='exams/', null=True, blank=True)

    def __str__(self):
        return self.title

class IQACMember(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255, blank=True, null=True)  # Optional field

    def __str__(self):
        return self.name

class IQACMinute(models.Model):
    name = models.CharField(max_length=255)
    pdf = models.FileField(upload_to='iqac_minutes/')

    def __str__(self):
        return self.name
    
class StatementCompliance(models.Model):
    name = models.CharField(max_length=255)
    pdf = models.FileField(upload_to='statement_compliance/')

    def __str__(self):
        return self.name
    
class AQAR(models.Model):
    name = models.CharField(max_length=255)
    pdf = models.FileField(upload_to='aqar/')

    def __str__(self):
        return self.name

class AQARReport(models.Model):
    name = models.CharField(max_length=255)
    pdf = models.FileField(upload_to='aqar_report/')

    def __str__(self):
        return self.name
    
class AISHE(models.Model):
    name = models.CharField(max_length=255)
    pdf = models.FileField(upload_to='aishe/')

    def __str__(self):
        return self.name
    
class BestPractice(models.Model):
    name = models.CharField(max_length=255)
    pdf = models.FileField(upload_to='best_practice/')

    def __str__(self):
        return self.name

class StudentSatisfaction(models.Model):
    name = models.CharField(max_length=255)
    pdf = models.FileField(upload_to='student_satisfaction/')

    def __str__(self):
        return self.name

class AcademicCalendar(models.Model):
    name = models.CharField(max_length=255)
    pdf = models.FileField(upload_to='academic_calendar/')

    def __str__(self):
        return self.name

class Feedback(models.Model):
    name = models.CharField(max_length=255)
    pdf = models.FileField(upload_to='feedback/')

    def __str__(self):
        return self.name