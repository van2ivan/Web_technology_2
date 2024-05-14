from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import Contact
from .serializer import ContactSerializer
from .permissions import IsOwner


def contact_to_json(model):
    return {'contact_name': model.contact_name, 'email': model.email, 'phone_number': model.phone_number, 'created_at': model.created_at, 'id': model.id}


class ContactList(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ContactSerializer

    def get_queryset(self):
        return Contact.objects.filter(user=self.request.user)


class ContactCreate(CreateAPIView):
    serializer_class = ContactSerializer
    permission_classes = (IsAuthenticated,)


class ContactDetail(RetrieveAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = (IsAuthenticated, IsOwner)


class EditContact(UpdateAPIView):
    queryset = Contact.objects.all()
    permission_classes = (IsAuthenticated, IsOwner)
    serializer_class = ContactSerializer


class DeleteContact(DestroyAPIView):
    queryset = Contact.objects.all()
    permission_classes = (IsAuthenticated, IsOwner)
    serializer_class = ContactSerializer
