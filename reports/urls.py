"""List of urls for application Journeys"""
from django.urls import include, re_path

from .views import ReportView

urlpatterns = [
    re_path(r'^totalkms_by_car/$', ReportView.as_view(report_name='Total driven kilometers by vehicle', fields_list={
            'vehicle__reg_number': 'Vehicle reg number', 'total_kms': 'Total driven'}, values_list=['vehicle__reg_number']), name='totalkms_by_car'),
    re_path(r'^totalkms_by_pass_by_car/$',
            ReportView.as_view(report_name='Total driven kilometers by vehicle & passenger', fields_list={
            'vehicle__reg_number': 'Vehicle reg number', 'passengers__username': 'passenger','total_kms': 'Total driven'}, values_list=['vehicle__reg_number', 'passengers__username']), name='totalkms_by_car_by_pass'),
    
]
