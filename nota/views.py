from django.http import HttpResponse
from django.shortcuts import render

from django.views import generic

from . import baserow

class HomeView(generic.TemplateView):
    template_name = 'home.html'

class TimelineView(generic.TemplateView):
    template_name = 'timeline.html'

class ArchiveView(generic.ListView):
    template_name = 'archive.html'
    data = baserow.get_archive_all()

    def get_context_data(self, **kwargs):
        context = super(ArchiveView, self).get_context_data(**kwargs)
        context['data'] = self.data
        return context

    def get_queryset(self, **kwargs):
        return self.data

class PressView(generic.ListView):
    template_name = 'press.html'
    data = baserow.get_press_all()

    def get_context_data(self, **kwargs):
        context = super(PressView, self).get_context_data(**kwargs)
        context['data'] = self.data
        return context

    def get_queryset(self, **kwargs):
        return self.data

class AboutView(generic.TemplateView):
    template_name = 'about.html'

class ArchiveMaterialView(generic.TemplateView):
    template_name = 'archive_material.html'

    def get_context_data(self, **kwargs):
        context = super(ArchiveMaterialView, self).get_context_data(**kwargs)
        context['data'] = baserow.get_archival_material(context['row_id'])
        return context['data']
