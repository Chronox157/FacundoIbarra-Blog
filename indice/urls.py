
import imp
from django.contrib import admin
from django.urls import path, include
from .views import frontpage, post_detail

urlpatterns = [
    path("", frontpage, name="frontpage"),
    path("<slug:slug>/", post_detail, name="post_detail")
]
