from django.urls import path
from . import views
from .views import worksearch, AddWorkView, delete_work, PlannedWork, delete_planned, EditPlanned, Get_data, UserSettings, delete_links, Editdone

urlpatterns = [

    path('', worksearch.as_view(), name="worksearch"),
    path('addwork/', AddWorkView.as_view(), name="addworkpost"),
    path('delete1/<work_id>', delete_work, name='delete_work'),
    path('planned/', PlannedWork.as_view(), name="planned_work"),
    path('data/', Get_data.as_view(), name="api-data"),
    path('delete2/<work_id2>', delete_planned, name='delete_planned'),
    path('edit/<int:pk>', EditPlanned.as_view(), name="update_planned"),
    path('editd/<int:pk>', Editdone.as_view(), name="update_done"),
    path('settings/', UserSettings.as_view(), name="user_settings"),
    path('deletelink/<links_id>', delete_links, name='delete_links'),
]