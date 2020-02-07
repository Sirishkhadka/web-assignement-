from django.shortcuts import render, redirect
from app.forms.forms import GroundForm
from app.models.models import Ground
from app.authenticate import Authenticate

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
        grounds = Ground.objects.raw('''select * from grounds limit 3 offset %s''', [offset])
    else:
        grounds = Ground.objects.raw("select * from grounds limit 3 offset 0")
    count = Ground.objects.count()
    return render(request, "ground/index.html", {'grounds': grounds, 'counts': count, 'page': page})

@Authenticate.valid_user
def create(request):
    if request.method == "POST":
        form = GroundForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect('/ground')
            except:
                pass
    else:
        form = GroundForm()
    return render(request, 'ground/create.html', {'form': form})

# @Authenticate.valid_user_include_id
def edit(request, id):
    ground = Ground.objects.get(ground_id=id)
    return render(request, "ground/edit.html", {'ground': ground})

@Authenticate.valid_user_include_id
def update(request, id):
    ground = Ground.objects.get(ground_id=id)
    form = GroundForm(request.POST, request.FILES, instance=ground)
    if form.is_valid():
        form.save()
        return redirect('/ground')
    return render(request, "ground/edit.html", {'ground': ground})

@Authenticate.valid_user_include_id
def delete(request, id):
    ground = Ground.objects.get(ground_id=id)
    ground.delete()
    return redirect("/ground")
