from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView, ListView, CreateView, DeleteView, UpdateView
from .models import PostCreateCV
from .forms import CreateCVForm
from rest_framework.views import APIView
from rest_framework.response import Response

from datetime import datetime


class CreateownCV(CreateView):
    model = PostCreateCV
    form_class = CreateCVForm
    template_name = 'createyourcv.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        for x in range(20):
            print(x)
        return redirect('worksearch')

    def get_context_data(self, **kwargs, ):
        listset = []
        context = super(CreateownCV, self).get_context_data(**kwargs)
        context['listset'] = listset
        for items in range(30):
            listset.append(items)
        print(listset)
        return context