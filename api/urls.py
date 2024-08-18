from django.urls import path
from . import views
urlpatterns=[
    path("users", views.UsersListCreate.as_view(), name="users"),
    path("users/<int:pk>/", views.UserUpdateDelete.as_view(), name="update")
]