from  . models import Category

def menu_links(request):
    links=Category.objects.all()
    return dict(menu_links=links)