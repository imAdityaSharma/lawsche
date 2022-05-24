from email import message
from pyexpat.errors import messages
from django.shortcuts import render
from .models import Message
from booking.models import Users

def chat(request):
  return render(request, 'index.html')

def room(request,room_name) :#room_name
  username = request.GET.get('username', Users.objects.get(id=1).name)
  messages = Message.objects.filter(room=room_name)[0:25]

  return render(request, 'room.html', {'room_name': room_name, 'username': username , 'messages': messages })
