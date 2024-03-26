from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import store


urlpatterns = [

    path('<slug:category_slug>/', store, name='products_by_category'),
    path('', store, name='store'),
]
