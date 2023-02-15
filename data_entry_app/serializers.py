from rest_framework import serializers
from .models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from .models import Event, HealthInstitution, Profession


###############################################################
# Register Serializer
###############################################################
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "password", "first_name", "last_name")
        extra_kwargs = {
            "password": {"write_only": True},
        }

        def create(self, validated_data):
            user = User.objects.create_user(
                validated_data["username"],
                password=validated_data["password"],
                first_name=validated_data["first_name"],
                last_name=validated_data["last_name"],
            )
            return user


###############################################################
# Data Entry Categories Serializer
###############################################################
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ("event_name", "location", "event_data", "description")


class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = ("name", "description", "occupation")


class HealthInstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthInstitution
        fields = ("name", "phone_number", "speciality", "location")
