from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify

class Khodi(models.Model):
	title = models.CharField(max_length=50, unique=True)
	description = models.TextField()
	timestamp   = models.DateTimeField(default=timezone.now)
	slug        = models.SlugField(editable=False)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("khodi:khodidetail",kwargs={"slug":self.slug})


	def save(self, *args, **kwargs):
		if not self.pk:
			self.slug = slugify(self.title)
		return super(Khodi,self).save(*args,**kwargs)



class Post(models.Model):
	title 	  = models.CharField(max_length=60, unique=True)
	content   = models.TextField()
	slug      = models.SlugField(editable=False)
	submitted = models.DateField(default=timezone.now)
	khodi     = models.ForeignKey(Khodi, on_delete=models.CASCADE)
	topic     = models.CharField(max_length=20)

	def __str__(self):
		return self.title 

	def get_absolute_url(self):
		return reverse("khodi:post", kwargs={"slug":self.slug})

	def save(self, *args, **kwargs):
		if not self.pk:
			self.slug = slugify(self.title)
		return super(Post,self).save(*args, **kwargs)

class Example(models.Model):
	name = models.CharField(max_length=50, unique=True)
	code = models.TextField()
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	slug = models.SlugField(editable=False)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse("khodi:example", kwargs={"slug":self.slug})

	def save(self,*args, **kwargs):
		if not self.pk:
			self.slug = slugify(self.name)
		return super(Example,self).save(*args,**kwargs)


