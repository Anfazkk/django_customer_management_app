import datetime

from django.shortcuts import render, get_object_or_404

from users.models import Customer
from events.forms import EventForm


def index(request):
    customers = Customer.objects.all()
    context = {
        'title' : 'Customers',
        'customers' : customers
    }
    return render(request, 'web/index.html', context=context)


def sort(request, id):
    instances = get_object_or_404(Customer.objects.filter(number=id))
    events = instances.event.filter(is_deleted=False)

    sort  = request.GET.get('sort')
    now = datetime.datetime.now()
    month = now.month

    if sort:
        if sort == 'today':
            events = instances.event.filter(event_date=datetime.date.today(), is_deleted=False)
        elif sort == 'this-month':
            events = instances.event.filter(event_date__month=month, is_deleted=False)
        elif sort == 'all':
            events = events
    else:
        context = {
            'title' : instances.full_name,
            'events' : events,
            'instances' : instances,
            'error' : True,
            'message' : 'Event error'
        }
        return render(request, 'events/item.html', context=context)
    
    context = {
        'title' : instances.full_name,
        'events' : events,
        'instances' : instances,
        'error' : True,
        'message' : 'Event error'
    }
    return render(request, 'events/item.html', context=context)