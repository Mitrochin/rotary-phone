from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
path('quotes/', include('quotes_app.urls', namespace='quotes')),
    path('register/', include('quotes_app.urls')),
    path('login/', include('quotes_app.urls')),
    path('logout/', include('quotes_app.urls')),
    path('add_author/', include('quotes_app.urls')),
    path('add_quote/', include('quotes_app.urls')),
    path('authors/', include('quotes_app.urls')),
    path('', RedirectView.as_view(url='/quotes/', permanent=False)),
]

