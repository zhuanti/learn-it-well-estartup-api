from django.urls import path

from api.views.subject_review_views import *


app_name = 'subject'

urlpatterns = [
    path('all/', get_all_reviews),  # 列表

]
