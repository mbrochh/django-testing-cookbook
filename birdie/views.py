from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import generic

from . import models
from . import forms


class HomeView(generic.TemplateView):
    template_name = 'birdie/home.html'


class AdminView(generic.TemplateView):
    template_name = 'birdie/admin.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(AdminView, self).dispatch(request, *args, **kwargs)


class PostUpdateView(generic.UpdateView):
    model = models.Post
    form_class = forms.PostForm
    success_url = '/'
