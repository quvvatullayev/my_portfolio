from rest_framework import serializers
from models import (
    About_me,
    Skills,
    Education,
    Experience,
    Projects,
)

class About_meSerializer(serializers.ModelSerializer):
    class Meta:
        model = About_me
        fields = '__all__'

class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = '__all__'

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'

class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'