from django.shortcuts import render, redirect ,get_object_or_404
from .models import Employee
from .models import Department
from .models import Event
from .models import News,NewsImage
from .models import Notification
from .models import Exam
from .models import NSSPhoto
from .models import Activity
from .models import ActivityPhoto
from .models import IQACMember
from .models import IQACMinute
from .models import StatementCompliance
from .models import AQAR, AQARReport
from .models import AISHE
from .models import BestPractice
from .models import StudentSatisfaction
from .models import AcademicCalendar
from .models import Feedback
from datetime import datetime
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

    # Sort employees by seniority date (oldest first), fallback to nulls last
    employees = Employee.objects.filter(department=department).order_by('seniority', 'name')

    activities = Activity.objects.filter(department=department)

    return render(request, 'faculty.html', {
        'employees': employees,
        'depart': department.name,
        'description': department.description,
        'activities': activities
    })

# def staff_detail(request, employee_id):
#     employee = get_object_or_404(Employee, id=employee_id)
#     return render(request, 'staff_department.html', {'employee': employee})
def staff_detail(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    from_faculty = request.GET.get('from_faculty') == '1'  # Reads ?from_faculty=1
    return render(request, 'staff_department.html', {
        'employee': employee,
        'from_faculty': from_faculty,
    })

def club(request):
    # employees = Employee.objects.all()
    photos = NSSPhoto.objects.all().order_by('-uploaded_at')
    return render(request, 'nss.html', {'photos': photos})
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

def rusa(request):
    return render(request, 'rusa.html')

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
    # Define custom sort order for office staff positions
    position_order = {
        "Senior Superintendent": 1,
        "Head Accountant": 2,
        "Clerk": 3,
        "Librarian": 4,
        "Office Staff": 5,  # Default position for office staff
    }

    # Get all office staff members
    office_staff = Employee.objects.filter(position__in=position_order.keys())

    # Sort the employees by the defined order
    office_staff = sorted(office_staff, key=lambda emp: position_order.get(emp.position, 999))

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

def ewyl(request):
    return render(request, 'ewyl.html')

def grievance_redressal(request):
    return render(request, 'grievance_redressal.html')

def endowments(request):
    return render(request, 'endowments.html')

def feedback(request):
    feedbacks = Feedback.objects.all().order_by('-id')
    return render(request, 'feedback.html', {'feedbacks': feedbacks})

def code_of_conduct(request):
    return render(request, 'code_of_conduct.html')

def jeevani(request):
    return render(request, 'jeevani.html')


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
# def create_employee(request):
#     if 'username' in request.session:  # Ensure the user is logged in
#         if request.method == 'POST':
#             try:
#                 # Validate name and position fields
#                 name = request.POST.get('name', '').strip()
#                 position = request.POST.get('position', '').strip()
#                 qualification = request.POST.get('qualification', '').strip()
#                 department_id = request.POST.get('department')

#                 if not name or not position or not qualification or not department_id:
#                     return render(request, 'create_employee.html', 
#                                   {'error': 'All fields are required'})

#                 # Validate department
#                 try:
#                     department = Department.objects.get(id=department_id)
#                 except ObjectDoesNotExist:
#                     return render(request, 'create_employee.html', 
#                                   {'error': 'Invalid department selected'})

#                 # Validate and compress photo
#                 if 'photo' not in request.FILES:
#                     return render(request, 'create_employee.html', 
#                                   {'error': 'Please upload a photo'})

#                 photo = request.FILES['photo']
                
#                 if not photo.content_type.startswith('image/'):
#                     return render(request, 'create_employee.html', 
#                                   {'error': 'Please upload a valid image file'})

#                 if photo.size > 5 * 1024 * 1024:  # 5MB size limit
#                     return render(request, 'create_employee.html', 
#                                   {'error': 'Photo size should be less than 5MB'})

#                 # Compress the photo
#                 try:
#                     compressed_photo = compress_image(photo)
#                 except Exception as e:
#                     return render(request, 'create_employee.html', 
#                                   {'error': f'Error processing photo: {str(e)}'})

#                 # Save employee record
#                 employee = Employee(
#                     name=name,
#                     position=position,
#                     photo=compressed_photo,
#                     qualification=qualification,
#                     department=department
#                 )
#                 employee.save()

#                 return redirect('employee_list')

#             except Exception as e:
#                 return render(request, 'create_employee.html', 
#                               {'error': f'Error creating employee: {str(e)}'})

#         # Fetch departments for dropdown
#         department_list = Department.objects.all()
#         return render(request, 'create_employee.html', {"departments": department_list})

#     return redirect('login')
def create_employee(request):
    if 'username' in request.session:  # Ensure the user is logged in
        if request.method == 'POST':
            try:
                # Required fields
                name = request.POST.get('name', '').strip()
                position = request.POST.get('position', '').strip()
                qualification = request.POST.get('qualification', '').strip()

                # Check if qualification is required based on position
                non_required_positions = [
                    "Senior Superintendent",
                    "Head Accountant",
                    "Clerk",
                    "Librarian",
                    "Office Staff"
                ]

                # If position is not in non-required positions, qualification is required
                if position not in non_required_positions and not qualification:
                    department_list = Department.objects.all()
                    return render(request, 'create_employee.html', {
                        'departments': department_list,
                        'error': 'Qualification is required for this position.'
                    })

                # Optional fields
                department_id = request.POST.get('department', None)
                total_work_experience = request.POST.get('total_work_experience', '').strip()
                seminars_conferences_organised = request.POST.get('seminars_conferences_organised', '').strip()
                publications = request.POST.get('publications', '').strip()
                books_published = request.POST.get('books_published', '').strip()
                papers_presented = request.POST.get('papers_presented', '').strip()
                awards_honours = request.POST.get('awards_honours', '').strip()
                personal_webpage = request.POST.get('personal_webpage', '').strip() or None
                additional_responsibilities = request.POST.get('additional_responsibilities', '').strip()
                phd_mphil_projects_guided = request.POST.get('phd_mphil_projects_guided', '').strip()
                major_minor_projects = request.POST.get('major_minor_projects', '').strip()
                seniority = request.POST.get('seniority', '').strip() or None

                # Validate required fields
                if not name or not position:
                    department_list = Department.objects.all()
                    return render(request, 'create_employee.html', {
                        'departments': department_list,
                        'error': 'Name and Position are required.'
                    })

                # Optional department
                department = None
                if department_id:
                    try:
                        department = Department.objects.get(id=department_id)
                    except ObjectDoesNotExist:
                        return render(request, 'create_employee.html', {
                            'error': 'Invalid department selected',
                            'departments': Department.objects.all()
                        })

                # Optional photo
                photo = None
                if 'photo' in request.FILES:
                    uploaded_photo = request.FILES['photo']
                    if not uploaded_photo.content_type.startswith('image/'):
                        return render(request, 'create_employee.html', {
                            'error': 'Please upload a valid image file',
                            'departments': Department.objects.all()
                        })
                    if uploaded_photo.size > 5 * 1024 * 1024:
                        return render(request, 'create_employee.html', {
                            'error': 'Photo size should be less than 5MB',
                            'departments': Department.objects.all()
                        })

                    try:
                        photo = compress_image(uploaded_photo)
                    except Exception as e:
                        return render(request, 'create_employee.html', {
                            'error': f'Error processing photo: {str(e)}',
                            'departments': Department.objects.all()
                        })

                # Seniority date handling
                seniority_date = None
                if seniority:
                    try:
                        seniority_date = datetime.strptime(seniority, "%Y-%m-%d").date()
                    except ValueError:
                        return render(request, 'create_employee.html', {
                            'error': 'Invalid seniority date format.',
                            'departments': Department.objects.all()
                        })
                    
                # Save Employee
                employee = Employee(
                    name=name,
                    position=position,
                    photo=photo,
                    qualification=qualification,
                    department=department,
                    total_work_experience=total_work_experience,
                    seminars_conferences_organised=seminars_conferences_organised,
                    publications=publications,
                    books_published=books_published,
                    papers_presented=papers_presented,
                    awards_honours=awards_honours,
                    personal_webpage=personal_webpage,
                    additional_responsibilities=additional_responsibilities,
                    phd_mphil_projects_guided=phd_mphil_projects_guided,
                    major_minor_projects=major_minor_projects,
                    seniority=seniority_date,
                )
                employee.save()

                return redirect('employee_list')

            except Exception as e:
                return render(request, 'create_employee.html', {
                    'error': f'Error creating employee: {str(e)}',
                    'departments': Department.objects.all()
                })

        # GET method: show form
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
                # Required fields
                name = request.POST.get('name', '').strip()
                position = request.POST.get('position', '').strip()
                qualification = request.POST.get('qualification', '').strip()

                # Conditional requirement for qualification
                non_required_positions = [
                    "Senior Superintendent",
                    "Head Accountant",
                    "Clerk",
                    "Librarian",
                    "Office Staff"
                ]
                if position not in non_required_positions and not qualification:
                    return render(request, 'update_employee.html', {
                        'employee': employee,
                        'departments': department_list,
                        'error': 'Qualification is required for this position.'
                    })

                if not name or not position:
                    return render(request, 'update_employee.html', {
                        'employee': employee,
                        'departments': department_list,
                        'error': 'Name and Position are required.'
                    })

                # Update core fields
                employee.name = name
                employee.position = position
                employee.qualification = qualification if qualification else None

                # Department (optional)
                department_id = request.POST.get('department')
                if department_id:
                    try:
                        employee.department = Department.objects.get(id=department_id)
                    except ObjectDoesNotExist:
                        return render(request, 'update_employee.html', {
                            'employee': employee,
                            'departments': department_list,
                            'error': 'Invalid department selected'
                        })
                else:
                    employee.department = None

                # Photo (optional)
                if 'photo' in request.FILES:
                    photo = request.FILES['photo']
                    if not photo.content_type.startswith('image/'):
                        return render(request, 'update_employee.html', {
                            'employee': employee,
                            'departments': department_list,
                            'error': 'Please upload a valid image file'
                        })
                    if photo.size > 5 * 1024 * 1024:
                        return render(request, 'update_employee.html', {
                            'employee': employee,
                            'departments': department_list,
                            'error': 'Photo size should be less than 5MB'
                        })
                    try:
                        delete_old_photo(employee)
                        compressed_photo = compress_image(photo)
                        employee.photo = compressed_photo
                    except Exception as e:
                        return render(request, 'update_employee.html', {
                            'employee': employee,
                            'departments': department_list,
                            'error': f'Error processing photo: {str(e)}'
                        })
                elif not employee.photo:
                    from django.core.files import File
                    import os

                    dummy_path = os.path.join(settings.BASE_DIR, 'static/assets/dummy_employee.jpeg')
                    if os.path.exists(dummy_path):
                        with open(dummy_path, 'rb') as f:
                            employee.photo.save('default_photo.jpeg', File(f), save=False)

                # Optional fields
                employee.total_work_experience = request.POST.get('total_work_experience', '').strip() or None
                employee.seminars_conferences_organised = request.POST.get('seminars_conferences_organised', '').strip() or None
                employee.publications = request.POST.get('publications', '').strip() or None
                employee.books_published = request.POST.get('books_published', '').strip() or None
                employee.papers_presented = request.POST.get('papers_presented', '').strip() or None
                employee.awards_honours = request.POST.get('awards_honours', '').strip() or None
                employee.personal_webpage = request.POST.get('personal_webpage', '').strip() or None
                employee.additional_responsibilities = request.POST.get('additional_responsibilities', '').strip() or None
                employee.phd_mphil_projects_guided = request.POST.get('phd_mphil_projects_guided', '').strip() or None
                employee.major_minor_projects = request.POST.get('major_minor_projects', '').strip() or None
                seniority = request.POST.get('seniority', '').strip() or None
                if seniority:
                    try:
                        employee.seniority = datetime.strptime(seniority, "%Y-%m-%d").date()
                    except ValueError:
                        return render(request, 'update_employee.html', {
                            'employee': employee,
                            'departments': department_list,
                            'error': 'Invalid seniority date format.'
                        })
                else:
                    employee.seniority = None

                # Save changes
                employee.save()

                return redirect('employee_list')

            except Exception as e:
                return render(request, 'update_employee.html', {
                    'employee': employee,
                    'departments': department_list,
                    'error': f'Error updating employee: {str(e)}'
                })

        return render(request, 'update_employee.html', {
            'employee': employee,
            'departments': department_list
        })

    return redirect('login')
# def update_employee(request, employee_id):
#     if 'username' in request.session:
#         employee = get_object_or_404(Employee, pk=employee_id)
#         department_list = Department.objects.all()

#         if request.method == 'POST':
#             try:
#                 # Get form data
#                 name = request.POST.get('name', '').strip()
#                 position = request.POST.get('position', '').strip()
#                 qualification = request.POST.get('qualification', '').strip()
#                 department_id = request.POST.get('department')

#                 # Ensure all fields are filled
#                 if not name or not position or not qualification or not department_id:
#                     return render(request, 'update_employee.html', 
#                                   {'employee': employee, 'departments': department_list, 
#                                    'error': 'All fields are required'})

#                 # Convert department_id to Department object
#                 try:
#                     department = Department.objects.get(id=department_id)
#                 except ObjectDoesNotExist:
#                     return render(request, 'update_employee.html', 
#                                   {'employee': employee, 'departments': department_list, 
#                                    'error': 'Invalid department selected'})

#                 # Update employee fields
#                 employee.name = name
#                 employee.position = position
#                 employee.qualification = qualification
#                 employee.department = department  # ✅ Assign Department object, not ID

#                 # Handle photo update
#                 if 'photo' in request.FILES:
#                     photo = request.FILES['photo']
                    
#                     # Validate file type
#                     if not photo.content_type.startswith('image/'):
#                         return render(request, 'update_employee.html', 
#                                       {'employee': employee, 'departments': department_list, 
#                                        'error': 'Please upload a valid image file'})

#                     # Check file size (max 5MB)
#                     if photo.size > 5 * 1024 * 1024:
#                         return render(request, 'update_employee.html', 
#                                       {'employee': employee, 'departments': department_list, 
#                                        'error': 'Photo size should be less than 5MB'})

#                     try:
#                         # Delete old photo first
#                         delete_old_photo(employee)
#                         # Compress and save new photo
#                         compressed_photo = compress_image(photo)
#                         employee.photo = compressed_photo
#                     except Exception as e:
#                         return render(request, 'update_employee.html', 
#                                       {'employee': employee, 'departments': department_list, 
#                                        'error': f'Error processing photo: {str(e)}'})

#                 # Save updated employee
#                 employee.save()
#                 return redirect('employee_list')

#             except Exception as e:
#                 return render(request, 'update_employee.html', 
#                               {'employee': employee, 'departments': department_list, 
#                                'error': f'Error updating employee: {str(e)}'})

#         return render(request, 'update_employee.html', 
#                       {'employee': employee, 'departments': department_list})

#     return redirect('login')

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
            department_id = request.POST.get('department')
            department = get_object_or_404(Department, id=department_id)

            activity = Activity.objects.create(
                name=request.POST.get('name'),
                department=department
            )

            for photo_file in request.FILES.getlist('photos'):
                if photo_file.content_type.startswith('image/') and photo_file.size <= 5 * 1024 * 1024:
                    compressed = compress_image(photo_file)
                    ActivityPhoto.objects.create(activity=activity, photo=compressed)

            return redirect('activity_list')

        departments = Department.objects.all()
        return render(request, 'create_activity.html', {'departments': departments})

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
        activity = get_object_or_404(Activity, id=activity_id)
        departments = Department.objects.all()

        if request.method == 'POST':
            activity.name = request.POST.get('name')
            department_id = request.POST.get('department')
            activity.department = get_object_or_404(Department, id=department_id)
            activity.save()

            # Delete selected photos
            delete_ids = request.POST.getlist('delete_photos')
            ActivityPhoto.objects.filter(id__in=delete_ids, activity=activity).delete()

            # Add new photos
            for photo_file in request.FILES.getlist('photos'):
                if photo_file.content_type.startswith('image/') and photo_file.size <= 5 * 1024 * 1024:
                    compressed = compress_image(photo_file)
                    ActivityPhoto.objects.create(activity=activity, photo=compressed)

            return redirect('activity_list')

        return render(request, 'update_activity.html', {
            'activity': activity,
            'departments': departments,
        })

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
            # Update the text fields
            article.title = request.POST['title']
            article.description = request.POST['description']

            # Delete selected photos
            delete_ids = request.POST.getlist('delete_photos')
            if delete_ids:
                NewsImage.objects.filter(id__in=delete_ids, news_article=article).delete()

            # Handle new images
            for image_file in request.FILES.getlist('photos'):
                if image_file.content_type.startswith('image/') and image_file.size <= 5 * 1024 * 1024:
                    compressed_image = compress_image(image_file)
                    NewsImage.objects.create(
                        news_article=article,
                        image=compressed_image
                    )

            article.save()
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

#Feedback


def feedback_list(request):
    if 'username' in request.session:
        feedbacks = Feedback.objects.all().order_by('-id')
        return render(request, 'feedback_list.html', {'feedbacks': feedbacks})
    return redirect('login')

def create_feedback(request):
    if 'username' in request.session:
        if request.method == 'POST':
            name = request.POST['name']
            pdf = request.FILES['pdf']
            Feedback.objects.create(name=name, pdf=pdf)
            return redirect('feedback_list')
        return render(request, 'create_feedback.html')
    return redirect('login')

def update_feedback(request, pk):
    if 'username' in request.session:
        feedback = get_object_or_404(Feedback, pk=pk)
        if request.method == 'POST':
            feedback.name = request.POST['name']
            if 'pdf' in request.FILES:
                feedback.pdf = request.FILES['pdf']
            feedback.save()
            return redirect('feedback_list')
        return render(request, 'update_feedback.html', {'feedback': feedback})
    return redirect('login')

def delete_feedback(request, pk):
    if 'username' in request.session:
        feedback = get_object_or_404(Feedback, pk=pk)
        feedback.delete()
        return redirect('feedback_list')
    return redirect('login')

#Exam
def create_exam(request):
    if 'username' in request.session:
        if request.method == 'POST':
            category = request.POST.get('category')
            title = request.POST.get('title')
            # time = request.POST.get('time')
            # date = request.POST.get('date')
            description = request.POST.get('description')
            file = request.FILES.get('file')

            Exam.objects.create(category=category, title=title, description=description, file=file)
            return redirect('list_exams')
        return render(request, 'exam_create.html')
    return redirect('login')

def update_exam(request, exam_id):
    if 'username' in request.session:
        exam = get_object_or_404(Exam, pk=exam_id)
        if request.method == 'POST':
            exam.category = request.POST.get('category')
            exam.title = request.POST.get('title')
            # exam.time = request.POST.get('time')
            # exam.date = request.POST.get('date')
            exam.description = request.POST.get('description')
            if 'file' in request.FILES:
                exam.file = request.FILES['file']
            exam.save()
            return redirect('list_exams')
        return render(request, 'exam_update.html', {'exam': exam})
    return redirect('login')

def delete_exam(request, exam_id):
    if 'username' in request.session:
        exam = get_object_or_404(Exam, pk=exam_id)
        exam.delete()
        return redirect('list_exams')
    return redirect('login')

def list_exams(request):
    if 'username' in request.session:
        exams = Exam.objects.all().order_by('-id')
        return render(request, 'exam_list.html', {'exams': exams})
    return redirect('login')

# Frontend
def exam(request):
    exams = Exam.objects.all().order_by('-id')
    return render(request, 'exam2.html', {'exams': exams, 'cat': 'all'})

def examfilter(request, upg):
    exams = Exam.objects.filter(category=upg).order_by('-id')
    return render(request, 'exam2.html', {'exams': exams, 'cat': upg})

def exam2(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)
    return render(request, 'exam.html', {'exam': exam})

#NSSPhoto
def nss_photo_list(request):
    photos = NSSPhoto.objects.all().order_by('-uploaded_at')
    return render(request, 'nss_photo_list.html', {'photos': photos})

def nss_photo_create(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']
        NSSPhoto.objects.create(image=image)
        return redirect('nss_photo_list')
    return render(request, 'nss_photo_create.html', {'photo': None})

def nss_photo_update(request, photo_id):
    photo = get_object_or_404(NSSPhoto, id=photo_id)
    if request.method == 'POST' and request.FILES.get('image'):
        photo.image.delete()  # delete old file from media
        photo.image = request.FILES['image']
        photo.save()
        return redirect('nss_photo_list')
    return render(request, 'nss_photo_update.html', {'photo': photo})

def nss_photo_delete(request, photo_id):
    photo = get_object_or_404(NSSPhoto, id=photo_id)
    if request.method == 'POST':
        photo.image.delete()  # delete file from media folder
        photo.delete()
        return redirect('nss_photo_list')
    return redirect('nss_photo_list')

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