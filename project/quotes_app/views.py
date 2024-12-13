from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import UserRegisterForm
from .models import Author, Quote


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('quotes:login')
    else:
        form = UserRegisterForm()
    return render(request, 'quotes_app/register.html', {'form': form})


@login_required
def add_author(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        born_date = request.POST['born_date']
        born_location = request.POST['born_location']
        description = request.POST['description']
        Author(fullname=fullname, born_date=born_date, born_location=born_location, description=description).save()
        return redirect('quotes:authors')
    return render(request, 'quotes_app/add_author.html')


@login_required
def add_quote(request):
    if request.method == 'POST':
        quote = request.POST['quote']
        author_id = request.POST['author']
        author = Author.objects.filter(id=author_id).first()
        tags = request.POST['tags']
        user = request.user
        Quote(quote=quote, author=author, tags=tags, user=user).save()
        return redirect('quotes:quotes')
    authors = Author.objects.all()
    return render(request, 'quotes_app/add_quote.html', {'authors': authors})


def author_list(request):
    authors = Author.objects.all()
    return render(request, 'quotes_app/authors.html', {'authors': authors})


def quote_list(request):
    quotes = Quote.objects.all()
    return render(request, 'quotes_app/quotes.html', {'quotes': quotes})


def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    quotes = Quote.objects.filter(author=author)
    return render(request, 'quotes_app/author_detail.html', {'author': author, 'quotes': quotes})
