from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('timeline/', views.TimelineView.as_view(), name='timeline'),
    path('archive/', views.ArchiveView.as_view(), name='archive'),
    path('interviews/', views.OralHistoryInterviews.as_view(), name='interviews'),
    path('interview/<str:name>/', views.SingleOralHistoryInterview.as_view(), name='oral_history_interview'),
    path('press/', views.PressView.as_view(), name='press'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('archive/<int:row_id>/', views.ArchiveMaterialView.as_view(), name='archival_record'),
]