from django import forms
from .models import Quote


class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ["text", "author"]
        widgets = {
            "text": forms.Textarea(attrs={"rows": 4, "placeholder": "Enter the quote..."}),
            "author": forms.TextInput(attrs={"placeholder": "Who said this?"}),
        }
