from django.urls import path

from api.views.report_review_views import *

app_name = 'report'

urlpatterns = [
    # path('all/', get_all_reviews),
    path('addsub/', addsub),
    # 下面test/ 供報表相關表格進行測試
    path('test/', get_all_reviews_test),
    path('inside/', get_reviews_insideshow),
    path('recordtime/', report_recordtime_edit),
    path('testsearch/', get_reviews_reportdata),
    path('reporttest/', get_reviews_report_test),
    path('reportweek/', get_report_usernameweek),
    # 學姊的範例測試
    # path('get/<int:pk>/', get_review),
    # path('get_critic_reviews/', get_critic_reviews),
]
