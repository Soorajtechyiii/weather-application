from django.urls import path #type:ignore
from.import views #type:ignore
urlpatterns=[
    path('pagehtml/',views.pagehtml),
    path('pagehtmll/',views.pagehtmll),
    path('index/',views.index),
    path('area/',views.area),
]