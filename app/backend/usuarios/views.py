from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import copy
from rest_framework.views import APIView
from . import models
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework import generics

