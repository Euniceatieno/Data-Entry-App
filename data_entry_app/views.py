from rest_framework import generics
from rest_framework.response import Response
from .serializers import (
    HealthInstitutionSerializer,
    ProfessionSerializer,
    EventSerializer,
    RegisterSerializer,
    UserSerializer,
)
from .utils import BaseCRUDAPIController
from .models import HealthInstitution, Profession, Event


###############################################################
# Register API View
###############################################################
class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                "user": UserSerializer(
                    user, context=self.get_serializer_context()
                ).data,
                "message": "User Created Successfully.Now perform Login to get your token",
            }
        )


###############################################################
# Health Institution API View
###############################################################
class HealthInstitutionController(BaseCRUDAPIController):
    def __init__(self, model, serializer):
        super().__init__(model, serializer)
        self.model = HealthInstitution
        self.serializer = HealthInstitutionSerializer


###############################################################
# Profession API View
###############################################################
class ProfessionController(BaseCRUDAPIController):
    def __init__(self, model, serializer):
        super().__init__(model, serializer)
        self.model = Profession
        self.serializer = ProfessionSerializer


###############################################################
# Event API View
###############################################################
class HealthInstitutionController(BaseCRUDAPIController):
    def __init__(self, model, serializer):
        super().__init__(model, serializer)
        self.model = Event
        self.serializer = EventSerializer
