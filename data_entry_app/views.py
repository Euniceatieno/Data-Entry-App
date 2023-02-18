from rest_framework import generics
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from .serializers import (
    HealthInstitutionSerializer,
    ProfessionSerializer,
    EventSerializer,
    RegisterSerializer,
)
from .utils import BaseCRUDAPIController, filter_records
from .models import HealthInstitution, Profession, Event
from rest_framework.permissions import AllowAny
from rest_framework.authentication import TokenAuthentication


###############################################################
# Register API View
###############################################################
class RegisterUserAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


###############################################################
# Health Institution API View
###############################################################
class HealthInstitutionController(BaseCRUDAPIController):
    model = HealthInstitution
    serializer = HealthInstitutionSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)


def filter_health_institutions(request):
    result = filter_records(request, HealthInstitution, HealthInstitutionSerializer)
    return result


###############################################################
# Profession API View
###############################################################
class ProfessionController(BaseCRUDAPIController):
    model = Profession
    serializer = ProfessionSerializer


def filter_professions(request):
    result = filter_records(request, Profession, ProfessionSerializer)
    return result


###############################################################
# Event API View
###############################################################
class EventController(BaseCRUDAPIController):
    model = Event
    serializer = EventSerializer


def filter_events(request):
    result = filter_records(request, Event, EventSerializer)
    return result
