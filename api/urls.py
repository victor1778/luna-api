from django.urls import path
from .views import MessageList, MessageDetail, UserList, UserDetail, index

urlpatterns = [
    # path('', index, name="index"),
    path('users/', UserList.as_view()),
    path('users/<uuid:pk>', UserDetail.as_view()),
    path('messages/', MessageList.as_view()),
    path('messages/<uuid:pk>', MessageDetail.as_view()),
]