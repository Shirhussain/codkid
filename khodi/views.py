from django.shortcuts import render
from django.views import generic
from .models import Khodi, Post, Example

class IndexView(generic.ListView):
	template_name = "index.html"
	context_object_name = "khodis"
	queryset = Khodi.objects.all().order_by('-timestamp')


class KhodiDetailView(generic.DetailView):
	template_name = "detail.html"
	context_object_name = "khodi"

	def get_queryset(self):
		self.obj = Khodi.objects.filter(slug=self.kwargs["slug"])
		return self.obj 

	def get_context_deta(self,*args,**kwargs):
		context = super(KhodiDetailView,self).get_context_data(**kwargs)
		context['posts'] = Post.objects.filter(khodi=self.obj)
		return context

class PostView(generic.DetailView):
	template_name 		= "post.html"
	context_object_name = "post"
	slug_url_kwarg      = "post_slug"

	def get_queryset(self):
		self.obj = Post.objects.filter(slug = self.kwargs["post_slug"]
			).filter(khodiــslug = self.kwargs["khodi_slug"])
		return self.obj 

	def get_context_data(self, *args, **kwargs):
		context = super(PostView, self).get_context_data(**kwargs)
		context['examples'] = Example.objects.filter(post = self.obj)
		return context

class ExampleView(generic.DetailView):
	template_name = "example.html"
	context_object_name = "example"
	slug_url_kwarg      = "example_slug"

	def get_queryset(self):
		self.obj = Example.objects.filter(slug = self.kwargs["example_slug"]).filter(
			                              post__slug = self.kwargs["post_slug"])
		return self.obj 

	def get_context_data(self, *args, **kwargs):
		context = super(ExampleView,self).get_context_data(**kwargs)
		# context['']

