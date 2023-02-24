from django.urls import path,include
from .views import TaskList,TaskDetail,TaskCreate,TaskUpdate,TaskDelete,CustomLoginView

urlpatterns = [
    path('login/',CustomLoginView.as_view(),name='login'),
    path('',TaskList.as_view(),name='tasks'),
    path('task/<int:pk>/',TaskDetail.as_view(),name='task'),
    path('create-task/',TaskCreate.as_view(), name='create'), 
    path('update-task/<int:pk>/',TaskUpdate.as_view(), name='update'),
        path('delete-task/<int:pk>/',TaskDelete.as_view(), name='delete'),
    
]
