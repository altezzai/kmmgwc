from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='department_photos/', blank=True, null=True)
    
    def __str__(self):
        return self.name
    
class Employee(models.Model):
    POSITION_CHOICES = [
        ("Head Of Department", "Head Of Department"),
        ("Professor", "Professor"),
        ("Associate Professor", "Associate Professor"),
        ("Assistant Professor", "Assistant Professor"),
        ("Visiting Faculty", "Visiting Faculty"),
        ("Office Staff", "Office Staff"),
    ]

    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/')
    position = models.CharField(max_length=255)
    qualification = models.TextField()
    department = models.ForeignKey('Department', on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Activity(models.Model):
    name = models.TextField()
    photo = models.ImageField(upload_to='photos/')
    department = models.ForeignKey(Department, on_delete=models.CASCADE)  # ForeignKey to Department

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