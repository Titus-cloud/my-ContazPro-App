from rest_framework import serializers
from .models import SubscriptionPlan, CustomUser, UseProfile, Category, Contact, CustomUser


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


# TODO This is a user registration serializers
class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'firstname', 'last_name', 'email', 'password']
        extra_fields = {'password' :{'write_only': True}}

        def create(self, validated_data):
            password = validated_data.pop('password')
            user = self.Meta.model(**validated_data)
            user.set_password(password)
            user.save()
            return user
        

# TODO Create a user login serializer
class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()