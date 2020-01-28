"""Defines URL patterns for learning logs"""

from django.urls import path
from . import views

app_name = 'learning_logs'

urlpatterns = [
    #Homepage
    path('', views.index, name='index'),

    # Show all topics
    path('topics/', views.topics, name='topics'),

    # detail page for single topic
    path('topics/<topic_id>', views.topic, name='topic')
]

