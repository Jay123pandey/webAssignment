from django.shortcuts import render, redirect
from app.models.item import Item
from app.forms.itemform import ItemForm
from app.authentication import Authenticate

@Authenticate.user_valid
def index(request):
    items = Item.objects.all()
    return render(request, "item/index.html", {'items': items})


@Authenticate.user_valid
def create(request):
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect("/item")
            except:
                pass
    else:
        form = ItemForm()
    return render(request, "item/create.html", {'form': form})

@Authenticate.valid_user_include_id
def edit(request, id):
    item = Item.objects.get(item_id=id)
    return render(request, "item/edit.html", {'item': item})

@Authenticate.valid_user_include_id
def update(request, id):
    item = Item.objects.get(item_id=id)
    form = ItemForm(request.POST, request.FILES, instance=item)
    if form.is_valid():
        form.save()
        return redirect('/item')
    return render(request, "item/edit.html", {'item': item})

@Authenticate.valid_user_include_id
def delete(request, id):
    Item.objects.get(item_id=id).item_image.delete()
    item = Item.objects.get(item_id=id)
    item.delete()
    return redirect("/item")
