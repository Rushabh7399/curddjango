from django.conf.urls import include

from django.urls import path
from .views import createView, store, show_emp, delete_emp, update_view, edit, view, test_view
urlpatterns = [
    path('create', createView),
    path('store', store, name='store'),
    path('', show_emp),
    path('delete/<int:emp_id>', delete_emp, name="delete_emp"),
    path('update/<int:emp_id>', update_view, name="update"),
    path('edit/<int:emp_id>', edit, name="edit"),
    path('view/<int:emp_id>', view, name="view"),
    path('test', test_view)

]