from django.shortcuts import render, redirect ,get_object_or_404
from .models import Employee
from .models import Department
from .models import Event
from .models import News,NewsImage
from .models import Notification
from .models import Activity
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
def faculty(request, dept):
    department = get_object_or_404(Department, pk=dept)  # Fetch department by ID
    employees = Employee.objects.filter(department=dept)
    activities = Activity.objects.filter(department=dept)
    return render(request, 'faculty.html', {'employees': employees, 'depart': department.name, "description":department.description, 'activities': activities})

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
    return render(request, "statement.html")
def minutes(request):
    return render(request, "minutes.html")
def aishe(request):
    return render(request, "aishe.html")
def aqar(request):
    return render(request, "aqar.html")
def iqac_activities(request):
    return render(request, "iqac_activities.html")
def best_practice(request):
    return render(request, "best_practice.html")
def student_satisfaction(request):
    return render(request, "student_satisfaction.html")
    return render(request, "best_practice.html")
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

# def delete_department(request, pk):
#     """Delete a department and its associated image."""
#     if 'username' in request.session:
#         try:
#             department = get_object_or_404(Department, id=pk)

#             # Delete associated photo if it exists
#             if department.photo:
#                 photo_path = department.photo.path  # Get the full file path
#                 if os.path.isfile(photo_path):  # Ensure file exists before deleting
#                     default_storage.delete(photo_path)

#             department.delete()  # Delete department after removing photo
#             return redirect('department_list')

#         except Exception as e:
#             print(f"Error deleting department {pk}: {e}")
#             return redirect('department_list')

#     return redirect('login')
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
# def create_employee(request):
#     if 'username' in request.session:
#         if request.method == 'POST':
#             try:
#                 # First check if a file was uploaded
#                 if 'photo' not in request.FILES:
#                     return render(request, 'create_employee.html', 
#                                 {'error': 'Please upload a photo'})
                
#                 photo = request.FILES['photo']
                
#                 # Validate file type
#                 if not photo.content_type.startswith('image/'):
#                     return render(request, 'create_employee.html', 
#                                 {'error': 'Please upload a valid image file'})
                
#                 # Check file size (e.g., max 5MB)
#                 if photo.size > 5 * 1024 * 1024:  # 5MB in bytes
#                     return render(request, 'create_employee.html', 
#                                 {'error': 'Photo size should be less than 5MB'})
                
#                 # If all checks pass, compress the photo
#                 try:
#                     compressed_photo = compress_image(photo)
#                 except Exception as e:
#                     return render(request, 'create_employee.html', 
#                                 {'error': f'Error processing photo: {str(e)}'})
                
#                 # Continue with creating employee...
#                 employee = Employee(
#                     name=request.POST.get('name'),
#                     position=request.POST.get('position'),
#                     photo=compressed_photo,
#                     qualification=request.POST.get('qualification'),
#                     department=request.POST.get('department')
#                 )
#                 employee.save()
                
#                 return redirect('employee_list')
                
#             except Exception as e:
#                 return render(request, 'create_employee.html', 
#                             {'error': f'Error creating employee: {str(e)}'})
#         department_list = Department.objects.all()
#         return render(request, 'create_employee.html', {"departments":department_list})
#     return redirect('login')
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
# def update_employee(request, employee_id):
#     if 'username' in request.session:
#         employee = get_object_or_404(Employee, pk=employee_id)
#         department_list = Department.objects.all()
#         if request.method == 'POST':
#             name = request.POST.get('name')
#             position = request.POST.get('position')
#             photo = request.FILES.get('photo')
#             qualification = request.POST.get('qualification')
#             department = request.POST.get('department')
#             employee.name = name
#             employee.position = position
#             employee.department = department
#             employee.qualification = qualification
#             if 'photo' in request.FILES:
#                         photo = request.FILES['photo']
                        
#                         # Validate file type
#                         if not photo.content_type.startswith('image/'):
#                             return render(request, 'update_employee.html', 
#                                         {'employee': employee, 
#                                         'error': 'Please upload a valid image file'})
                        
#                         # Check file size (max 5MB)
#                         if photo.size > 5 * 1024 * 1024:
#                             return render(request, 'update_employee.html', 
#                                         {'employee': employee, 
#                                         'error': 'Photo size should be less than 5MB'})
                        
#                         try:
#                             # Delete old photo first
#                             delete_old_photo(employee)
#                             # Compress and save new photo
#                             compressed_photo = compress_image(photo)
#                             employee.photo = compressed_photo
#                         except Exception as e:
#                             return render(request, 'update_employee.html', 
#                                         {'employee': employee, 
#                                         'error': f'Error processing photo: {str(e)}'})
#             employee.save()
#             return redirect('employee_list')
#         return render(request, 'update_employee.html', {'employee': employee, "departments":department_list})
#     return redirect('login')

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

# def create_activity(request):
#     if 'username' in request.session:
#         if request.method == 'POST':
#             try:
#                 # Debugging: Check incoming data
#                 print("POST Data:", request.POST)
#                 print("FILES Data:", request.FILES)

#                 # First check if a file was uploaded
#                 if 'photo' not in request.FILES:
#                     return render(request, 'create_activity.html', 
#                                   {'error': 'Please upload a photo'})
                
#                 photo = request.FILES['photo']
                
#                 # Validate file type
#                 if not photo.content_type.startswith('image/'):
#                     return render(request, 'create_activity.html', 
#                                   {'error': 'Please upload a valid image file'})
                
#                 # Check file size (e.g., max 5MB)
#                 if photo.size > 5 * 1024 * 1024:  # 5MB in bytes
#                     return render(request, 'create_activity.html', 
#                                   {'error': 'Photo size should be less than 5MB'})
                
#                 # Compress the photo
#                 try:
#                     compressed_photo = compress_image(photo)
#                 except Exception as e:
#                     print(f"Error compressing image: {e}")
#                     return render(request, 'create_activity.html', 
#                                   {'error': f'Error processing photo: {str(e)}'})

#                 # Create Activity object
#                 activity = Activity(
#                     name=request.POST.get('name'),  # Ensure this matches your form input
#                     photo=compressed_photo,
#                     department=request.POST.get('department')
#                 )
#                 activity.save()
#                 print("Activity saved successfully!")

#                 return redirect('activity_list')
                
#             except Exception as e:
#                 print(f"Error creating activity: {e}")
#                 return render(request, 'create_activity.html', 
#                               {'error': f'Error creating activity: {str(e)}'})
        
#         # Load departments for dropdown
#         department_list = Department.objects.all()
#         return render(request, 'create_activity.html', {"departments": department_list})
#     return redirect('login')
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

def update_activity(request, pk):  # Make sure pk matches the URL
    activity = get_object_or_404(Activity, pk=pk)  # Get the activity object

    if request.method == 'POST':
        activity.name = request.POST.get('name')
        activity.department = request.POST.get('department')
        
        if 'photo' in request.FILES:
            photo = request.FILES['photo']
            activity.photo = photo
        
        activity.save()
        return redirect('activity_list')

    department_list = Department.objects.all()
    return render(request, 'update_activity.html', {'activity': activity, 'departments': department_list})

def delete_activity(request, pk):  # Ensure `pk` is a parameter
    activity = get_object_or_404(Activity, pk=pk)  # Fetch the activity
    activity.delete()  # Delete the activity
    return redirect('activity_list')  # Redirect to the activity list

# def delete_activity(request, activity_id):
#     if 'username' in request.session:
#         activity = get_object_or_404(Activity, pk=activity_id)
#         activity.delete()
#         delete_old_photo(activity)
#         return redirect('activity_list')
#     return redirect('login')


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