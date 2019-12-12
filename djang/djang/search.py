from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from books.models import Book, Publisher
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from djang.form import ContactForm


def search(request):
    errors = []
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) >= 20:
            errors.append('Please enter at most 20 characters.')
        else:
            book = Publisher.objects.filter(name__icontains=q)
            print(book)
            return render_to_response('search_result.html', {'books': book, 'query': q})
    print(errors)
    return render_to_response('search_form.html', {'errors': errors})

@csrf_exempt
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            list = []
            list.append(cd.get('email', 'noreply@example.com'))
            send_mail(
                    cd['subject'],
                    cd['message'],
                    '834015958@qq.com',
                    list
                )
            return HttpResponseRedirect('/contact/thanks/')
        else:
            form = ContactForm(
                initial={'subject':'i love your site!'}
            )
        return render_to_response('contact_form.html',
                              {'form':form})

    return render_to_response('contact_form.html',
                              {'form': ContactForm(request.POST)})



def test_form(request):
    pass
