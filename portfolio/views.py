from django.core.mail import send_mail
from django.conf import settings
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Project, Blog, Skill, Newsletter
from .serializers import *

# Create your views here.
class ListProjectView(ListAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        category = self.kwargs['category']
        return Project.objects.filter(category=category).order_by('-created')[:12]

class ListBlogView(ListAPIView):
    queryset = Blog.objects.all().order_by('-created')[:12]
    serializer_class = BlogSerializer

class ListSkillView(ListAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class ContactView(APIView):
    def post(self, request):
        serializer = ContactSerializer(data = request.data)

        if serializer.is_valid():
            body = {
                'first_name' : f"{serializer.data['first_name']}",
                'last_name' : f"{serializer.data['last_name']}",
                'email': f"{serializer.data['email']}",
                'phone': f"{serializer.data['phone']}",
                'message': f"{serializer.data['message']}",
            }
            message = '\n'.join(body.values())
            
            try:
                news_check = Newsletter.objects.get(email = body['email'])
            except Newsletter.DoesNotExist:
                news_check = None

            if not news_check:
                Newsletter.objects.create(
                    email = body['email'],
                    first_name = body['first_name'],
                    last_name = body['last_name']
                )
            send_mail('Hi Daniel!, Someone wants to reach out to you',
                message,
                settings.EMAIL_HOST_USER,
                [settings.RECIPIENT_ADDRESS],
            )
            return Response({'message': 'Message sent successfully', 'data':serializer.data}, status=status.HTTP_200_OK)
        return Response({'data': serializer.errors, 'message': 'Something went wrong, Please try again later'}, status=status.HTTP_400_BAD_REQUEST)

class MailingListView(CreateAPIView):
    queryset = Newsletter.objects.all()
    serializer_class = MailingListSerializer