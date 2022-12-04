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
    path('reportweek/', get_report_week),
    path('reportday/', get_report_day),
    path('addbase/', add_report_week)
    # path('day/', get_day),
    # path('wdate/', get_week),
    # path('countnum/', get_countnum_reviews)
    # path('reportplanday/', get_plan_day),
    # path('reportplanweek/', get_plan_week),
    # path('reportdayin/', get_chartreport_day),
    # path('reportweekin/', get_chartreport_week),
    # 學姊的範例測試
    # path('get/<int:pk>/', get_review),
    # path('get_critic_reviews/', get_critic_reviews),
]
