
from django.contrib import admin
from django.urls import path
from apps.main import views

app_name = "apps.main"
urlpatterns = [
    path('',views.index, name="index"),
    path('category/',views.category, name="category"),
    path('product/<slug:slug>/',views.productdetail, name="productdetail"),
    path('addtocart-<int:pid>/',views.addtocart, name="addtocart"),
    path('my-cart/',views.mycart, name="mycart"),
    path("managecart/<int:cpid>/", views.managecart, name="managecart"),

    path("search/<str:keyword>", views.SearchView,  name = "search"),
]
