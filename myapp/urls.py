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

    path('club', views.club, name='club'),
    path('fitness', views.fitness, name='fitness'),
    path('about', views.about, name='about'),
    path('alumini', views.alumini, name='alumini'),
    path('courses', views.courses, name='courses'),
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
    path('update_activity/<int:pk>/', views.update_activity, name='update_activity'),

    path('event/create/', views.event_create, name='event_create'),
    path('event/<int:event_id>/update/', views.event_update, name='event_update'),
    path('event/<int:event_id>/delete/', views.event_delete, name='event_delete'),
    path('events/', views.event_list, name='event_list'),  # Create a view for listing events

    path('news/', views.news_list, name='news_list'),
    path('news/create/', views.create_news, name='create_news'),
    path('news/update/<int:pk>/', views.update_news, name='update_news'),
    path('news/delete/<int:pk>/', views.delete_news, name='delete_news'),

    path('create_notification/', views.create_notification, name='create_notification'),
    path('update_notification/<int:notification_id>/', views.update_notification, name='update_notification'),
    path('delete_notification/<int:notification_id>/', views.delete_notification, name='delete_notification'),
    path('list_notifications/', views.list_notifications, name='list_notifications'),

    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),


]
