from django.shortcuts import render, HttpResponse
from immudb.client import ImmudbClient
from django.http import Http404, JsonResponse
import json
import random
from app1.forms import *
# Create your views here.

# key = "BANK_TRANSFER_00"
# data = {
#     "bank_transaction_id": 762349991003 + 1,
#     "from": "Mark",
#     "to": "Bob",
#     "amount": 500.00
# }


def Index(request):
    return render(request, "app1/index.html")

def SingleInput(request):
    ic = ImmudbClient()
    ic.login(username="immudb", password="immudb")
    form = NameForm(request.POST)
    if form.is_valid():
        key = form.cleaned_data['akey']
        data = form.cleaned_data['name']
        ret = ic.verifiedSet(key.encode("utf8"), json.dumps(data).encode("utf8"))
        return HttpResponse("Thank you")
    return render(request, 'app1/input.html', {'form': form})


def MultipleInput(request):
    ic = ImmudbClient()
    ic.login(username="immudb", password="immudb")
    counter = Counter(request.POST)
    if counter.is_valid():
        ctr = counter.cleaned_data['counter']
        for x in range(1, int(ctr) + 1):
            key = str(x)
            data = str(random.randint(1, 10000))
            ret = ic.verifiedSet(key.encode("utf8"), json.dumps(data).encode("utf8"))
        return HttpResponse("Thank you")
    return render(request, 'app1/inputm.html', {'form': counter})


def OutputDataSingle(request):
    try:
        ic = ImmudbClient()
        ic.login(username="immudb", password="immudb")

        form = OutputS(request.POST)
        if form.is_valid():
            values = form.cleaned_data['akey']
            ret = ic.verifiedGet(values.encode("utf8"))
            data = json.loads(ret.value.decode('utf8'))
            return render(request, "app1/output.html", {
                "id": values,
                "name": data,
                'form': form
            })
        return render(request, "app1/output.html", {'form': form})
    except:
        raise Http404()


def OutputDataMultiple(request):
    ic = ImmudbClient()
    ic.login(username="immudb", password="immudb")

    form = OutputM(request.POST)
    dict_data = {}
    if form.is_valid():
        min_num = form.cleaned_data['min_num']
        max_num = form.cleaned_data['max_num']
        for x in range(int(min_num), int(max_num)):
            ret = ic.verifiedGet(str(x).encode("utf8"))
            data = json.loads(ret.value.decode('utf8'))
            dict_data[x] = data
    dict_data = json.dumps(dict_data, indent=2)
    print(dict_data)
    return render(request, "app1/outputm.html", {
        'dictionary': dict_data,
        'form': form
    })
