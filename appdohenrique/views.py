from django.shortcuts import render, redirect
from .models import Jogos, ThingsILike


# Create your views here.
def home(request):
    jogos = Jogos.objects.all()
    things = ThingsILike.objects.all()
    return render(request,
                  "home.html",
                  context={
                      "jogos": jogos,
                      "things": things
                  })


def create_jogos(request):
    if request.method == "POST":
        Jogos.objects.create(title=request.POST["title"],
                             genre=request.POST["genre"],
                             price=request.POST["price"],
                             date=request.POST["date"])
        return redirect("home")
    return render(request, "forms.html")


# Create your views here.


def update_jogos(request, id):
    jogos = Jogos.objects.get(id=id)
    print(jogos.title)
    if request.method == "POST":
        jogos.title = request.POST["title"]
        jogos.genre = request.POST["genre"]
        jogos.price = request.POST["price"]
        jogos.date = request.POST["date"]
        jogos.save()
        return redirect("home")
    return render(request,
                  "forms.html",
                  context={
                      "action": "Atualizar",
                      "jogos": jogos
                  })


def delete_jogos(request, id):
    jogos = Jogos.objects.get(id=id)
    print(jogos.title)
    if request.method == "POST":
        if "confirm" in request.POST:
            jogos.delete()
        return redirect("home")
    return render(request,
                  "are_you_sure.html",
                  context={
                      "action": "Atualizar",
                      "jogos": jogos
                  })


def create_things(request):
    if request.method == "POST":
        ThingsILike.objects.create(title=request.POST["title"],
                                   what=request.POST["what"],
                                   when=request.POST["when"],
                                   how_often=request.POST["how_often"])
        return redirect("home")
    return render(request, "forms01.html")


# Create your views here.


def update_things(request, id):
    things = ThingsILike.objects.get(id=id)
    print(things.title)
    if request.method == "POST":
        things.title = request.POST["title"]
        things.what = request.POST["what"]
        things.when = request.POST["when"]
        things.how_often = request.POST["how_often"]
        things.save()
        return redirect("home")
    return render(request,
                  "forms01.html",
                  context={
                      "action": "Atualizar",
                      "things": things
                  })


def delete_things(request, id):
    things = ThingsILike.objects.get(id=id)
    print(things.title)
    if request.method == "POST":
        if "confirm" in request.POST:
            things.delete()
        return redirect("home")
    return render(request,
                  "are_you_sure01.html",
                  context={
                      "action": "Atualizar",
                      "things": things
                  })
