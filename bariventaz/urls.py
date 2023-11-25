from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from bariventazapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("register/", views.register, name="register"),
    path("login/", LoginView.as_view(template_name="login.html"),
        name="login"),
    path("logout/", LogoutView.as_view(template_name="logout.html"),
        name="logout"),
    path('', views.products, name='products'),
    path('search_product', views.search_product, name='search'),
    path('search_product2/', views.search_product2, name='search2'),
    path('specific/<str:pk>/', views.specific, name='specifics'),
    path('specific2/<str:pk>/', views.specific2, name='specifics2'),
    path('specific3/', views.specific3, name='specifics3'),
    path('admincontact/', views.admincontact, name='admincontact'),
    path('stores/', views.stores, name='stores'),
    path('render_eljubilazo/<str:pk>/', views.render_eljubilazo, name='render_eljubilazo'),
    path('details/<str:pk>/', views.details, name='details'),
    path('details2/<str:pk>/', views.details2, name='details2'),
    path('ElJubilazoStore/', views.ElJubilazoStore, name='ElJubilazo'),




]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)