"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from core import views as core_views

urlpatterns = [
    path('', core_views.habit_list, name="habit_list"),
    path('habit/<int:pk>/', core_views.habit_detail, name="habit_detail"),
    path('habit/create/', core_views.habit_create, name="habit_create"),
    path('habit/<int:pk>/delete/', core_views.habit_delete, name="habit_delete"),
    path("habit/<int:pk>/update/", core_views.habit_update, name="habit_update"),
    path('accounts/', include('registration.backends.simple.urls')),
    path('habit/<int:habit_pk>/create_record/', core_views.record_create, name="record_create"),
    #path('records/<int:habit_pk>/create_update/', core_views.record_update, name='record_update'),
    #path('record/<int:pk>/delete/', core_views.record_delete, name='record_delete'),
    path('admin/', admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("api/", include("api.urls")),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
