
from django.urls import path
from .import views

urlpatterns = [
    path('create/',views.create,
    name="create-page"),
    path('user-create/',views.UserCreateList.as_view(),name="user-list-create"),
    path('user-create/<int:pk>',views.USerUpdateDelete.as_view(),name="user-list-update-delete"),
]
