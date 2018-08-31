from django.urls import path

from . import views

urlpatterns = [
    path('', views.branch_details, name='index'),
    path('branch_details/<str:ifsc>/', views.branch_details),
    path('bank/<str:bank_name>/city/<str:city>', views.all_branches)
]