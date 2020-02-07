from django.shortcuts import render, redirect
from app.forms.forms import BookForm
from app.models.models import Book, Ground, Team

from app.authenticate import Authenticate


@Authenticate.valid_user
def index(request):
    books = Book.objects.all()
    return render(request, "book/index.html", {'books': books, 'counts': 0, 'page': 1})


@Authenticate.valid_user
def create(request):
    grounds = Ground.objects.all()
    teams = Team.objects.all()
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect('/book')
            except:
                pass
    else:
        form = BookForm()
    return render(request, 'book/create.html', {'form': form, 'grounds': grounds, 'teams': teams})


@Authenticate.valid_user_include_id
def delete(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect("/book")


def create_self(request):
    print(request.method == "POST")
    if request.method == "POST":
        print(request.POST)
        form = BookForm(request.POST, request.FILES)
        # if form.is_valid():
        #     try:
        form.save()
        return redirect('/book')
    # except:
    #     pass

    return redirect('/')
