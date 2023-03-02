from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='index'),
    path('delete/<int:task_id>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('cbvindex/',views.TaskListView.as_view(),name='cbvindex'),
    path('cbvdetail/<int:pk>/',views.TaskDetailView.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:pk>/',views.TaskUpdateView.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.TaskDeleteView.as_view(),name='cbvdelete')
]