from django.http import JsonResponse
from .models import Category, Event, User, Registrations
from .serializers import CategorySerializer, EventSerializer, UserSerializer, RegistationsSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout

@api_view(['POST'])
def api_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)

@api_view(['POST'])
def api_logout(request):
    logout(request)

@api_view(['GET'])
def api_category(request):
    if request.method == 'GET':
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def api_filter_events(request):
    if request.method == 'GET':
        event = Event.objects.filter(category=2)
        event = event.filter(category=3)
        serializer = EventSerializer(event, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def api_getEventsById(request, id_category):
    tags = id_category.split("&")
    tags = [int(tags[i]) for i in range(len(tags))]
    event = Event.objects.filter(category=tags[0])

    for i in range(1, len(tags)):
        event = event.filter(category=tags[i])

    serializer = EventSerializer(event, many=True)
    return Response(serializer.data)



@api_view(['GET', 'POST'])
def api_event(request):
    if request.method == 'GET':
        event = Event.objects.all()
        serializer = EventSerializer(event, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PATCH', 'DELETE'])
def api_event_detail(request, pk):
    try:
        event = Event.objects.get(pk=pk)
        if request.method == 'GET':
            serializer = EventSerializer(event)
            return Response(serializer.data)
        elif request.method == 'PATCH':
            serializer = EventSerializer(event, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            event.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def api_user(request):
    if request.method == 'GET':
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def api_user_registration(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def api_eventEntry(request):
    if request.method == 'POST':
        serializer = RegistationsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
def api_eventLeave(request):
    if request.method == 'PATCH':
        try:
            registration = Registrations.objects.get(user=request.data['user'], event=request.data['event'])
            registration.delete()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def api_getEventsByUserId(request, userId):
    if request.method == 'GET':
        try:
            user = User.objects.get(pk=userId)
            event = user.events
            serializer = EventSerializer(event, many=True)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
