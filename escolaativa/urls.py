from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('gamificacao.urls')),
    path('gamificacao/', include('gamificacao.urls')),
    path('admin/', admin.site.urls),
]
