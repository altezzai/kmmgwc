from django.db import models

from .validators import validate_extension, validate_file, validate_size, no_html_validator


class Department(models.Model):
    name = models.CharField(validators=[no_html_validator], max_length=100, unique=True)
    description = models.TextField(validators=[no_html_validator], blank=True, null=True)
    photo = models.ImageField(
        upload_to="department_photos/",
        blank=True,
        null=True,
        validators=[validate_file, validate_extension, validate_size],
    )

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

#     name = models.CharField(validators=[no_html_validator], max_length=255)
#     photo = models.ImageField(upload_to='photos/')
#     position = models.CharField(validators=[no_html_validator], max_length=255)
#     qualification = models.TextField(validators=[no_html_validator], )
#     department = models.ForeignKey('Department', on_delete=models.CASCADE, null=True, blank=True)
#     def __str__(self):
#         return self.name
from django.db import models


class Employee(models.Model):
    POSITION_CHOICES = [
        ("Principal", "Principal"),
        ("Head Of Department & Professor", "Head Of Department & Professor"),
        (
            "Head of the Department & Associate Professor",
            "Head of the Department & Associate Professor",
        ),
        ("Professor", "Professor"),
        ("Associate Professor", "Associate Professor"),
        ("Assistant Professor", "Assistant Professor"),
        ("Guest Lecturer", "Guest Lecturer"),
        ("Senior Superintendent", "Senior Superintendent"),
        ("Head Accountant", "Head Accountant"),
        ("Clerk ", "Clerk "),
        ("Librarian", "Librarian"),
        ("Office Staff", "Office Staff"),
    ]

    name = models.CharField(validators=[no_html_validator], max_length=255)
    photo = models.ImageField(
        upload_to="photos/",
        null=True,
        blank=True,
        validators=[validate_file, validate_extension, validate_size],
    )
    position = models.CharField(validators=[no_html_validator], max_length=255, choices=POSITION_CHOICES)
    qualification = models.TextField(validators=[no_html_validator], null=True, blank=True)
    department = models.ForeignKey(
        "Department", on_delete=models.CASCADE, null=True, blank=True
    )

    # New optional fields
    seniority = models.DateField(null=True, blank=True)
    total_work_experience = models.CharField(validators=[no_html_validator], max_length=255, null=True, blank=True)
    seminars_conferences_organised = models.TextField(validators=[no_html_validator], null=True, blank=True)
    publications = models.TextField(validators=[no_html_validator], null=True, blank=True)
    books_published = models.TextField(validators=[no_html_validator], null=True, blank=True)
    papers_presented = models.TextField(validators=[no_html_validator], null=True, blank=True)
    awards_honours = models.TextField(validators=[no_html_validator], null=True, blank=True)
    personal_webpage = models.URLField(null=True, blank=True)
    additional_responsibilities = models.TextField(validators=[no_html_validator], null=True, blank=True)
    phd_mphil_projects_guided = models.TextField(validators=[no_html_validator], null=True, blank=True)
    major_minor_projects = models.TextField(validators=[no_html_validator], null=True, blank=True)

    def __str__(self):
        return self.name


class NSSPhoto(models.Model):
    image = models.ImageField(
        upload_to="nss/",
        validators=[validate_file, validate_extension, validate_size],
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)


class Activity(models.Model):
    name = models.TextField(validators=[no_html_validator], )
    department = models.ForeignKey(Department, on_delete=models.CASCADE)


class ActivityPhoto(models.Model):
    activity = models.ForeignKey(
        Activity, related_name="photos", on_delete=models.CASCADE
    )
    photo = models.ImageField(
        upload_to="photos/",
        validators=[validate_file, validate_extension, validate_size],
    )


#     def __str__(self):
#         return f"{self.name} ({self.department.name})"  # Show department name in admin panel


class Event(models.Model):
    title = models.CharField(validators=[no_html_validator], max_length=200)
    time = models.TimeField()
    date = models.DateField()
    description = models.TextField(validators=[no_html_validator], )
    venue = models.CharField(validators=[no_html_validator], max_length=200)
    url = models.URLField()

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(validators=[no_html_validator], max_length=255)
    description = models.TextField(validators=[no_html_validator], )
    date = models.DateField()
    image = models.ImageField(
        upload_to="news_images/",
        null=True,
        blank=True,
        validators=[validate_file, validate_extension, validate_size],
    )

    def __str__(self):
        return self.title


class NewsImage(models.Model):
    news_article = models.ForeignKey(
        News, on_delete=models.CASCADE, related_name="images"
    )
    image = models.ImageField(
        upload_to="news_images/",
        validators=[validate_file, validate_extension, validate_size],
    )


class Notification(models.Model):
    category = models.CharField(validators=[no_html_validator], max_length=50)
    title = models.CharField(validators=[no_html_validator], max_length=100)
    description = models.TextField(validators=[no_html_validator], )
    file = models.FileField(
        upload_to="uploads/",
        null=True,
        blank=True,
        validators=[validate_file, validate_extension, validate_size],
    )

    def __str__(self):
        return self.title


class Exam(models.Model):
    category = models.CharField(validators=[no_html_validator], max_length=50)
    title = models.CharField(validators=[no_html_validator], max_length=100)
    description = models.TextField(validators=[no_html_validator], )
    # time = models.TimeField()
    # date = models.DateField()
    file = models.FileField(
        upload_to="exams/",
        null=True,
        blank=True,
        validators=[validate_file, validate_extension, validate_size],
    )

    def __str__(self):
        return self.title


class IQACMember(models.Model):
    name = models.CharField(validators=[no_html_validator], max_length=255)
    position = models.CharField(validators=[no_html_validator], max_length=255, blank=True, null=True)  # Optional field

    def __str__(self):
        return self.name


class IQACMinute(models.Model):
    name = models.CharField(validators=[no_html_validator], max_length=255)
    pdf = models.FileField(
        upload_to="iqac_minutes/",
        validators=[validate_file, validate_extension, validate_size],
    )

    def __str__(self):
        return self.name


class StatementCompliance(models.Model):
    name = models.CharField(validators=[no_html_validator], max_length=255)
    pdf = models.FileField(
        upload_to="statement_compliance/",
        validators=[validate_file, validate_extension, validate_size],
    )

    def __str__(self):
        return self.name


class AQAR(models.Model):
    name = models.CharField(validators=[no_html_validator], max_length=255)
    pdf = models.FileField(
        upload_to="aqar/",
        validators=[validate_file, validate_extension, validate_size],
    )

    def __str__(self):
        return self.name


class AQARReport(models.Model):
    name = models.CharField(validators=[no_html_validator], max_length=255)
    pdf = models.FileField(
        upload_to="aqar_report/",
        validators=[validate_file, validate_extension, validate_size],
    )

    def __str__(self):
        return self.name


class AISHE(models.Model):
    name = models.CharField(validators=[no_html_validator], max_length=255)
    pdf = models.FileField(
        upload_to="aishe/",
        validators=[validate_file, validate_extension, validate_size],
    )

    def __str__(self):
        return self.name


class BestPractice(models.Model):
    name = models.CharField(validators=[no_html_validator], max_length=255)
    pdf = models.FileField(
        upload_to="best_practice/",
        validators=[validate_file, validate_extension, validate_size],
    )

    def __str__(self):
        return self.name


class StudentSatisfaction(models.Model):
    name = models.CharField(validators=[no_html_validator], max_length=255)
    pdf = models.FileField(
        upload_to="student_satisfaction/",
        validators=[validate_file, validate_extension, validate_size],
    )

    def __str__(self):
        return self.name


class AcademicCalendar(models.Model):
    name = models.CharField(validators=[no_html_validator], max_length=255)
    pdf = models.FileField(
        upload_to="academic_calendar/",
        validators=[validate_file, validate_extension, validate_size],
    )

    def __str__(self):
        return self.name


class Feedback(models.Model):
    name = models.CharField(validators=[no_html_validator], max_length=255)
    pdf = models.FileField(
        upload_to="feedback/",
        validators=[validate_file, validate_extension, validate_size],
    )

    def __str__(self):
        return self.name
