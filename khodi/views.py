from django.shortcuts import render
from django.views import generic
from .models import Khodi

class IndexView(generic.ListView):
	template_name = "index.html"
	# model = Khodi
	context_object_name = "khodis"
	queryset = Khodi.objects.all().order_by('-timestamp')


class KhodiDetailView(generic.DetailView):
	model = Khodi
	template_name = "detail.html"
	context_object_name = "khodi"





















# from django.shortcuts import get_object_or_404

# def book_detail_view(request, primary_key):
#     book = get_object_or_404(Book, pk=primary_key)
#     return render(request, 'catalog/book_detail.html', context={'book': book})



# class BookDetailView(View):
#     def get(self, request, *args, **kwargs):
#         book = get_object_or_404(Book, pk=kwargs['pk'])
#         context = {'book': book}
#         return render(request, 'books/book_detail.html', context)