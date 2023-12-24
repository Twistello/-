from django.shortcuts import render
from django.views.generic.base import View
from .models import Post

# Create your views here.
class postView(View):
    '''Вывод завписей'''
    def get(self,request):
        posts = Post.objects.all()
        return render(request, 'main/main.html',{'post_list':posts})