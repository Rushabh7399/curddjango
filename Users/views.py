from django.shortcuts import render, redirect, HttpResponse
from Users.forms import UserForm, OrderForm
from Users.models import Orders
# Create your views here.

def create_user(request):
    user = UserForm()
    return render(request, 'create_user.html', {"user": user})

def create_order(request):

    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = OrderForm()
    return render(request, 'orders_view.html', {'form': form})

def success(request):
    return HttpResponse('successfully uploaded')

def display_hotel_images(request):
    if request.method == 'GET':
        # getting all the objects of hotel.
        Hotels = Orders.objects.all()
        return render(request, 'display_order_images.html',
                       {'order_images': Hotels})

def signup(request):
    return render(request, "sign_up.html")