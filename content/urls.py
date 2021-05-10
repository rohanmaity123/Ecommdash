from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="Dashboard"),
    path("addcategory/", views.addcategory, name="addcategory"),
    path("managecategory/", views.managecategory, name="managecategory"),
    path("deletecategory/<str:pk>/", views.deletecategory, name="deletecategory"),
    path("getcategory/<str:pk>/", views.getcategory, name="getcategory"),
    path("editcategory/<str:pk>/", views.editcategory, name="editcategory"),
    path("addsubcategory/", views.addsubcategory, name="addsubcategory"),
    path("managesubcategory/", views.managesubcategory, name="managesubcategory"),
    path("deletesubcategory/<str:pk>/", views.deletesubcategory, name="deletesubcategory"),
]
