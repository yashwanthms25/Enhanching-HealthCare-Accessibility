from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt





def careplus_base(request):
    return render(request, 'base.html')

def hear_from_ceo(request):
    return render(request, 'base.html')

def maven_for_patients(request):
    return render(request, 'patients.html')

def careplus_services(request):
    return render(request, 'services.html')

def request_demo(request):
    return render(request, 'video_cons.html')

def maven_for_individuals(request):
    return render(request, 'individuals.html')

def appointment(request):
    return render(request,'appoinment.html')

def form(request):
    return render(request,'roomform.html')

def room(request):
    return render(request,'room.html')



def appointment(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone = request.POST['phone']
        dob = request.POST['dob']
        address = request.POST['address']
        city = request.POST['city']
        
        email = request.POST['email']
        previous_attendance = request.POST['previous_attendance']
        

        data = f"{first_name},{last_name},{phone},{dob},{address},{city},{email},{previous_attendance},\n"

        with open('appointments.txt', 'a') as file:
            file.write(data)

        return HttpResponse('Appointment saved successfully.')

    return render(request, 'appointment.html')




def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('about')  # Replace 'base_page_url_name' with the actual URL name of your base page
    return render(request, 'individuals.html')
        #validate the user name and password here

def home(request):
    return render(request, 'base.html')

# views.py

import uuid
from django.shortcuts import render

def generate_room(request):
    room_id = str(uuid.uuid4())[:8]  # Generate a unique room ID
    return render(request, 'video_call.html', {'room_id': room_id})

# views.py

from django.shortcuts import redirect

def join_room(request, room_id):
    return render(request, 'video_call.html', {'room_id': room_id})


# views.py

from django.shortcuts import render, redirect
from django.http import Http404

def join_room(request):
    if request.method == 'POST':
        room_id = request.POST.get('room_id')
        if is_valid_room(room_id):
            return redirect('video_call', room_id=room_id)
        else:
            raise Http404("Room not found or invalid.")
    return render(request, 'join_room.html')

def is_valid_room(room_id):
    # Implement logic to validate room ID (e.g., check if the room exists)
    # You may need to query your database or perform other checks here
    return True  # Placeholder for validation logic

# views.py

from django.shortcuts import render

def video_call(request, room_id):
    # Implement your logic to render the video call page here
    return render(request, 'video_call.html', {'room_id': room_id})

from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('about')  # Replace 'base_page_url_name' with the actual URL name of your base page

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('about')  # Replace 'base_page_url_name' with the actual URL name of your base page
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def profile_view(request):
    return render(request, 'profile.html')