from django.shortcuts import render

from models import Bank
#from django.views.generic.list import ListView

# Create your views here.

def index(request):
    return render(request,'finance.html')


def banks(request):
    all_banks = Bank.objects.all()
    context = {'all_banks':all_banks}
    return render(request,'bank_list.html',context)


"""
class BankListView(ListView):

    model = Bank

    def get_context_data(self, **kwargs):
        context = super(BankListView, self).get_context_data(**kwargs)
        return context
"""