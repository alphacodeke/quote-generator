from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Quote
from .forms import QuoteForm
import random


def home(request):
    approved_quotes = Quote.objects.filter(approved=True)
    quote = random.choice(approved_quotes) if approved_quotes.exists() else None
    return render(request, "quotes/home.html", {"quote": quote})


def add_quote(request):
    if request.method == "POST":
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Quote submitted! It will appear once approved.")
            return redirect("home")
    else:
        form = QuoteForm()
    return render(request, "quotes/add_quote.html", {"form": form})


def quote_list(request):
    quotes = Quote.objects.filter(approved=True)
    return render(request, "quotes/quote_list.html", {"quotes": quotes})
