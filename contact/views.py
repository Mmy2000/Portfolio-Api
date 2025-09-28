from rest_framework import generics
from .models import Contact
from .serializers import ContactSerializer
from config.response import CustomResponse
from django.core.mail import send_mail
from django.conf import settings


class ContactCreateAPIView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def create(self, request, *args, **kwargs):
        # Call parent create method (saves the object)
        response = super().create(request, *args, **kwargs)

        # Get the created contact data
        contact_email = response.data.get("email")
        contact_name = response.data.get("first_name")  # adapt to your model fields
        contact_subject = response.data.get("subject")
        contact_message = response.data.get("message")

        # ✅ Send email
        if contact_email:
            send_mail(
                subject="Thank you for contacting us",
                message=(
                    f"Dear {contact_name},\n\n"
                    f"Thank you for reaching out to us. We have received your message:\n\n"
                    f"Subject: {contact_subject}\n"
                    f"Message: {contact_message}\n\n"
                    f"Our team will get back to you as soon as possible.\n\n"
                    f"Best regards,\n"
                    f"Mahmoud Yousef"
                ),
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[contact_email],
                fail_silently=False,
            )

        return CustomResponse(data=response.data,message="Your message has been submitted successfully, and a confirmation email has been sent!", status=201)
