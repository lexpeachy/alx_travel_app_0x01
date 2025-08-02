from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from listings import views

urlpatterns = [
    path('listings/', views.ListingList.as_view()),
    path('listings/<int:pk>/', views.ListingDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)