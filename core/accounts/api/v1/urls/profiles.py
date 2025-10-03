from django.urls import path, include
from .. import views

urlpatterns = [
    # Profile
    path("", views.ProfileApiView.as_view(), name="profile")
]
