from django.shortcuts import render, redirect
from app.forms.forms import TeamForm
from app.models.models import Team
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
        teams = Team.objects.raw('''select * from teams limit 3 offset %s''', [offset])
    else:
        teams = Team.objects.raw("select * from teams limit 3 offset 0")
    count = Team.objects.count()
    return render(request, "team/index.html", {'teams': teams, 'counts': count, 'page': page})


@Authenticate.valid_user
def create(request):
    if request.method == "POST":
        form = TeamForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect('/team')
            except:
                pass
    else:
        form = TeamForm()
    return render(request, 'team/create.html', {'form': form})


@Authenticate.valid_user_include_id
def edit(request, id):
    team = Team.objects.get(team_id=id)
    return render(request, "team/edit.html", {'team': team})


@Authenticate.valid_user_include_id
def update(request, id):
    team = Team.objects.get(team_id=id)
    form = TeamForm(request.POST, request.FILES, instance=team)
    if form.is_valid():
        form.save()
        return redirect('/team')
    return render(request, "team/edit.html", {'team': team})


@Authenticate.valid_user_include_id
def delete(request, id):
    Team.objects.get(team_id=id).team_image.delete()
    team = Team.objects.get(team_id=id)
    team.delete()
    return redirect("/team")


def create_self(request):
    if request.method == "POST":
        form = TeamForm(request.POST, request.FILES)

        form.save()
        return redirect('/team')

    return render(request, '/')
