"""curddjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path
from curd.views import createView, store, show_emp, delete_emp, update_view, edit, view
from django.conf.urls import include
from curd import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('create', createView),
    # path('store', store, name='store'),
    path('employee/', include('curd.urls')),
    path('Users/', include('Users.urls'))
    # path('delete/<int:emp_id>', delete_emp, name="delete_emp"),
    # path('update/<int:emp_id>', update_view, name="update"),
    # path('edit/<int:emp_id>', edit, name="edit"),
    # path('view/<int:emp_id>', view, name="view")

]

from django.conf.urls.static import static
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
