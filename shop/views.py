from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from shop.forms import ProductForm
from shop.models import Product


# Create your views here.
def dashboard(request):
    context = {

    }
    return render(request, 'shop/admin_dashboard.html', context)


class ProductListView(ListView):
    model = Product
    extra_context = {
        'products_count': Product.objects.count()
    }
    paginate_by = 10


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm


class ProductDeleteView(DeleteView):
    model = Product
