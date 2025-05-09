from django.urls import path
from . import views

urlpatterns = [
    # ... other URL patterns
    path('', views.index, name='index'),
    path('news/<int:nw_id>/', views.news, name='news'),
    path('allnews', views.allnews, name='allnews'),
    path('events/<int:ev_id>/', views.events, name='events'),
    path('allevents', views.allevents, name='allevents'),
    # path('faculty/<str:dept>/', views.faculty, name='faculty'),
    path('faculty/<int:dept>/', views.faculty, name='faculty'),  # Accept department ID
    path('notification', views.notification, name='notification'),
    path('notification2/<int:noti_id>/', views.notification2, name='notification2'),
    path('notificationfilter/<str:upg>/', views.notificationfilter, name='notificationfilter'),

    #exam
    path('exam', views.exam, name='exam'),
    path('examfilter/<str:upg>/', views.examfilter, name='examfilter'),
    path('exam2/<int:exam_id>/', views.exam2, name='exam2'),


    # Admin exam
    path('exams/list/', views.list_exams, name='list_exams'),
    path('exams/create/', views.create_exam, name='create_exam'),
    path('exams/update/<int:exam_id>/', views.update_exam, name='update_exam'),
    path('exams/delete/<int:exam_id>/', views.delete_exam, name='delete_exam'),

    path('club', views.club, name='club'),
    path('fitness', views.fitness, name='fitness'),
    # path('about', views.about, name='about'),
    path('about-college/', views.about_college, name='about_college'),
    path('rti/', views.rti, name='rti'),
    path('cdc/', views.cdc, name='cdc'),
    path('office/', views.office, name='office'),

    #Facility
    path('academic/', views.academic_facilities, name='academic_facilities'),
    path('library/', views.library, name='library'),
    path('orice/', views.orice, name='orice'),
    path('procedures-policy/', views.procedures_policy, name='procedures_policy'),
    path('it-facility/', views.it_facility, name='it_facility'),
    path('sports/', views.sports_facility, name='sports_facility'),
    path('amenity-centre/', views.amenity_centre, name='amenity_centre'),
    path('canteen/', views.canteen, name='canteen'),
    path('womens-hostel/', views.womens_hostel, name='womens_hostel'),
    path('auditorium/', views.auditorium_seminar_halls, name='auditorium_seminar_halls'),

    #Research
    path('research-centre/', views.research_centre, name='research_centre'),
    path('research-guides/', views.research_guides, name='research_guides'),
    path('research-scholars/', views.research_scholars, name='research_scholars'),
    path('research-projects/', views.research_projects, name='research_projects'),
    path('research-journal/', views.research_journal, name='research_journal'),

    #Student Support
    path('scholarships/', views.scholarships, name='scholarships'),
    path('career-guidance/', views.career_guidance, name='career_guidance'),
    path('yip/', views.yip, name='yip'),
    path('ewyl/', views.ewyl, name='ewyl'),
    path('grievance-redressal/', views.grievance_redressal, name='grievance_redressal'),
    path('endowments/', views.endowments, name='endowments'),
    path('feedback/', views.feedback, name='feedback'),
    path('code-of-conduct/', views.code_of_conduct, name='code_of_conduct'),
    path('jeevani/', views.jeevani, name='jeevani'),

    #Feedback admin
    path('feedback_admin/', views.feedback_list, name='feedback_list'),  # Admin list
    path('feedback_admin/new/', views.create_feedback, name='create_feedback'),
    path('feedback_admin/update/<int:pk>/', views.update_feedback, name='update_feedback'),
    path('feedback_admin/delete/<int:pk>/', views.delete_feedback, name='delete_feedback'),

    path('pta',views.pta, name='pta'),
    path('rusa',views.rusa, name='rusa'),
    path('college_union',views.college_union, name='college_union'),
    path('committies',views.committies, name='committies'),
    path('clubs',views.clubs, name='clubs'),
    path('alumini', views.alumini, name='alumini'),
    path('courses', views.courses, name='courses'),
    path('admission/', views.admission, name='admission'),
    path('academic_calendar/', views.academic_calendar, name='academic_calendar'),
    path('exam-calendar/', views.exam_calendar, name='exam_calendar'),
    path('academic-results/', views.academic_results, name='academic_results'),

    path('FYUGP', views.FYUGP, name='FYUGP'),
    path('placement', views.placement, name='placement'),
    path('scholarship', views.scholarship, name='scholarship'),
    path('applicatonforms', views.applicatonforms, name='applicatonforms'),
    path('courses', views.courses, name='courses'),
    path('universityinfo', views.universityinfo, name='universityinfo'),
    path('iqac', views.iqac, name='iqac'),
    path('staffcouncil', views.staffcouncil, name='staffcouncil'),
    path('manager', views.manager, name='manager'),
    path('principal', views.principal, name="principal"),

    path('minutes', views.minutes, name="minutes"),
    path('statement', views.statement, name="statement"),
    path('aishe', views.aishe, name="aishe"),
    path('aqar', views.aqar, name="aqar"),
    path('iqac_activities', views.iqac_activities, name="iqac_activities"),
    path('best_practice', views.best_practice, name="best_practice"),
    path('student_satisfaction', views.student_satisfaction, name="student_satisfaction"),
    path('institutional_distinctiveness', views.institutional_distinctiveness, name="institutional_distinctiveness"),
    
    path('staff/<int:employee_id>/', views.staff_detail, name='staff_detail'),

    path('create_employee', views.create_employee, name='create_employee'),
    path('employee_list', views.employee_list, name='employee_list'),
    path('delete_employee/<int:employee_id>/', views.delete_employee, name='delete_employee'),
    path('update_employee/<int:employee_id>/', views.update_employee, name='update_employee'),

    path('create_department', views.create_department, name='create_department'),
    path('department_list', views.department_list, name='department_list'),
    path('delete_department/<int:pk>/', views.delete_department, name='delete_department'),
    path('update_department/<int:pk>/', views.update_department, name='update_department'),

    path('create_activity', views.create_activity, name='create_activity'),
    path('activity_list/', views.activity_list, name='activity_list'),
    path('delete_activity/<int:pk>/', views.delete_activity, name='delete_activity'),
    path('update_activity/<int:activity_id>/', views.update_activity, name='update_activity'),

    path('event/create/', views.event_create, name='event_create'),
    path('event/<int:event_id>/update/', views.event_update, name='event_update'),
    path('event/<int:event_id>/delete/', views.event_delete, name='event_delete'),
    path('events/', views.event_list, name='event_list'),  # Create a view for listing events

    path('news/', views.news_list, name='news_list'),
    path('news/create/', views.create_news, name='create_news'),
    path('news/update/<int:pk>/', views.update_news, name='update_news'),
    path('news/delete/<int:pk>/', views.delete_news, name='delete_news'),

    path('academic_calendar/list/', views.academic_calendar_list, name="academic_calendar_list"),
    path('academic_calendar/create/', views.create_academic_calendar, name="create_academic_calendar"),
    path('academic_calendar/edit/<int:id>/', views.update_academic_calendar, name="update_academic_calendar"),
    path('academic_calendar/delete/<int:id>/', views.delete_academic_calendar, name="delete_academic_calendar"),


    path("iqac_members/", views.iqac_member_list, name="iqac_member_list"),
    path("iqac_members/new/", views.create_iqac_member, name="create_iqac_member"),
    path("iqac_members/edit/<int:id>/", views.update_iqac_member, name="update_iqac_member"),
    path("iqac_members/delete/<int:id>/", views.delete_iqac_member, name="delete_iqac_member"),

    path("iqac_minutes/", views.iqac_minutes_list, name="iqac_minutes_list"),
    path("iqac_minutes/new/", views.create_iqac_minute, name="create_iqac_minute"),
    path("iqac_minutes/edit/<int:id>/", views.update_iqac_minute, name="update_iqac_minute"),
    path("iqac_minutes/delete/<int:id>/", views.delete_iqac_minute, name="delete_iqac_minute"),

    path("statement_compliance/", views.statement_compliance_list, name="statement_compliance_list"),
    path("statement_compliance/new/", views.create_statement_compliance, name="create_statement_compliance"),
    path("statement_compliance/edit/<int:id>/", views.update_statement_compliance, name="update_statement_compliance"),
    path("statement_compliance/delete/<int:id>/", views.delete_statement_compliance, name="delete_statement_compliance"),

    path('aqar_list/', views.aqar_list, name="aqar_list"),
    path('aqar/new/', views.create_aqar, name="create_aqar"),
    path('aqar/edit/<int:id>/', views.update_aqar, name="update_aqar"),
    path('aqar/delete/<int:id>/', views.delete_aqar, name="delete_aqar"),

    path('aqar_report_list/', views.aqar_report_list, name="aqar_report_list"),
    path('aqar_report/new/', views.create_aqar_report, name="create_aqar_report"),
    path('aqar_report/edit/<int:id>/', views.update_aqar_report, name="update_aqar_report"),
    path('aqar_report/delete/<int:id>/', views.delete_aqar_report, name="delete_aqar_report"),

    path("aishe/list/", views.aishe_list, name="aishe_list"),
    path("aishe/new/", views.create_aishe, name="create_aishe"),
    path("aishe/edit/<int:id>/", views.update_aishe, name="update_aishe"),
    path("aishe/delete/<int:id>/", views.delete_aishe, name="delete_aishe"),

    path('best_practice/list/', views.best_practice_list, name="best_practice_list"),
    path('best_practice/new/', views.create_best_practice, name="create_best_practice"),
    path('best_practice/edit/<int:id>/', views.update_best_practice, name="update_best_practice"),
    path('best_practice/delete/<int:id>/', views.delete_best_practice, name="delete_best_practice"),

    path("student_satisfaction/list/", views.student_satisfaction_list, name="student_satisfaction_list"),
    path("student_satisfaction/new/", views.create_student_satisfaction, name="create_student_satisfaction"),
    path("student_satisfaction/edit/<int:id>/", views.update_student_satisfaction, name="update_student_satisfaction"),
    path("student_satisfaction/delete/<int:id>/", views.delete_student_satisfaction, name="delete_student_satisfaction"),


    path('create_notification/', views.create_notification, name='create_notification'),
    path('update_notification/<int:notification_id>/', views.update_notification, name='update_notification'),
    path('delete_notification/<int:notification_id>/', views.delete_notification, name='delete_notification'),
    path('list_notifications/', views.list_notifications, name='list_notifications'),

    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),


]
