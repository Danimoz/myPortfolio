from django.urls import path
from .views import (
    ListBlogView,
    ListProjectView,
    ListSkillView,
    ContactView,
    MailingListView
)

urlpatterns = [
    path('blog/', ListBlogView.as_view()),
    path('projects/<str:category>/', ListProjectView.as_view()),
    path('skills/', ListSkillView.as_view()),
    path('contact/', ContactView.as_view()),
    path('mailing-list/', MailingListView.as_view()),
]
