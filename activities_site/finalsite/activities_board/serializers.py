from rest_framework import serializers
from .models import Category, Event, User, Registrations
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title')

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'eventName','content','eventFormat','startTime','endTime','location','published','organizer','category')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password',)

class RegistationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registrations
        fields = ('user','event')
