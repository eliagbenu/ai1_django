from django.shortcuts import render

from models import Bank

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#from django.views.generic.list import ListView

# Create your views here.

def index(request):
    return render(request,'finance.html')

def banks(request):
    bank_list = Bank.objects.all()
    paginator = Paginator(bank_list, 2)
    page = request.GET.get('page')

    try:
        all_banks = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        all_banks = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        all_banks = paginator.page(paginator.num_pages)

    context = {'all_banks':all_banks}
    return render(request,'bank_list.html',context)

"""
def banks(request):
    all_banks = Bank.objects.all()

    context = {'all_banks':all_banks}
    return render(request,'bank_list.html',context)
"""

"""
class BankListView(ListView):

    model = Bank

    def get_context_data(self, **kwargs):
        context = super(BankListView, self).get_context_data(**kwargs)
        return context
"""