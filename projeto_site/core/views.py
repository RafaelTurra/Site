# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
#
def index(request):
        return render(request, "index.html")



def login(request):
        if request.method == "GET":
                return render(request, "login.html")
        else:
                senha = request.POST.get("pass")
                if senha is "teste123":
                      print("Usuário",request.POST.get("email"),"entrou com sucesso")
                      time.sleep( 5 )
                      return render(request, "contato.html")
                else:
                        print("Usuário",request.POST.get("email"),"entrou com senha errada.")

def contato(request):
        if request.method == "GET":
                return render(request, "contato.html")
        else:
                print("Nome: ",request.POST.get("nome"))