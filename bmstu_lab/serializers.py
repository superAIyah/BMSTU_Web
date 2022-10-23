from rest_framework import serializers
from .models import Subjects, Autors, Articles


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
        fields = ('title', 'link', "autor_id", "subject_id")
