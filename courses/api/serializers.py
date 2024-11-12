from rest_framework import serializers
from courses.models import Subject, Course, Module, Content

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'title', 'slug']  # fields to be serialized
    
class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ['order', 'title', 'description']

class CourseSerializer(serializers.ModelSerializer):
    modules = ModuleSerializer(many=True, read_only=True)
    class Meta:
        model = Course
        fields = [
            'id', 'subject', 'title', 'slug', 'overview', 'created', 'owner', 'modules'
        ]

class ItemRelatedField(serializers.RelatedField):
    def to_representation(self, value):
        return value.render()
    
class ContentSerializer(serializers.ModelSerializer):
    item = ItemRelatedField(read_only=True)
    class Meta:
        model = Content
        fields = ['item', 'order']  # fields to be serialized
        
class ModuleWithContentSerializer(serializers.ModelSerializer):
    contents = ContentSerializer(many=True)
    class Meta:
        model = Module
        fields = ['order', 'title', 'description', 'contents']
    
class CourseWithContentsSerializer(serializers.ModelSerializer):
    modules = ModuleWithContentSerializer(many=True)
    class Meta:
        model = Course
        fields = ['id', 'subject', 'title', 'slug', 'overview', 'created', 'owner', 'modules']

