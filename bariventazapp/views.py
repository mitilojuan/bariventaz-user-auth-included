from django.shortcuts import render
from .models import *


def products(request):
    productsautocomplete =  Electronics.objects.all()
    productsautocomplete2 =  Products.objects.all()
    products =  Products.objects.all().order_by('?')[:1] #the number four is to limit the number of queries shown on the browser from the database. Meaning that only five queries would be shown.
    products2 =  Products.objects.all().order_by('?')[:1]
    products3 =  Products.objects.all().order_by('?')[:1]
    products4 =  Products.objects.all().order_by('?')[:1]
    products5 =  Products.objects.all().order_by('?')[:1]
    products6 =  Products.objects.all().order_by('?')[:1]
    products7 =  Products.objects.all().order_by('?')[:1]
    products8 =  Products.objects.all().order_by('?')[:1]
    products9 =  Products.objects.all().order_by('?')[:1]
    products10 =  Products.objects.all().order_by('?')[:1]
    products11 =  Products.objects.all().order_by('?')[:1]
    products12 =  Products.objects.all().order_by('?')[:1]
    electronics = Electronics.objects.all().order_by('?')[:1]
    electronics2 = Electronics.objects.all().order_by('?')[:1]
    electronics3 = Electronics.objects.all().order_by('?')[:1]
    electronics4 = Electronics.objects.all().order_by('?')[:1]
    electronics5 = Electronics.objects.all().order_by('?')[:1]
    electronics6 = Electronics.objects.all().order_by('?')[:1]
    electronics7 = Electronics.objects.all().order_by('?')[:1]
    electronics8 = Electronics.objects.all().order_by('?')[:1]
    electronics9 = Electronics.objects.all().order_by('?')[:1]
    electronics10 = Electronics.objects.all().order_by('?')[:1]
    electronics11 = Electronics.objects.all().order_by('?')[:1]
    electronics12 = Electronics.objects.all().order_by('?')[:1]
    slides = Electronics.objects.all().order_by('?')[:1]
    slides2 = Electronics.objects.all().order_by('?')[:1]



    return render(request, 'home.html', {'products':products, 'products2':products2, 'products3':products3, 'products4':products4, 'products5':products5,
                                        'products6':products6,'products7':products7, 'products8':products8, 'products9':products9, 'products10':products10,
                                        'products11':products11, 'products12':products12, 'electronics': electronics, 'electronics2': electronics2,
                                        'electronics3': electronics3, 'electronics4': electronics4, 'electronics5': electronics5, 'electronics6': electronics6,
                                        'electronics7': electronics7, 'electronics8': electronics8, 'electronics9': electronics9, 'electronics10': electronics10,
                                        'electronics11': electronics11, 'electronics12': electronics12, 'slides':slides, 'productsautocomplete': productsautocomplete,
                                        'productsautocomplete2': productsautocomplete2, 'slides2': slides2})







def stores(request):
    storesauto = Stores.objects.all()
    productsautocomplete =  Electronics.objects.all()
    productsautocomplete2 =  Products.objects.all()
    stores = Stores.objects.all().order_by('?')[:1]
    electronics2 = Electronics.objects.all().order_by('?')[:1]
    electronics3 = Electronics.objects.all().order_by('?')[:1]
    electronics4 = Electronics.objects.all().order_by('?')[:1]
    electronics5 = Electronics.objects.all().order_by('?')[:1]
    electronics6 = Electronics.objects.all().order_by('?')[:1]
    electronics7 = Electronics.objects.all().order_by('?')[:1]
    electronics8 = Electronics.objects.all().order_by('?')[:1]
    electronics9 = Electronics.objects.all().order_by('?')[:1]
    electronics10 = Electronics.objects.all().order_by('?')[:1]
    electronics11 = Electronics.objects.all().order_by('?')[:1]
    electronics12 = Electronics.objects.all().order_by('?')[:1]

    return render(request, 'stores.html', {'stores': stores, 'electronics2': electronics2, 'electronics3': electronics3, 'electronics4': electronics4,
                                                'electronics5': electronics5, 'electronics6': electronics6, 'electronics7': electronics7, 'electronics8': electronics8,
                                                'electronics9': electronics9, 'electronics10': electronics10, 'electronics11': electronics11,
                                                'electronics12': electronics12, 'productsautocomplete': productsautocomplete, 'productsautocomplete2': productsautocomplete2,
                                                'storesauto': storesauto})










def render_eljubilazo(request,pk):
    productsautocomplete =  Electronics.objects.all()
    productsautocomplete2 =  Products.objects.all()
    accessories = Vefase.objects.all().order_by('?')[:1]


    return render(request, 'eljubilazo.html', {'accessories': accessories, 'productsautocomplete': productsautocomplete, 'productsautocomplete2': productsautocomplete2})












def specific2(request,pk):
    specifics2 = Electronics.objects.filter(id=pk)
    return render(request, 'specifics2.html', {'specifics2':specifics2})

def search_product(request):

    storesauto = Stores.objects.all()
    productsautocomplete =  Electronics.objects.all()
    productsautocomplete2 =  Products.objects.all()
    """ search function  """
    if request.method == "POST":
        query_name = request.POST.get('name', None)



    if query_name:
        results = Products.objects.filter(item__contains=query_name).order_by('?') or Electronics.objects.filter(item__contains=query_name).order_by('?')
    #else:
        results2 =Stores.objects.filter(name__contains=query_name)

        if not results and not results2:

            return render(request, 'noresults.html')



    #if query_name:
        #results2 = Stores.objects.filter(name__contains=query_name)


        #if not results2:
                #return render(request, 'noresults.html', {'productsautocomplete': productsautocomplete, 'productsautocomplete2': productsautocomplete2,
                                                          #'storesauto': storesauto})







    return render(request, 'specifics.html', {'results': results, 'results2': results2,  'productsautocomplete': productsautocomplete, 'productsautocomplete2': productsautocomplete2,
                                                  'storesauto': storesauto})








def search_product2(request):





    """ search function """
    if request.method == "POST":
        query_name2 = request.POST.get('name', None)
        if query_name2:
            search2 = Electronics.objects.filter(item__contains=query_name2)
            if not search2:
                    return render(request, 'noresults.html')
        return render(request, 'specifics2.html', {"search2":search2})

    return render(request, 'specifics2.html')

def details2(request,pk):

    details2 =  Electronics.objects.filter(id=pk) or Products.objects.filter(id=pk)
    suggested = Electronics.objects.all().order_by('?')[:1]
    suggested2 = Electronics.objects.all().order_by('?')[:1]
    suggested3 = Electronics.objects.all().order_by('?')[:1]
    productsautocomplete =  Electronics.objects.all()
    productsautocomplete2 =  Products.objects.all()
    return render(request, 'moredetails2.html', {'details2':details2, 'suggested': suggested, 'suggested2':suggested2, 'suggested3': suggested3,
                                                 'productsautocomplete': productsautocomplete, 'productsautocomplete2': productsautocomplete2})






def details(request,pk):
    details2 =  Vefase.objects.filter(id=pk)
    suggested = Electronics.objects.all().order_by('?')[:1]
    suggested2 = Electronics.objects.all().order_by('?')[:1]
    suggested3 = Electronics.objects.all().order_by('?')[:1]
    productsautocomplete =  Electronics.objects.all()
    productsautocomplete2 =  Products.objects.all()
    return render(request, 'vefase.html', {'details2':details2, 'suggested': suggested, 'suggested2':suggested2, 'suggested3': suggested3,
                                                 'productsautocomplete': productsautocomplete, 'productsautocomplete2': productsautocomplete2})







def specific(request,pk):
    storesauto = Stores.objects.all()
    productsautocomplete =  Electronics.objects.all()
    productsautocomplete2 =  Products.objects.all()
    specifics = Products.objects.filter(id=pk) or Electronics.objects.filter(id=pk) or Stores.objects.filter(id=pk)
    return render(request, 'specifics.html', {'specifics':specifics, 'productsautocomplete': productsautocomplete, 'productsautocomplete2': productsautocomplete2,
                                              'storesauto': storesauto})


def admincontact(request):
    return render(request, 'admincontact.html')

def specific3(request):
    specifics3 = Electronics.objects.all()
    return render(request, 'specifics3.html', {'specifics3':specifics3})

def ElJubilazoStore(request):
    jubilazomarket =  ElJubilazo.objects.all().order_by('?')[:1] #the number four is to limit the number of queries shown on the browser from the database. Meaning that only five queries would be shown.


    return render(request, 'ElJubilazo.html', {'jubilazomarket':jubilazomarket,})