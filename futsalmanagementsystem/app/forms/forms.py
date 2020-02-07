from django import forms
from app.models.models import Team, Ground, Book, User


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = "__all__"


class GroundForm(forms.ModelForm):
    class Meta:
        model = Ground
        fields = "__all__"


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
