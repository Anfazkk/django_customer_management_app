from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponseRedirect

from events.forms import EventForm
from users.models import Customer
from events.models import Events


def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        customer = Customer.objects.get(number=request.user.id)
        
        if form.is_valid():
            instance = form.save(commit=False)
            events, created = Events.objects.get_or_create(
                event_name = instance.event_name,
                event_date = instance.event_date
            )

            customer.event.add(events)
            url = f'/{request.user.id}'
            return HttpResponseRedirect(url)
        
        else:
            form = EventForm()
            context = {
                'title' : 'Add Event',
                'form' : form,
                'error' : True,
                'message' : 'Event error'
            }
            return render(request, 'events/add_event.html', context=context)       

    else:
        form = EventForm()
        context = {
            'title' : 'Add Event',
            'form' : form,
            'error' : True,
            'message' : 'Event error'
        }
        return render(request, 'events/add_event.html', context=context)
    

def edit_event(request, id):
    instance = get_object_or_404(Events, id=id)

    if request.method == 'POST':
        instance = get_object_or_404(Events, id=id)
        form = EventForm(request.POST, request.FILES, instance=instance)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()

            url = f'/{request.user.id}'
            return HttpResponseRedirect(url)
        
    else:
        form = EventForm()
        context = {
            'title' : 'Edit Event',
            'form' : form,
            'error' : True,
            'message' : 'Event error',
            'instances' : instance
        }
        return render(request, 'events/edit_event.html', context=context)


def delete_event(request, id):
    instance = get_object_or_404(Events, id=id)
    instance.is_deleted=True
    instance.save()

    url = f'/{request.user.id}'
    return HttpResponseRedirect(url)


def go_back(request):
    url = f'/{request.user.id}'
    return HttpResponseRedirect(url)