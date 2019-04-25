
from bboard.models import Rubric, Bb
from .forms import BbForm
from django.urls import reverse_lazy

from django.views.generic.edit import CreateView

from django.views.generic.base import TemplateView
from django.views.generic.detail import  DetailView
from django.views.generic.list import ListView
#-------------------------------------------------------------------
#редактировать  и обновить и удалить статью
from django.views.generic.edit import   UpdateView, DeleteView

#LoginRequiredМixin - допускает к странице только пользователей, выполнивших вход:
from django.contrib.auth.mixins import LoginRequiredMixin


"""""""""
UserPassesTestMixin -
допускает к странице только тех пользователей, кто вы­
полнил вход и в чьем отношении переопределенный метод test _ func () вернет
в качестве результата значение тrue (в изначальной реализации метод test _ func ()
возбуждает исключение NotimplementedFLтor, поэтому его обязательно следует
переопределить). Пример:
"""""""""
from django.contrib.auth.mixins import UserPassesTestMixin



class BbCreateView(LoginRequiredMixin, CreateView):
    """Для дабавления обявлений через форму пользователя"""
    template_name = 'bboard/create.html'
    form_class = BbForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context



class BbIindexView(TemplateView):
    """Выводит все записи на галавной странице"""
    template_name = 'bboard/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['bbs'] = Bb.objects.all()
        context['rubrics'] = Rubric.objects.all()
        return context


class BbDetailView(DetailView):
    """Загаловаок статьи ссылкой с переходом на статью"""
    model = Bb

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context




class BbRubricView(ListView):
    """выводит левое меню рублрик """
    template_name = 'bboard/by_rubric.html'
    context_object_name = 'bbs'

    def get_queryset(self):
        return Bb.objects.filter(rubric=self.kwargs['rubric_id'])

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['rubrics'] = Rubric.objects.all()
        context['current_rubric'] = Rubric.objects.get(pk=self.kwargs['rubric_id'])
        return context

#-------------------------------------------------------------------------------------



class BbEditView(UpdateView):
    """Редактировать запись"""
    model = Bb
    form_class = BbForm
    success_url = '/bboard/'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context


class BbDeleteView(DeleteView):
    """Удалить запись """
    model = Bb
    success_url = '/bboard/'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context

#---------------------------------------------------------------


