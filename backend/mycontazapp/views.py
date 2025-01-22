from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Contact, Category, SubscriptionPlan
from .serializers import (
    ContactSerializer,
    UserRegistrationSerializer,
    CategorySerializer,
    SubscriptionSerializer,
    UseProfileSerializer,
)
from rest_framework import status


class ContactView(APIView):
    def get(self, request, format=None):
        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data)

    def post(self, request, format="json"):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegisterView(APIView):
    def post(self, request, format="json"):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryView(APIView):
    def get(self, request, format=None):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)

    def post(self, request, Format=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SubscriptionPlanView(APIView):
    def get(self, request, format=None):
        plan = SubscriptionPlan.objects.all()
        serializer = SubscriptionSerializer(plan, many=True)
        return Response(serializer.data)

    def post(self, request, Format=None):
        serializer = SubscriptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UseProfile(APIView):
    def get(self, request, format=None):
        profiles = UseProfile.objects.all()
        serializer = UseProfileSerializer(profiles, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UseProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SingleContactView(APIView):
    def get_by_id(self, id):
        try:
            return Contact.objects.get(id=id)
        except Contact.DoesNotExist:
            raise  status.HTTP_400_BAD_REQUEST

    def get(self,request, id, format=None):
        contact = self.get_by_id(id)
        serializer = ContactSerializer(contact)
        return Response(serializer.data)

    def put(self, request, id, format = None):
        contact = self.get_by_id(id)
        serializer = ContactSerializer(contact, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_404_NOT_FOUND)
    
    def delete(self, required, id, format):
        contact = self.get_by_id(id)

        if contact is None:
            return Response({"error": "Contact not found"}, status=status.HTTP_404_NOT_FOUND)
        contact.delete()
        return Response({"message": "Deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

