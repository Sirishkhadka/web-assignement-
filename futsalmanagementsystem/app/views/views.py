from django.shortcuts import render, redirect
from app.forms.forms import UserForm
from app.models.models import User
from django.http import JsonResponse,HttpResponse
from app.authenticate import Authenticate

def homepage(request):
    return render(request,'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

@Authenticate.valid_user
def index(request):
    page = 1
    if request.method == "POST":
        limit = 3
        if 'prev' in request.POST:
            page = (int(request.POST['page']) - 1)
        else:
            page = (int(request.POST['page']) + 1)
        tempoffset = page - 1
        offset = 0
        if tempoffset > 0:
            offset = tempoffset * limit
        users = User.objects.raw('''select * from users limit 3 offset %s''', [offset])
    else:
        users = User.objects.raw("select * from users limit 3 offset 0")
    count = User.objects.count()
    return render(request, "user/index.html", {'users': users, 'counts': count, 'page': page})


@Authenticate.valid_user
def user_search(request):
    users = User.objects.order_by('-user_id').filter(email__contains=request.GET['search']).values()
    data = {
        'users': list(users[:3:0])
    }
    return JsonResponse(data, safe=False)


@Authenticate.valid_user
def create(request):
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            try:
                form.save()
                return redirect('/user')
            except:
                pass
    else:
        form = UserForm()
    return render(request, 'user/create.html', {'form': form})


@Authenticate.valid_user_include_id
def edit(request, id):
    user = User.objects.get(user_id=id)
    return render(request, "user/edit.html", {'user': user})


@Authenticate.valid_user_include_id
def update(request, id):
    user = User.objects.get(user_id=id)
    form = UserForm(request.POST, request.FILES, instance=user)
    if form.is_valid():
        form.save()
        return redirect('/user')
    return render(request, "user/edit.html", {'user': user})


@Authenticate.valid_user_include_id
def delete(request, id):
    user = User.objects.get(user_id=id)
    user.delete()
    return redirect("/user")
