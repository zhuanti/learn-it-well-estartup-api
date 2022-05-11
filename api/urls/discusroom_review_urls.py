from django.urls import path

from api.views.book_review_views import *


app_name = 'book_review'

urlpatterns = [
    path('all/', get_all_reviews),
    path('get/<int:pk>/', get_review),
    # path('get_critic_reviews/', get_critic_reviews),
]