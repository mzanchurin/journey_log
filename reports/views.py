from django.views.generic import TemplateView
from journeys.models import Journey
from django.db.models import Sum, Func
from django.db import models


# class ReportView(ListView):
#     # model = Journey
#     template_name = 'reports/objects_list.html'
#     report_name = ''
#     fields = []

#     def get_queryset(self):
#         qs = Journey.objects.values('vehicle__reg_number').annotate(total_kms=Sum('length'))
#         return qs


class Round(Func):
    function = 'ROUND'
    template='%(function)s(%(expressions)s, 1)'

class ReportView(TemplateView):
    template_name = 'reports/objects_list.html'
    report_name = ''
    fields_list = []
    values_list = [] 

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        qs = Journey.objects.values(*self.values_list).annotate(total_kms=Round(Sum('length', output_field=models.CharField())))
        context['object_list'] = qs
        context['report_name'] = self.report_name
        context['fields_list'] = self.fields_list
        return context        