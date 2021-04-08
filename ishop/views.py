from django.shortcuts import render
from django.views.generic.list import ListView
from .models import CarShop


# Create your views here.
def index(request):
    data = {
        'title': 'Landing'
    }
    return render(request, 'ishop/index.html', data)

class CarShop(ListView):
    model = CarShop
    context_object_name = 'carshop'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Интернет магазин'
        return context