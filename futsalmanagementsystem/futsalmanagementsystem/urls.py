"""newmew URL Configuration

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
from django.urls import path
from app.views import views, brand, auth, team, ground, book

# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('homepage',views.homepage),
    path('login', auth.login),
    path('user_login', auth.entry),
    path('logout', auth.logout),
    path('user_search', views.user_search),
    path('user', views.index),
    path('user_create', views.create),
    path('user_edit/<int:id>', views.edit),
    path('user_update/<int:id>', views.update),
    path('user_delete/<int:id>', views.delete),
    path('', auth.index),
    path('team', team.index),
    path('team_create', team.create),
    path('team_create_self', team.create_self),
    path('team_edit/<int:id>', team.edit),
    path('team_update/<int:id>', team.update),
    path('team_delete/<int:id>', team.delete),
    path('ground', ground.index),
    path('ground_create', ground.create),
    path('ground_edit/<int:id>', ground.edit),
    path('ground_update/<int:id>', ground.update),
    path('ground_delete/<int:id>', ground.delete),
    path('book', book.index),
    path('book_create', book.create),
    path('book_create_self', book.create_self),
    path('book_delete/<int:id>', book.delete),
    path('about', views.about),
    path('contact', views.contact),
    # path('brand', brand.index),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
