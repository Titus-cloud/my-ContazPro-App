from rest_framework import serializers
from .models import SubscriptionPlan, CustomUser, UseProfile, Category, Contact


# Creating serializers
class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionPlan
        fields = ["id", "name", "max_contacts"]


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "first_name", "last_name", "email", "password"]


class UseProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UseProfile
        fields = ["id", "user", "profile"]


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "gender",
            "date_added",
            "birthday",
            "address",
            "image",
            "category",
            "owner",
        ]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["category_name"]
