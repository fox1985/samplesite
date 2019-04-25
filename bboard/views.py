
from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from .models import Bb, Rubric
from .forms import BbForm, SearchForm
#-------------------------------------------------------------------------
from  django.forms import modelformset_factory, formset_factory
from django.forms.formsets import  ORDERING_FIELD_NAME










# Create your views here.

def index(request):
    bbs = Bb.objects.all()
    rubrics = Rubric.objects.all()
    return render(request, 'bboard/index.html', {'bbs': bbs, 'rubrics': rubrics})


def by_rubric(request, rubric_id):
    #filter метод: возвращает первую запись набора или None, если набор пуст :
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'bbs': bbs, 'rubrics' : rubrics, 'current_rubric' : current_rubric }
    return render(request, 'bboard/by_rubric.html', context)




def add_and_save(request):
    """Добавления через форму пользовотелям """
    if request.method == 'POST':
        bbf = BbForm(request.POST)
        if bbf.is_valid():
            bbf.save()
            return HttpResponseRedirect(reverse('by_rubric', kwargs={'rubric_id': bbf.cleaned_data['rubric'].pk}))
        else:
            context = {'form':bbf}
            return render(request, 'bboard/create.html', context)

    else:
        bbf = BbForm()
        context = {'form': bbf}
        return render(request, 'bboard/create.html', context)



def index(request):
    # Проверяем, имеет ли текущий пользователь права добавлять,
    # править и удалять рубрики
    #if request.user.has_perms(('bboard.add_rubric', 'bboard.change_rubric', 'bboard.change_rubric', 'bboard.delete_rubric')):

    rubrics = Rubric.objects.all()
    bbs = Bb.objects.all()
    """Пример использования пагинатора"""
    paginator = Paginator(bbs, 2)
    if 'page' in request.GET:
        page_num = request.GET['page']
    else:
        page_num = 1

    page = paginator.get_page(page_num)
    context = {'rubrics': rubrics, 'page': page, 'bbs': page.object_list}
    return  render(request, 'bboard/index.html', context)

#----------------------------------------------------------------------------------------


def search(request):
    if request.method == 'POST':
        sf = SearchForm(request.POST)
        if sf.is_valid():
            keyword = sf.cleaned_data['keyword']
            rubric_id =sf.cleaned_data['rucric'].pk
            bbs = Bb.objects.filter(...)
            context = {'bbs': bbs}
            return render(request, 'bboard/search_result.html', context)
    else:
        sf = SearchForm()
        context = {'form': sf}
        return render(request, 'bboard/search.html', context)



def formset_processing(request):
    FS = formset_factory(SearchForm, extra=3, can_order=True, can_delete=True)

    if request.method == 'POST':
        formset = FS(request.POST)
        if formset.is_valid():
            for form in formset:
                if form.cleaned_data and not form.cleaned_data['DELETE']:
                    keyword = form.cleaned_data['keyword']
                    rubric_id = form.cleaned_data['rucric'].pk
                    order = form.cleaned_data['ORDER']
                    'Выполнаяем какие-либо действия над полученными данными'
                return render(request, 'bboard/process_result.html')
        else:
            formset = FS()
            context = {'formset': formset}
            return render(request, 'bboard/formset.html', context)




