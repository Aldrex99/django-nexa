from django import forms
from django.contrib.auth import get_user_model
from .models import Feedback

User = get_user_model()

class FeedbackForm(forms.ModelForm):
    author = forms.ModelChoiceField(
        queryset=User.objects.all(),
        required=False,
        label="Auteur",
        help_text="Laissez vide pour utiliser l’utilisateur connecté"
    )

    class Meta:
        model  = Feedback
        fields = ('author', 'comment', 'rating')

    def clean_rating(self):
        r = self.cleaned_data['rating']
        if not (1 <= r <= 5):
            raise forms.ValidationError("La note doit être comprise entre 1 et 5.")
        return r
