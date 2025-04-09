from django.shortcuts import render, redirect ,get_object_or_404
from .models import Employee
from .models import Department
from .models import Event
from .models import News,NewsImage
from .models import Notification
from .models import Activity
from .models import IQACMember
from .models import IQACMinute
from .models import StatementCompliance
from .models import AQAR, AQARReport
from .models import AISHE
from .models import BestPractice
from .models import StudentSatisfaction
from .models import AcademicCalendar
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from datetime import date
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.storage import default_storage
from django.conf import settings
import sys
import os
#home
def index(request):
    # employees = Employee.objects.all()
    evt = Event.objects.all().order_by('-date')[:3]

    nws = News.objects.all().order_by('-id')[:3]
    return render(request, 'index.html',{'events': evt,'news': nws})

def news(request,nw_id):
    nw = get_object_or_404(News, pk=nw_id)
    nws = News.objects.all().order_by('-id')[:3]
    return render(request, 'news.html',{'news': nw,'newses': nws})
def allnews(request):
    nws = News.objects.all().order_by('-id')
    return render(request, 'morenews.html',{'newses': nws})

def events(request,ev_id):
    ev = get_object_or_404(Event, pk=ev_id)
    evt = Event.objects.all().order_by('-date')[:3]
    return render(request, 'events.html',{'events': evt,'evt': ev})

def allevents(request):
    evt = Event.objects.all().order_by('-date')
    return render(request, 'allevents.html',{'events': evt})

# def faculty(request,dept):
#     employees = Employee.objects.filter(department=dept)

#     # print(type(employees[0].qualification))
#     return render(request, 'faculty.html',{'employees':employees,'depart':dept})
# def faculty(request, dept):
#     department = get_object_or_404(Department, pk=dept)  # Fetch department by ID
#     employees = Employee.objects.filter(department=dept)
#     activities = Activity.objects.filter(department=dept)
#     return render(request, 'faculty.html', {'employees': employees, 'depart': department.name, "description":department.description, 'activities': activities})
def faculty(request, dept):
    department = get_object_or_404(Department, pk=dept)

    # Define custom order for positions
    position_order = {
        "Head Of Department": 1,
        "Professor": 2,
        "Associate Professor": 3,
        "Assistant Professor": 4,
        "Visiting Faculty": 5,
        "Office Staff": 6,
    }

    # Get all employees and sort based on custom order
    employees = list(Employee.objects.filter(department=department))
    employees.sort(key=lambda emp: position_order.get(emp.position, 999))  # default 999 if unmatched

    activities = Activity.objects.filter(department=department)

    return render(request, 'faculty.html', {
        'employees': employees,
        'depart': department.name,
        'description': department.description,
        'activities': activities
    })

def club(request):
    # employees = Employee.objects.all()
    return render(request, 'nss.html')
def fitness(request):
    # employees = Employee.objects.all()
    return render(request, 'fitness.html')
def alumini(request):
    # employees = Employee.objects.all()
    return render(request, 'alumini.html')
def courses(request):
    # employees = Employee.objects.all()
    return render(request, 'courses.html')
def admission(request):
    return render(request, 'admission.html')

def academic_calendar(request):
    calendars = AcademicCalendar.objects.all()
    return render(request, 'academic_calendar.html', {'calendars': calendars})

def exam_calendar(request):
    return render(request, 'exam_calendar.html')

def academic_results(request):
    return render(request, 'academic_results.html')

def committies(request):
    return render(request, 'committies.html')

def pta(request):
    return render(request, 'pta.html')

def college_union(request):
    return render(request, 'college_union.html')

def clubs(request):
    return render(request, 'clubs.html')

def FYUGP(request):
    return render(request, 'FYUGP.html')
def iqac(request):
    # employees = Employee.objects.all()
    return render(request, 'iqac.html')

def staffcouncil(request):
    # employees = Employee.objects.all()
    return render(request, 'staffcouncil.html')
# def about(request):
#     # employees = Employee.objects.all()
#     return render(request, 'about.html')

def about_college(request):
    return render(request, 'about_college.html')

def rti(request):
    return render(request, 'rti.html')

def cdc(request):
    return render(request, 'cdc.html')

def office(request):
    office_staff = Employee.objects.filter(position="Office Staff")  # Fetch only office staff
    # return render(request, 'office.html')
    return render(request, 'office.html', {'employees': office_staff})

#Faclilties
def academic_facilities(request):
    return render(request, 'academic_facilities.html')

def library(request):
    return render(request, 'library.html')

def orice(request):
    return render(request, 'orice.html')

def procedures_policy(request):
    return render(request, 'procedures_policy.html')

def it_facility(request):
    return render(request, 'it_facility.html')

def sports_facility(request):
    return render(request, 'sports_facility.html')

def amenity_centre(request):
    return render(request, 'amenity_centre.html')

def canteen(request):
    return render(request, 'canteen.html')

def womens_hostel(request):
    return render(request, 'womens_hostel.html')

def auditorium_seminar_halls(request):
    return render(request, 'auditorium_seminar_halls.html')

#Research
def research_centre(request):
    return render(request, 'research_centre.html')

def research_guides(request):
    return render(request, 'research_guides.html')

def research_scholars(request):
    return render(request, 'research_scholars.html')

def research_projects(request):
    return render(request, 'research_projects.html')

def research_journal(request):
    return render(request, 'research_journal.html')

#Student Support
def scholarships(request):
    return render(request, 'scholarships.html')

def career_guidance(request):
    return render(request, 'career_guidance.html')

def yip(request):
    return render(request, 'yip.html')

def grievance_redressal(request):
    return render(request, 'grievance_redressal.html')

def endowments(request):
    return render(request, 'endowments.html')

def feedback(request):
    return render(request, 'feedback.html')

def code_of_conduct(request):
    return render(request, 'code_of_conduct.html')


def applicatonforms(request):
    # employees = Employee.objects.all()
    return render(request, 'applicatonforms.html')
def placement(request):
    # employees = Employee.objects.all()
    return render(request, 'placement.html')
def scholarship(request):
    # employees = Employee.objects.all()
    return render(request, 'scholarship.html')
def universityinfo(request):
    # employees = Employee.objects.all()
    return render(request, 'universityinfo.html')
def notification(request):
    noti = Notification.objects.all().order_by('-id')
    return render(request, 'notification2.html',{'notifications':noti,'cat':"all"})
def notificationfilter(request,upg):
    noti = Notification.objects.filter(category=upg).order_by('-id')
    return render(request, 'notification2.html',{'notifications':noti,'cat':upg})
def notification2(request ,noti_id):
    notification = get_object_or_404(Notification, pk=noti_id)

    return render(request, 'notifications.html', {'notification': notification})
    # return render(request, 'notifications.html',{'notification':noti2})

def manager(request):
    return render(request, "manager.html")
def principal(request):
    return render(request, "principal.html")
def statement(request):
    statements = StatementCompliance.objects.all().order_by('-id')  # Fetch all statement records
    return render(request, 'statement.html', {'statements': statements})
# def minutes(request):
#     return render(request, "minutes.html")
def minutes(request):
    iqac_minutes = IQACMinute.objects.all().order_by('-id')  # Fetch all minutes
    return render(request, 'minutes.html', {'minutes': iqac_minutes})
def aishe(request):
    aishe_records = AISHE.objects.all().order_by('-id')
    return render(request, 'aishe.html', {'aishe_records': aishe_records})
def aqar(request):
    return render(request, "aqar.html")
def iqac_activities(request):
    return render(request, "iqac_activities.html")
def best_practice(request):
    best_practices = BestPractice.objects.all().order_by('-id')
    return render(request, 'best_practice.html', {'best_practices': best_practices})
def student_satisfaction(request):
    student_satisfaction_entries = StudentSatisfaction.objects.all()
    return render(request, "student_satisfaction.html", {"entries": student_satisfaction_entries})


def institutional_distinctiveness(request):
    return render(request, "institutional_distinctiveness.html")

#Department
def department_list(request):
    """Display all departments."""
    if 'username' in request.session:
        departments = Department.objects.all().order_by('name')
        return render(request, 'department_list.html', {'departments': departments})
    return redirect('login')

def create_department(request):
    """Create a new department."""
    if 'username' in request.session:
        if request.method == 'POST':
            name = request.POST.get('name')
            description = request.POST.get('description', '')
            photo = request.FILES.get('photos', None)

            department = Department(name=name, description=description)
            #Assign the photo only if it exists
            if photo:
                department.photo = photo
            department.save()
            departments = Department.objects.all()
            print("Departments:", departments)
            return redirect('department_list')
        return render(request, 'create_department.html')
    return redirect('login')

def update_department(request, pk):
    """Update an existing department."""
    if 'username' in request.session:
        department = get_object_or_404(Department, pk=pk)

        if request.method == 'POST':
            department.name = request.POST['name']
            department.description = request.POST.get('description', '')

            # If a new photo is uploaded, delete the old one and update
            if 'photo' in request.FILES:
                if department.photo:
                    default_storage.delete(department.photo.path)  # Delete old photo
                department.photo = request.FILES['photo']

            department.save()
            return redirect('department_list')

        return render(request, 'update_department.html', {'department': department})
    return redirect('login')


def delete_department(request, pk):
    """Delete a department and its associated image."""
    if 'username' in request.session:
        if request.method == "POST":  # Only allow deletion via POST
            try:
                department = get_object_or_404(Department, id=pk)

                # Delete associated photo if it exists
                if department.photo:
                    photo_path = department.photo.path  # Get the full file path
                    if os.path.isfile(photo_path):  # Ensure file exists before deleting
                        default_storage.delete(photo_path)

                department.delete()  # Delete department after removing photo
                return redirect('department_list')

            except Exception as e:
                print(f"Error deleting department {pk}: {e}")

        return redirect('department_list')  # Redirect if not POST

    return redirect('login')


#Employee

# Function to compress image before saving
def compress_image(image):
    try:
        img = Image.open(image)
        img = img.convert('RGB')  # Ensure it's in RGB mode (not RGBA)
        img_io = io.BytesIO()
        img.save(img_io, format='JPEG', quality=70)  # Adjust quality as needed
        return InMemoryUploadedFile(
            img_io, None, image.name, 'image/jpeg', img_io.tell, None
        )
    except Exception as e:
        raise Exception(f"Compression error: {str(e)}")

# Employee creation view
def create_employee(request):
    if 'username' in request.session:  # Ensure the user is logged in
        if request.method == 'POST':
            try:
                # Validate name and position fields
                name = request.POST.get('name', '').strip()
                position = request.POST.get('position', '').strip()
                qualification = request.POST.get('qualification', '').strip()
                department_id = request.POST.get('department')

                if not name or not position or not qualification or not department_id:
                    return render(request, 'create_employee.html', 
                                  {'error': 'All fields are required'})

                # Validate department
                try:
                    department = Department.objects.get(id=department_id)
                except ObjectDoesNotExist:
                    return render(request, 'create_employee.html', 
                                  {'error': 'Invalid department selected'})

                # Validate and compress photo
                if 'photo' not in request.FILES:
                    return render(request, 'create_employee.html', 
                                  {'error': 'Please upload a photo'})

                photo = request.FILES['photo']
                
                if not photo.content_type.startswith('image/'):
                    return render(request, 'create_employee.html', 
                                  {'error': 'Please upload a valid image file'})

                if photo.size > 5 * 1024 * 1024:  # 5MB size limit
                    return render(request, 'create_employee.html', 
                                  {'error': 'Photo size should be less than 5MB'})

                # Compress the photo
                try:
                    compressed_photo = compress_image(photo)
                except Exception as e:
                    return render(request, 'create_employee.html', 
                                  {'error': f'Error processing photo: {str(e)}'})

                # Save employee record
                employee = Employee(
                    name=name,
                    position=position,
                    photo=compressed_photo,
                    qualification=qualification,
                    department=department
                )
                employee.save()

                return redirect('employee_list')

            except Exception as e:
                return render(request, 'create_employee.html', 
                              {'error': f'Error creating employee: {str(e)}'})

        # Fetch departments for dropdown
        department_list = Department.objects.all()
        return render(request, 'create_employee.html', {"departments": department_list})

    return redirect('login')

def employee_list(request):
    if 'username' in request.session:
        employees = Employee.objects.all().order_by('-id')
        return render(request, 'employee_list.html', {'employees': employees})
    return redirect('login')
def delete_old_photo(employee):
    """
    Safely delete the old photo file from storage
    """
    if employee.photo:
        if os.path.isfile(employee.photo.path):
            try:
                os.remove(employee.photo.path)
            except Exception as e:
                print(f"Error deleting old photo: {e}")


def update_employee(request, employee_id):
    if 'username' in request.session:
        employee = get_object_or_404(Employee, pk=employee_id)
        department_list = Department.objects.all()

        if request.method == 'POST':
            try:
                # Get form data
                name = request.POST.get('name', '').strip()
                position = request.POST.get('position', '').strip()
                qualification = request.POST.get('qualification', '').strip()
                department_id = request.POST.get('department')

                # Ensure all fields are filled
                if not name or not position or not qualification or not department_id:
                    return render(request, 'update_employee.html', 
                                  {'employee': employee, 'departments': department_list, 
                                   'error': 'All fields are required'})

                # Convert department_id to Department object
                try:
                    department = Department.objects.get(id=department_id)
                except ObjectDoesNotExist:
                    return render(request, 'update_employee.html', 
                                  {'employee': employee, 'departments': department_list, 
                                   'error': 'Invalid department selected'})

                # Update employee fields
                employee.name = name
                employee.position = position
                employee.qualification = qualification
                employee.department = department  # ✅ Assign Department object, not ID

                # Handle photo update
                if 'photo' in request.FILES:
                    photo = request.FILES['photo']
                    
                    # Validate file type
                    if not photo.content_type.startswith('image/'):
                        return render(request, 'update_employee.html', 
                                      {'employee': employee, 'departments': department_list, 
                                       'error': 'Please upload a valid image file'})

                    # Check file size (max 5MB)
                    if photo.size > 5 * 1024 * 1024:
                        return render(request, 'update_employee.html', 
                                      {'employee': employee, 'departments': department_list, 
                                       'error': 'Photo size should be less than 5MB'})

                    try:
                        # Delete old photo first
                        delete_old_photo(employee)
                        # Compress and save new photo
                        compressed_photo = compress_image(photo)
                        employee.photo = compressed_photo
                    except Exception as e:
                        return render(request, 'update_employee.html', 
                                      {'employee': employee, 'departments': department_list, 
                                       'error': f'Error processing photo: {str(e)}'})

                # Save updated employee
                employee.save()
                return redirect('employee_list')

            except Exception as e:
                return render(request, 'update_employee.html', 
                              {'employee': employee, 'departments': department_list, 
                               'error': f'Error updating employee: {str(e)}'})

        return render(request, 'update_employee.html', 
                      {'employee': employee, 'departments': department_list})

    return redirect('login')

def delete_employee(request, employee_id):
    if 'username' in request.session:
        employee = get_object_or_404(Employee, pk=employee_id)
        employee.delete()
        delete_old_photo(employee)
        return redirect('employee_list')
    return redirect('login')

#Activity

def create_activity(request):
    if 'username' in request.session:
        if request.method == 'POST':
            try:
                # Debugging: Check incoming data
                print("POST Data:", request.POST)
                print("FILES Data:", request.FILES)

                # First check if a file was uploaded
                if 'photo' not in request.FILES:
                    return render(request, 'create_activity.html', 
                                  {'error': 'Please upload a photo'})
                
                photo = request.FILES['photo']
                
                # Validate file type
                if not photo.content_type.startswith('image/'):
                    return render(request, 'create_activity.html', 
                                  {'error': 'Please upload a valid image file'})
                
                # Check file size (e.g., max 5MB)
                if photo.size > 5 * 1024 * 1024:  # 5MB in bytes
                    return render(request, 'create_activity.html', 
                                  {'error': 'Photo size should be less than 5MB'})

                # Compress the photo
                try:
                    compressed_photo = compress_image(photo)
                except Exception as e:
                    print(f"Error compressing image: {e}")
                    return render(request, 'create_activity.html', 
                                  {'error': f'Error processing photo: {str(e)}'})

                # Convert department ID to Department object
                department_id = request.POST.get('department')
                department = get_object_or_404(Department, id=department_id)

                # Create Activity object
                activity = Activity(
                    name=request.POST.get('name'),  # Ensure this matches your form input
                    photo=compressed_photo,
                    department=department  # ✅ Assign Department object, not ID
                )
                activity.save()
                print("Activity saved successfully!")

                return redirect('activity_list')

            except Exception as e:
                print(f"Error creating activity: {e}")
                return render(request, 'create_activity.html', 
                              {'error': f'Error creating activity: {str(e)}'})
        
        # Load departments for dropdown
        department_list = Department.objects.all()
        return render(request, 'create_activity.html', {"departments": department_list})

    return redirect('login')

def activity_list(request):
    if 'username' in request.session:
        activities = Activity.objects.all()  # Retrieve all activities
        # activities = Activity.objects.select_related('department').all()  # Optimize queries
        return render(request, 'activity_list.html', {'activities': activities})
    return redirect('login')
def delete_old_photo(activity):
    """
    Safely delete the old photo file from storage
    """
    if activity.photo:
        if os.path.isfile(activity.photo.path):
            try:
                os.remove(activity.photo.path)
            except Exception as e:
                print(f"Error deleting old photo: {e}")

def update_activity(request, activity_id):
    if 'username' in request.session:
        activity = get_object_or_404(Activity, pk=activity_id)
        department_list = Department.objects.all()

        if request.method == 'POST':
            name = request.POST.get('name')
            department_id = request.POST.get('department')  # Getting the department ID as a string
            
            # Convert department_id to a Department instance
            department = get_object_or_404(Department, pk=department_id)

            photo = request.FILES.get('photo')

            activity.name = name
            activity.department = department  # ✅ Assign the correct instance

            # Handle photo upload (if exists)
            if 'photo' in request.FILES:
                photo = request.FILES['photo']
                
                # Validate file type
                if not photo.content_type.startswith('image/'):
                    return render(request, 'update_activity.html', {
                        'activity': activity,
                        'departments': department_list,
                        'error': 'Please upload a valid image file'
                    })
                
                # Check file size (max 5MB)
                if photo.size > 5 * 1024 * 1024:
                    return render(request, 'update_activity.html', {
                        'activity': activity,
                        'departments': department_list,
                        'error': 'Photo size should be less than 5MB'
                    })

                try:
                    # Delete old photo first
                    delete_old_photo(activity)
                    # Compress and save new photo
                    compressed_photo = compress_image(photo)
                    activity.photo = compressed_photo
                except Exception as e:
                    return render(request, 'update_activity.html', {
                        'activity': activity,
                        'departments': department_list,
                        'error': f'Error processing photo: {str(e)}'
                    })

            activity.save()
            return redirect('activity_list')

        return render(request, 'update_activity.html', {'activity': activity, 'departments': department_list})
    
    return redirect('login')

def delete_activity(request, pk):  # Ensure `pk` is a parameter
    activity = get_object_or_404(Activity, pk=pk)  # Fetch the activity
    activity.delete()  # Delete the activity
    return redirect('activity_list')  # Redirect to the activity list



#Event
def compress_image(image_file):
    """
    Compress the input image file while maintaining aspect ratio
    Returns a compressed InMemoryUploadedFile object
    """
    img = Image.open(image_file)
    
    # Convert to RGB if image is in RGBA mode
    if img.mode == 'RGBA':
        img = img.convert('RGB')
    
    # Set maximum dimensions
    max_width = 800
    max_height = 800
    
    # Calculate new dimensions while maintaining aspect ratio
    ratio = min(max_width/img.width, max_height/img.height)
    new_width = int(img.width * ratio)
    new_height = int(img.height * ratio)
    
    # Resize image
    img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
    
    # Save the compressed image
    output = BytesIO()
    img.save(output, format='JPEG', quality=75, optimize=True)
    output.seek(0)
    
    return InMemoryUploadedFile(
        output,
        'ImageField',
        f"{image_file.name.split('.')[0]}.jpg",
        'image/jpeg',
        sys.getsizeof(output),
        None
    )
def event_list(request):

    if 'username' in request.session:
        events = Event.objects.all().order_by('-id')
        return render(request, 'event_list.html', {'events': events})
    return redirect('login')
def event_create(request):
    if 'username' in request.session:
        if request.method == 'POST':
            title = request.POST.get('title')
            time = request.POST.get('time')
            date = request.POST.get('date')
            description = request.POST.get('description')
            venue = request.POST.get('venue')
            url = request.POST.get('url')

            event = Event(title=title, time=time, date=date, description=description, venue=venue, url=url)
            event.save()
            return redirect('event_list')
        return render(request, 'event_create.html')
    return redirect('login')
def event_update(request, event_id):
    if 'username' in request.session:
        event = get_object_or_404(Event, pk=event_id)
        if request.method == 'POST':
            event.title = request.POST.get('title')
            event.time = request.POST.get('time')
            event.date = request.POST.get('date')
            event.description = request.POST.get('description')
            event.venue = request.POST.get('venue')
            event.url = request.POST.get('url')
            event.save()
            return redirect('event_list')
        return render(request, 'event_update.html', {'event': event})
    return redirect('login')
def event_delete(request, event_id):
    if 'username' in request.session:
        event = get_object_or_404(Event, pk=event_id)
        event.delete()
        return redirect('event_list')
    return redirect('login')
#News
def news_list(request):
    if 'username' in request.session:
        news_articles = News.objects.all().order_by('-id')
        return render(request, 'news_list.html', {'news_articles': news_articles})
    return redirect('login')

def create_news(request):
    if 'username' in request.session:
        if request.method == 'POST':
            title = request.POST['title']
            description = request.POST['description']
            d = request.POST['date']
            
            # Create the news article first
            news_article = News.objects.create(
                title=title,
                description=description,
                date=d
            )
            
            # Process and save each uploaded image
            for image_file in request.FILES.getlist('photos'):
                # Compress the image
                compressed_image = compress_image(image_file)
                
                # Create NewsImage object with compressed image
                NewsImage.objects.create(
                    news_article=news_article,
                    image=compressed_image
                )
            
            return redirect('news_list')
        
        return render(request, 'create_news.html')
    return redirect('login')
def update_news(request, pk):
    if 'username' in request.session:
        article = get_object_or_404(News, pk=pk)

        if request.method == 'POST':
            # Update the text fields (title and description)
            article.title = request.POST['title']
            article.description = request.POST['description']
            
            # Handle new images
            if request.FILES:
                for image_file in request.FILES.getlist('photos'):
                    # Compress each new image
                    compressed_image = compress_image(image_file)
                    
                    # Create new NewsImage object with compressed image
                    NewsImage.objects.create(
                        news_article=article,
                        image=compressed_image
                    )
            
            article.save()
            # for image_file in request.FILES.getlist('photos'):
            #     NewsImage.objects.create(news_article=article, image=image_file)

            return redirect('news_list')

        return render(request, 'update_news.html', {'article': article})
    return redirect('login')

# news/views.py


def delete_news(request, pk):
    """
    Delete a news article and all its associated images
    """
    if 'username' in request.session:
        try:
            # Get the news article
            article = get_object_or_404(News, pk=pk)
            
            # Get all associated images before deleting the article
            images = NewsImage.objects.filter(news_article=article)
            
            # Delete each image file from storage
            for image in images:
                if image.image:
                    # Get the full path of the image
                    image_path = os.path.join(settings.MEDIA_ROOT, str(image.image))
                    try:
                        # Check if file exists before attempting deletion
                        if os.path.isfile(image_path):
                            os.remove(image_path)
                    except Exception as e:
                        print(f"Error deleting image file {image_path}: {e}")
            
            # Delete the news article (this will also delete associated NewsImage objects
            # due to CASCADE deletion in the database)
            article.delete()
            
            return redirect('news_list')
            
        except Exception as e:
            # Log the error and redirect
            print(f"Error deleting news article {pk}: {e}")
            return redirect('news_list')
            
    return redirect('login')

#Academic Calander
def academic_calendar_list(request):
    calendars = AcademicCalendar.objects.all()
    return render(request, 'academic_calendar_list.html', {'calendars': calendars})

def create_academic_calendar(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        pdf = request.FILES.get('pdf')
        
        if name and pdf:
            AcademicCalendar.objects.create(name=name, pdf=pdf)
            return redirect('academic_calendar_list')  # Redirect to the list page

    return render(request, 'create_academic_calendar.html')

def update_academic_calendar(request, id):
    calendar = get_object_or_404(AcademicCalendar, id=id)

    if request.method == 'POST':
        calendar.name = request.POST.get('name')
        if 'pdf' in request.FILES:
            calendar.pdf = request.FILES['pdf']
        calendar.save()
        return redirect('academic_calendar_list')

    return render(request, 'update_academic_calendar.html', {'calendar': calendar})

def delete_academic_calendar(request, id):
    calendar = get_object_or_404(AcademicCalendar, id=id)
    calendar.delete()
    return redirect('academic_calendar_list')

#IQAC Member

def iqac_member_list(request):
    if 'username' in request.session:
        iqac_members = IQACMember.objects.all()
        return render(request, 'iqac_member_list.html', {'iqac_members': iqac_members})
    return redirect('login')

def create_iqac_member(request):
    """ Create a new IQAC member """
    if 'username' in request.session:
        if request.method == 'POST':
            name = request.POST['name']
            position = request.POST.get('position', '')  # Optional

            IQACMember.objects.create(name=name, position=position)

            return redirect('iqac_member_list')

        return render(request, 'create_iqac_member.html')

    return redirect('login')


def update_iqac_member(request, id):
    """ Update an existing IQAC member """
    if 'username' in request.session:
        member = get_object_or_404(IQACMember, pk=id)

        if request.method == 'POST':
            member.name = request.POST['name']
            member.position = request.POST.get('position', '')

            member.save()
            return redirect('iqac_member_list')

        return render(request, 'update_iqac_member.html', {'member': member})

    return redirect('login')


def delete_iqac_member(request, id):
    """ Delete an IQAC member """
    if 'username' in request.session:
        member = get_object_or_404(IQACMember, pk=id)
        member.delete()
        return redirect('iqac_member_list')

    return redirect('login')

def iqac(request):
    iqac_members = IQACMember.objects.all().order_by('id')  # Fetch all members
    return render(request, 'iqac.html', {'iqac_members': iqac_members})

#iqac_minutes
def minutes_list(request):
    iqac_minutes = IQACMinute.objects.all().order_by('-id')  # Fetch all IQAC minutes
    return render(request, 'minutes.html', {'iqac_minutes': iqac_minutes})

def iqac_minutes_list(request):
    if 'username' in request.session:
        iqac_minutes = IQACMinute.objects.all().order_by('-id')
        return render(request, 'iqac_minutes_list.html', {'iqac_minutes': iqac_minutes})
    return redirect('login')

def create_iqac_minute(request):
    if 'username' in request.session:
        if request.method == 'POST':
            name = request.POST['name']
            pdf = request.FILES['pdf']
            IQACMinute.objects.create(name=name, pdf=pdf)
            return redirect('iqac_minutes_list')
        return render(request, 'create_iqac_minute.html')
    return redirect('login')

def update_iqac_minute(request, id):
    if 'username' in request.session:
        minute = get_object_or_404(IQACMinute, id=id)
        if request.method == 'POST':
            minute.name = request.POST['name']
            if 'pdf' in request.FILES:
                minute.pdf = request.FILES['pdf']
            minute.save()
            return redirect('iqac_minutes_list')
        return render(request, 'update_iqac_minute.html', {'minute': minute})
    return redirect('login')

def delete_iqac_minute(request, id):
    if 'username' in request.session:
        minute = get_object_or_404(IQACMinute, id=id)
        minute.delete()
        return redirect('iqac_minutes_list')
    return redirect('login')

#StatementComplaince
def statement_list(request):
    statements = StatementCompliance.objects.all().order_by('-id')  
    return render(request, 'statement.html', {'statements': statements})

def statement_compliance_list(request):
    if 'username' in request.session:
        statements = StatementCompliance.objects.all().order_by('-id')
        return render(request, 'statement_compliance_list.html', {'statements': statements})
    return redirect('login')

def create_statement_compliance(request):
    if 'username' in request.session:
        if request.method == 'POST':
            name = request.POST['name']
            pdf = request.FILES['pdf']
            StatementCompliance.objects.create(name=name, pdf=pdf)
            return redirect('statement_compliance_list')
        return render(request, 'create_statement_compliance.html')
    return redirect('login')

def update_statement_compliance(request, id):
    if 'username' in request.session:
        statement = get_object_or_404(StatementCompliance, id=id)
        if request.method == 'POST':
            statement.name = request.POST['name']
            if 'pdf' in request.FILES:
                statement.file = request.FILES['pdf']
            statement.save()
            return redirect('statement_compliance_list')
        return render(request, 'update_statement_compliance.html', {'statement': statement})
    return redirect('login')

def delete_statement_compliance(request, id):
    if 'username' in request.session:
        statement = get_object_or_404(StatementCompliance, id=id)
        statement.delete()
        return redirect('statement_compliance_list')
    return redirect('login')

#AQAR
def aqar(request):
    aqar_list = AQAR.objects.all().order_by('-id')
    aqar_reports = AQARReport.objects.all().order_by('-id')
    return render(request, "aqar.html", {'aqar_list': aqar_list, 'aqar_reports': aqar_reports})

def aqar_list(request):
    if 'username' in request.session:
        aqars = AQAR.objects.all().order_by("-id")  # Fetch all AQARs (latest first)
        return render(request, "aqar_list.html", {"aqars": aqars})
    return redirect("login")

def create_aqar(request):
    if 'username' in request.session:  # Ensure user is logged in
        if request.method == "POST":
            name = request.POST["name"]
            pdf = request.FILES.get("pdf")  # Ensure PDF is uploaded
            
            if name and pdf:  # Ensure fields are not empty
                AQAR.objects.create(name=name, pdf=pdf)
                return redirect("aqar_list")  # Redirect to list after saving

        return render(request, "create_aqar.html")  # Show form if GET request
    return redirect("login")

def update_aqar(request, id):
    if 'username' in request.session:
        aqar = get_object_or_404(AQAR, id=id)
        if request.method == 'POST':
            aqar.name = request.POST['name']
            if 'pdf' in request.FILES:
                aqar.pdf = request.FILES['pdf']
            aqar.save()
            return redirect('aqar_list')
        return render(request, 'update_aqar.html', {'aqar': aqar})
    return redirect('login')

def delete_aqar(request, id):
    if 'username' in request.session:
        aqar = get_object_or_404(AQAR, id=id)
        aqar.delete()
        return redirect('aqar_list')
    return redirect('login')

#AQAR Report
def aqar_report_list(request):
    if 'username' in request.session:
        aqar_reports = AQARReport.objects.all().order_by('-id')
        return render(request, "aqar_report_list.html", {'aqar_reports': aqar_reports})
    return redirect('login')

def create_aqar_report(request):
    if 'username' in request.session:
        if request.method == 'POST':
            name = request.POST['name']
            pdf = request.FILES['pdf']
            AQARReport.objects.create(name=name, pdf=pdf)
            return redirect('aqar_report_list')
        return render(request, "create_aqar_report.html")
    return redirect('login')

def update_aqar_report(request, id):
    if 'username' in request.session:
        aqar_report = get_object_or_404(AQARReport, id=id)
        if request.method == 'POST':
            aqar_report.name = request.POST['name']
            if 'pdf' in request.FILES:
                aqar_report.pdf = request.FILES['pdf']
            aqar_report.save()
            return redirect('aqar_report_list')
        return render(request, 'update_aqar_report.html', {'aqar_report': aqar_report})
    return redirect('login')

def delete_aqar_report(request, id):
    if 'username' in request.session:
        aqar_report = get_object_or_404(AQARReport, id=id)
        aqar_report.delete()
        return redirect('aqar_report_list')
    return redirect('login')

#AISHE
def aishe_list(request):
    if 'username' in request.session:
        aishe_records = AISHE.objects.all().order_by('-id')
        return render(request, 'aishe_list.html', {'aishe_records': aishe_records})
    return redirect('login')

def create_aishe(request):
    if 'username' in request.session:
        if request.method == 'POST':
            name = request.POST['name']
            pdf = request.FILES['pdf']
            AISHE.objects.create(name=name, pdf=pdf)
            return redirect('aishe_list')
        return render(request, 'create_aishe.html')
    return redirect('login')

def update_aishe(request, id):
    if 'username' in request.session:
        aishe_record = get_object_or_404(AISHE, id=id)
        if request.method == 'POST':
            aishe_record.name = request.POST['name']
            if 'pdf' in request.FILES:
                aishe_record.pdf = request.FILES['pdf']
            aishe_record.save()
            return redirect('aishe_list')
        return render(request, 'update_aishe.html', {'aishe_record': aishe_record})
    return redirect('login')

def delete_aishe(request, id):
    if 'username' in request.session:
        aishe_record = get_object_or_404(AISHE, id=id)
        aishe_record.delete()
        return redirect('aishe_list')
    return redirect('login')

#Best Practice
# Admin: List Best Practices
def best_practice_list(request):
    if 'username' in request.session:
        best_practices = BestPractice.objects.all().order_by('-id')
        return render(request, 'best_practice_list.html', {'best_practices': best_practices})
    return redirect('login')

# Admin: Create Best Practice
def create_best_practice(request):
    if 'username' in request.session:
        if request.method == 'POST':
            name = request.POST['name']
            pdf = request.FILES['pdf']
            BestPractice.objects.create(name=name, pdf=pdf)
            return redirect('best_practice_list')
        return render(request, 'create_best_practice.html')
    return redirect('login')

# Admin: Update Best Practice
def update_best_practice(request, id):
    if 'username' in request.session:
        best_practice = get_object_or_404(BestPractice, id=id)
        if request.method == 'POST':
            best_practice.name = request.POST['name']
            if 'pdf' in request.FILES:
                best_practice.pdf = request.FILES['pdf']
            best_practice.save()
            return redirect('best_practice_list')
        return render(request, 'update_best_practice.html', {'best_practice': best_practice})
    return redirect('login')

# Admin: Delete Best Practice
def delete_best_practice(request, id):
    if 'username' in request.session:
        best_practice = get_object_or_404(BestPractice, id=id)
        best_practice.delete()
        return redirect('best_practice_list')
    return redirect('login')

#Student Satisfaction
def student_satisfaction_list(request):
    student_satisfactions = StudentSatisfaction.objects.all()
    return render(request, "student_satisfaction_list.html", {"student_satisfactions": student_satisfactions})

def create_student_satisfaction(request):
    if request.method == "POST":
        name = request.POST.get("name")
        pdf = request.FILES.get("pdf")

        if name and pdf:
            StudentSatisfaction.objects.create(name=name, pdf=pdf)
            return redirect("student_satisfaction_list")

    return render(request, "create_student_satisfaction.html")

def update_student_satisfaction(request, id):
    student_satisfaction = get_object_or_404(StudentSatisfaction, id=id)

    if request.method == "POST":
        student_satisfaction.name = request.POST.get("name", student_satisfaction.name)
        if request.FILES.get("pdf"):
            student_satisfaction.pdf = request.FILES.get("pdf")
        student_satisfaction.save()
        return redirect("student_satisfaction_list")

    return render(request, "edit_student_satisfaction.html", {"student_satisfaction": student_satisfaction})

def delete_student_satisfaction(request, id):
    student_satisfaction = get_object_or_404(StudentSatisfaction, id=id)
    student_satisfaction.delete()
    return redirect("student_satisfaction_list")

#Notificationreturn redirect('news_list')

def create_notification(request):
    if 'username' in request.session:
        if request.method == 'POST':
            category = request.POST.get('category')
            title = request.POST.get('title')
            description = request.POST.get('description')
            file = request.FILES.get('file')

            notification = Notification(category=category, title=title, description=description, file=file)
            notification.save()
            return redirect('list_notifications')
            return JsonResponse({'message': 'Notification created successfully'})
        return render(request, 'notification_create.html')
    return redirect('login')
@csrf_exempt
def update_notification(request, notification_id):
    if 'username' in request.session:
        notification = get_object_or_404(Notification, pk=notification_id)

        if request.method == 'POST':
            category = request.POST.get('category')
            title = request.POST.get('title')
            description = request.POST.get('description')
            file = request.FILES.get('file')

            # Update the notification attributes
            notification.category = category
            notification.title = title
            notification.description = description

            if file:
                notification.file = file

            # Save the updated notification
            notification.save()

            # Redirect to the list of notifications
            return redirect('list_notifications')

        return render(request, 'notification_update.html', {'notification': notification})
    return redirect('login')
@csrf_exempt
def delete_notification(request, notification_id):
    if 'username' in request.session:
        notification = Notification.objects.get(id=notification_id)
        notification.delete()
        return redirect('list_notifications')
        # return JsonResponse({'message': 'Notification deleted successfully'})
    return redirect('login')
def list_notifications(request):
    if 'username' in request.session:
        notifications = Notification.objects.all().order_by('-id')
        return render(request, 'notification_list.html', {'notifications': notifications})
    return redirect('login')
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            request.session['username']= username
            return redirect('list_notifications')
        else:
            print('Invalid username or password.')
            return redirect('login')
    return render(request, 'login.html')

def logout(request):
    if 'username' in request.session:
        request.session.flush()
    return redirect('login')