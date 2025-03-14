from rest_framework import serializers
from .models import Rating
from rest_framework.validators import UniqueTogetherValidator
from django.contrib.auth.models import User

