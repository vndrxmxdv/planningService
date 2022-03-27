from django.urls import path
from .views import api_category, api_event, api_user, api_event_detail, api_eventEntry, api_eventLeave, api_user_registration, api_getEventsByUserId, api_getEventsById
from django.contrib.auth.views import LoginView

urlpatterns = [
	path('api/category', api_category),
	path('api/events', api_event),
	path('api/events/<int:pk>', api_event_detail),
	path('api/users', api_user),
	path('api/user/eventEntry', api_eventEntry),
	path('api/user/eventLeave', api_eventLeave),
	path('api/auth/registration', api_user_registration),
	path('api/events/getEventsByUserId/<int:userId>', api_getEventsByUserId),
	path('api/events/filter=<str:id_category>', api_getEventsById),

]