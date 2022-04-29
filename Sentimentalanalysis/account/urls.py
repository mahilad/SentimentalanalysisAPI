from django.urls import path

from . import views

urlpatterns = [
   path('', views.IndexView.as_view(), name='index'),
   path('review_sent/', views.FeedbackCreateView.as_view(), name='review_sent'),
   path('reviews/', views.ReviewsListView.as_view(), name='reviews'),
   path('reviews/<int:pk>/', views.ReviewDetailsView.as_view(), name='review_details'),
]