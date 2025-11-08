from django.urls import path
from . import views


urlpatterns = [
    path('', views.careplus_base, name='homepage'),
    path('about/', views.hear_from_ceo, name='about'),
    path('patients/', views.maven_for_patients, name='patients'),
    path('services/', views.careplus_services, name='services'),
    path('video_consulation/', views.request_demo, name='video_consulation'),
    path('individuals/', views.maven_for_individuals, name='individuals'),
    path('appointment/',views.appointment,name='appointment'),
    path('patients/roomform/',views.form,name='roomform'),
    path('patients/room/',views.room,name='room'),
    path('video_consulation/generate_room/', views.generate_room, name='generate_room'),
    path('video_consulation/join_room/', views.join_room, name='join_room'),
    path('video_consulation/video_call/<str:room_id>/', views.video_call, name='video_call'),
      path('login/', views.login_view, name='login'),
      path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('register/', views.register_view, name='register'),
        # Assuming you have a view for the video call
    # other URL patterns
]

    

