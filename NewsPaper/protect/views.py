from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext as _


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'


class Index(View):
    def get(self, request):
        string = _('Hello world')

        return HttpResponse(string)