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
    path('topics/<topic_id>', views.topic, name='topic'),

    # Page for adding new topic
    path('new_topic/', views.new_topic, name='new_topic'),

    #Page for adding new entry
    path('new_entry/<topic_id>', views.new_entry, name='new_entry'),

    #Page for editing entry
    path('edit_entry/<entry_id>', views.edit_entry, name='edit_entry'),
]

