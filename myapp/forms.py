from django import forms
from .models import (
    Notification,
    IQACMember,
    IQACMinute,
    StatementCompliance,
    AQAR,
    AQARReport,
    AISHE,
    BestPractice,
    StudentSatisfaction,
    Feedback,
    AcademicCalendar,
)

class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = ['category', 'title', 'description', 'file']

class IQACMemberForm(forms.ModelForm):
    class Meta:
        model = IQACMember
        fields = ['name', 'position']

class IQACMinuteForm(forms.ModelForm):
    class Meta:
        model = IQACMinute
        fields = ['name', 'pdf']

class StatementComplianceForm(forms.ModelForm):
    class Meta:
        model = StatementCompliance
        fields = ['name', 'pdf']

class AQARForm(forms.ModelForm):
    class Meta:
        model = AQAR
        fields = ['name', 'pdf']

class AQARReportForm(forms.ModelForm):
    class Meta:
        model = AQARReport
        fields = ['name', 'pdf']

class AISHEForm(forms.ModelForm):
    class Meta:
        model = AISHE
        fields = ['name', 'pdf']

class BestPracticeForm(forms.ModelForm):
    class Meta:
        model = BestPractice
        fields = ['name', 'pdf']

class StudentSatisfactionForm(forms.ModelForm):
    class Meta:
        model = StudentSatisfaction
        fields = ['name', 'pdf']

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'pdf']

class AcademicCalendarForm(forms.ModelForm):
    class Meta:
        model = AcademicCalendar
        fields = ['name', 'pdf']
