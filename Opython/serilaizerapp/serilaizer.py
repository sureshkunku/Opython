from rest_framework import serializers
from Opythonapp.models import UserProfile
class userprofileSerilaizer(serializers.ModelSerializer):
    class Meta:
        model=UserProfile
        fields=('username','password','first_name','last_name','email','is_superuser','gender','cell','address')

class userpostserilaizer(serializers.ModelSerializer):
    class Meta:
        model=UserProfile
        fields=('username','password','first_name','last_name','email','is_superuser','cell','address')

class userputserilaizer(serializers.ModelSerializer):
    class Meta:
        model=UserProfile
        fields=('username','password','first_name','last_name','email','is_superuser')
class userdeleteserilaizer(serializers.ModelSerializer):
    class Meta:
        model=UserProfile
        fields=('username','first_name','last_name')
        extra_kwargs = {"username": {"required": False},
                    "first_name": {"required": False},
                    "last_name": {"required": False}}



