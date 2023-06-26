from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import QAViewSet,TestViewSet,Testing_for_errorsViewSet

from home.api.v1.viewsets import (
    SignupViewSet,
    LoginViewSet,
)

router = DefaultRouter()
router.register("signup", SignupViewSet, basename="signup")
router.register("login", LoginViewSet, basename="login")
router.register('qa', QAViewSet )
router.register('testing_for_errors', Testing_for_errorsViewSet )
router.register('test', TestViewSet )

urlpatterns = [
    path("", include(router.urls)),
]
