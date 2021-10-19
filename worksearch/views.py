from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView, ListView, CreateView, DeleteView, UpdateView
from .forms import PostForm, PlannedForm, UserSettForm, PostUserForm
from rest_framework.views import APIView
from rest_framework.response import Response
from .Postapp import *
from datetime import datetime
from .models import PostUserSett, PostUserUpload


def delete_work(request, work_id):
    work2 = Post.objects.get(pk=work_id)
    work2.delete()
    return redirect('worksearch')

def delete_planned(request, work_id2):
    work1 = PostPlan.objects.get(pk=work_id2)
    work1.delete()
    return redirect('worksearch')

def delete_links(request, links_id):
    links = PostUserSett.objects.get(pk=links_id)
    links.delete()
    return redirect('user_settings')

# class cloneobject(UpdateView):
#     model = PostPlan
#     template_name = "update_done.html"
#     form_class = PostForm
#
# # def cloneobject(request, work_id2):
# #     obj_move_original = PostPlan.objects.get(pk=work_id2)
# #     obj_move_original.pk = None
# #     obj_move_original.last_app_date = datetime.now()
# #     obj_move_original.save()
# #
# #     return redirect('worksearch')
def upload_files(request):
    form = PostUserForm(request.POST or None, request.FILES or None)
    print("Form is", form)
    return redirect("user_settings")

class worksearch(ListView):
    template_name = 'userpage.html'
    queryset = Post.objects.all().order_by('-date_added')

    def get_context_data(self, **kwargs, ):
        listset = []
        context = super(worksearch, self).get_context_data(**kwargs)
        context['PostPlan'] = PostPlan.objects.all().order_by('last_app_date')
        context['Post'] = self.queryset
        context['PostUserSett'] = PostUserSett.objects.all()
        context['listset'] = listset
        today = datetime.now()
        lastday = PostPlan.objects.filter(last_app_date__year=today.year, last_app_date__month=today.month, last_app_date__day=today.day)
        context['lastday'] = lastday
        print(lastday)
        test = PostUserSett.objects.filter(user=self.request.user).only('title')
        for items in test:
            listset.append(items.title)

        return context

class AddWorkView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'addwork.html'
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return redirect('worksearch')

class PlannedWork(CreateView):
    model = PostPlan
    form_class = PlannedForm
    template_name = 'planningtoapply.html'
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return redirect('worksearch')

class UserSettings(CreateView):
    model = PostUserSett
    form_class = UserSettForm
    template_name = 'user_settings.html'
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return redirect('user_settings')

    def get_context_data(self, **kwargs, ):
        listset = []
        context = super(UserSettings, self).get_context_data(**kwargs)
        context['PostUserSett'] = PostUserSett.objects.all()
        context['PostUserUpload'] = PostUserUpload.objects.all()
        context['listset'] = listset
        test = PostUserSett.objects.filter(user=self.request.user)
        for items in test:
            listset.append(items)
        print("Form is", PostUserUpload)
        print(listset)
        return context


class EditPlanned(UpdateView):
    model = PostPlan
    template_name = "update_post.html"
    form_class = PlannedForm

class Editdone(UpdateView):
    model = Post
    template_name = "update_done.html"
    form_class = PostForm

class Get_data(APIView):
    def get(self, request, format=None):
        global user
        global data_queryset
        global data_app
        user = self.request.user
        data_queryset = Post.objects.all().filter(user=user)
        total_count = Post.objects.all().filter(user=user).count()
        if total_count != "0":
            data_queryset_plan = PostPlan.objects.all().filter(user=user)
            count_days_jan = Post.objects.filter(date_added__year="2021", date_added__month="1",
                                                 user=user).count()
            count_days_feb = Post.objects.filter(date_added__year="2021", date_added__month="2",
                                                 user=user).count()
            count_days_mars = Post.objects.filter(date_added__year="2021", date_added__month="3",
                                                  user=user).count()
            count_days_april = Post.objects.filter(date_added__year="2021", date_added__month="4",
                                                   user=user).count()
            count_days_may = Post.objects.filter(date_added__year="2021", date_added__month="5",
                                                 user=user).count()
            count_days_june = Post.objects.filter(date_added__year="2021", date_added__month="6",
                                                  user=user).count()
            count_days_july = Post.objects.filter(date_added__year="2021", date_added__month="7",
                                                  user=user).count()
            count_days_aug = Post.objects.filter(date_added__year="2021", date_added__month="8",
                                                 user=user).count()
            count_days_sep = Post.objects.filter(date_added__year="2021", date_added__month="9",
                                                 user=user).count()
            count_days_okt = Post.objects.filter(date_added__year="2021", date_added__month="10",
                                                 user=user).count()
            count_days_nov = Post.objects.filter(date_added__year="2021", date_added__month="11",
                                                 user=user).count()
            count_days_dec = Post.objects.filter(date_added__year="2021", date_added__month="12",
                                                 user=user).count()
            # antal aktiviteter uppdelade på antal annonser sökta
            work_choise_jan = Post.objects.filter(date_added__year="2021", date_added__month="1",
                                                  choises_activity="Work application", user=user).count()
            work_choise_feb = Post.objects.filter(date_added__year="2021", date_added__month="2",
                                                  choises_activity="Work application", user=user).count()
            work_choise_mars = Post.objects.filter(date_added__year="2021", date_added__month="3",
                                                  choises_activity="Work application", user=user).count()
            work_choise_april = Post.objects.filter(date_added__year="2021", date_added__month="4",
                                                  choises_activity="Work application", user=user).count()
            work_choise_may = Post.objects.filter(date_added__year="2021", date_added__month="5",
                                                  choises_activity="Work application", user=user).count()
            work_choise_june = Post.objects.filter(date_added__year="2021", date_added__month="6",
                                                  choises_activity="Work application", user=user).count()
            work_choise_july = Post.objects.filter(date_added__year="2021", date_added__month="7",
                                                  choises_activity="Work application", user=user).count()
            work_choise_aug = Post.objects.filter(date_added__year="2021", date_added__month="8",
                                                  choises_activity="Work application", user=user).count()
            work_choise_sep = Post.objects.filter(date_added__year="2021", date_added__month="9",
                                                  choises_activity="Work application", user=user).count()
            work_choise_oct = Post.objects.filter(date_added__year="2021", date_added__month="10",
                                                  choises_activity="Work application", user=user).count()
            work_choise_nov = Post.objects.filter(date_added__year="2021", date_added__month="11",
                                                  choises_activity="Work application", user=user).count()
            work_choise_dec = Post.objects.filter(date_added__year="2021", date_added__month="12",
                                                  choises_activity="Work application", user=user).count()
            # antal aktiviteter uppdelade på antal intresseanmälans
            regis_choice_jan = Post.objects.filter(date_added__year="2021", date_added__month="1",
                                                   choises_activity="Registration of interest", user=user).count()
            regis_choice_feb = Post.objects.filter(date_added__year="2021", date_added__month="2",
                                                   choises_activity="Registration of interest", user=user).count()
            regis_choice_mars = Post.objects.filter(date_added__year="2021", date_added__month="3",
                                                   choises_activity="Registration of interest", user=user).count()
            regis_choice_april = Post.objects.filter(date_added__year="2021", date_added__month="4",
                                                   choises_activity="Registration of interest", user=user).count()
            regis_choice_may = Post.objects.filter(date_added__year="2021", date_added__month="5",
                                                   choises_activity="Registration of interest", user=user).count()
            regis_choice_june = Post.objects.filter(date_added__year="2021", date_added__month="6",
                                                   choises_activity="Registration of interest", user=user).count()
            regis_choice_july = Post.objects.filter(date_added__year="2021", date_added__month="7",
                                                   choises_activity="Registration of interest", user=user).count()
            regis_choice_aug = Post.objects.filter(date_added__year="2021", date_added__month="8",
                                                   choises_activity="Registration of interest", user=user).count()
            regis_choice_sep = Post.objects.filter(date_added__year="2021", date_added__month="9",
                                                   choises_activity="Registration of interest", user=user).count()
            regis_choice_oct = Post.objects.filter(date_added__year="2021", date_added__month="10",
                                                   choises_activity="Registration of interest", user=user).count()
            regis_choice_nov = Post.objects.filter(date_added__year="2021", date_added__month="11",
                                                   choises_activity="Registration of interest", user=user).count()
            regis_choice_dec = Post.objects.filter(date_added__year="2021", date_added__month="12",
                                                   choises_activity="Registration of interest", user=user).count()
            # antal aktiviteter uppdelade på antal övriga aktiviteter
            other_choice_jan = Post.objects.filter(date_added__year="2021", date_added__month="1",
                                                   choises_activity="Other activity", user=user).count()
            other_choice_feb = Post.objects.filter(date_added__year="2021", date_added__month="2",
                                                   choises_activity="Other activity", user=user).count()
            other_choice_mars = Post.objects.filter(date_added__year="2021", date_added__month="3",
                                                   choises_activity="Other activity", user=user).count()
            other_choice_april = Post.objects.filter(date_added__year="2021", date_added__month="4",
                                                   choises_activity="Other activity", user=user).count()
            other_choice_may = Post.objects.filter(date_added__year="2021", date_added__month="5",
                                                   choises_activity="Other activity", user=user).count()
            other_choice_june = Post.objects.filter(date_added__year="2021", date_added__month="6",
                                                   choises_activity="Other activity", user=user).count()
            other_choice_july = Post.objects.filter(date_added__year="2021", date_added__month="7",
                                                   choises_activity="Other activity", user=user).count()
            other_choice_aug = Post.objects.filter(date_added__year="2021", date_added__month="8",
                                                   choises_activity="Other activity", user=user).count()
            other_choice_sep = Post.objects.filter(date_added__year="2021", date_added__month="9",
                                                   choises_activity="Other activity", user=user).count()
            other_choice_oct = Post.objects.filter(date_added__year="2021", date_added__month="10",
                                                   choises_activity="Other activity", user=user).count()
            other_choice_nov = Post.objects.filter(date_added__year="2021", date_added__month="11",
                                                   choises_activity="Other activity", user=user).count()
            other_choice_dec = Post.objects.filter(date_added__year="2021", date_added__month="12",
                                                   choises_activity="Other activity", user=user).count()

            labels = ['Januari', 'Februari', 'Mars', 'April', 'May', 'June', 'July', 'August', 'September',
                      'October', 'November', 'December']
            default_items = [count_days_jan, count_days_feb,count_days_mars,count_days_april,count_days_may,
                             count_days_june,count_days_july,count_days_aug,count_days_sep,count_days_okt,
                             count_days_nov,count_days_dec]
            default_items2 = [work_choise_jan, work_choise_feb, work_choise_mars, work_choise_april, work_choise_may,
                              work_choise_june, work_choise_july, work_choise_aug, work_choise_sep, work_choise_oct,
                              work_choise_nov ,work_choise_dec]
            default_items3 = [regis_choice_jan, regis_choice_feb, regis_choice_mars, regis_choice_april, regis_choice_may,
                              regis_choice_june, regis_choice_july, regis_choice_aug, regis_choice_sep, regis_choice_oct,
                              regis_choice_nov, regis_choice_dec]
            default_items4 = [other_choice_jan, other_choice_feb, other_choice_mars, other_choice_april, other_choice_may,
                              other_choice_june, other_choice_july, other_choice_aug, other_choice_sep, other_choice_oct,
                              other_choice_nov, other_choice_dec]
            data1 = {
                "labels": labels,
                "default": default_items,
                "default2": default_items2,
                "default3": default_items3,
                "default4": default_items4,
            }
            return Response(data1)

        if total_count == "0":
            print("There is", total_count)