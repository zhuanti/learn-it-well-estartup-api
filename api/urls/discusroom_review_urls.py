from django.urls import path

from api.views.discusroom_review_views import *


app_name = 'discusroom'

urlpatterns = [
    path('all/', get_all_reviews),
    # path('get/<int:pk>/', get_review),
    # path('get_critic_reviews/', get_critic_reviews),
]