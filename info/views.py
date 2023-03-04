from django.shortcuts import render
from django.http.response import HttpResponseRedirect

from users.models import Customer
from info.forms import UpdateUserForm


def update(request, id):
    data = Customer.objects.get(id=id)
    form = UpdateUserForm(instance=data)

    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            url = f'/{request.user.id}'
            return HttpResponseRedirect(url)
    
    context = {
        'title': 'Update',
        'form': form, 
    }
    return render(request, 'web/update.html', context=context)