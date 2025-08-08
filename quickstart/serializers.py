from django.contrib.auth.models import Group, User, Permission
from rest_framework import serializers


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ['id', 'name']
 
        
class GroupSerializer(serializers.ModelSerializer):
    permissions = PermissionSerializer(many=True)
    class Meta:
        model = Group
        fields = ['id', 'name', 'permissions'] 


class UserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True)
    permissions = PermissionSerializer(many=True)
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']