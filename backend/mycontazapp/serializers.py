from Rest_Frameworks import serializers
from .models import SubscriptionPlan, CustomUser, UseProfile, Category


class SubscriptionSerializer(serializers.ModelSerializer):
  class Meta:
    model = SubscriptionPlan
    fields = ['id' ,'name', 'max_contacts']


class CustomUserSerializer(serializers.ModelSerializer):
  class Meta:
    model = CustomUser
    fields = ['id', 'first_name', 'last_name', 'email', 'password']


class UseProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = UseProfile
    fields = ['id', 'user' , 'profile']


class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = ['id', 'first_name', 'last_name', 'email', 'phone_number', 'gender', 'date_added', 'birthday', 'address', 'image', 'category', 'owner']