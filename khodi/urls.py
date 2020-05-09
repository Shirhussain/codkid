from django.urls import path
from .views import IndexView, KhodiDetailView, PostView, ExampleView

app_name = "khodi"
urlpatterns = [
    path('',IndexView.as_view(), name="index"),
    path('<slug:slug>/', KhodiDetailView.as_view(), name = "khodi"),
    path('<slug:khodi_slug>/<slug:post_slug>/', PostView.as_view(), name = "post"),
    path('<slug:khodi_slug>/<slug:post_slug>/<slug:example_slug>/', ExampleView.as_view(), name = "example"),
]
