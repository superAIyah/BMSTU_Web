from rest_framework import serializers
from .models import Subjects, Autors, Articles, UserProfile
from django.contrib.auth.models import User

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username")

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subjects
        fields = ('name',)

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autors
        fields = ('name', 'family_name')

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        #fields = ('title', 'link', "autor_id", "photo", "subject_id", 'photo_link', 'subject', 'price', "id", "cart")
        fields = '__all__'
