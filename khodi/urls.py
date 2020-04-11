from django.urls import path
from .views import IndexView, KhodiDetailView

app_name = "khodi"
urlpatterns = [
    path('',IndexView.as_view(), name="index"),
    path('<slug:slug>/', KhodiDetailView.as_view(), name = "khodidetail"),
]
