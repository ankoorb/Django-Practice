# from django.shortcuts import render
# from django.http import HttpResponse
#
# # Create your views here.
# def home(request):
#     return HttpResponse('It works!')

from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from home.forms import HomeForm
from home.models import Post


class HomeView(TemplateView):
    template_name = 'home/home.html'

    # # Overwriting GET method from parent class
    # def get(self, request):
    #     pass

    def get(self, request):
        form = HomeForm()
        posts = Post.objects.all().order_by('-created')
        args = {'form': form, 'posts': posts}
        return render(request, self.template_name, args)

    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            text = form.cleaned_data['post'] # From forms.py
            form = HomeForm()
            return redirect('home:home')

        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)


