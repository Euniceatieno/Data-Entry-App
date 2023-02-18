from django.urls import path
from data_entry_app.views import (
    EventController,
    HealthInstitutionController,
    ProfessionController,
    RegisterUserAPIView,
    filter_events,
    filter_health_institutions,
    filter_professions,
)
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Data Entry API",
        default_version="v1",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path("register", RegisterUserAPIView.as_view()),
    path(
        "api/health_institution",
        HealthInstitutionController.as_view(),
        name="create_health_institution",
    ),
    path(
        "api/profession",
        ProfessionController.as_view(),
        name="create_profession",
    ),
    path(
        "api/event",
        EventController.as_view(),
        name="create_event",
    ),
    path(
        "api/filter_events",
        filter_events,
        name="filter_events",
    ),
    path(
        "api/filter_health_institutions",
        filter_health_institutions,
        name="filter_health_institutions",
    ),
    path(
        "api/filter_professions",
        filter_professions,
        name="filter_professions",
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
