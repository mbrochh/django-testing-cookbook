from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import generic


class HomeView(generic.TemplateView):
    template_name = 'birdie/home.html'


class AdminView(generic.TemplateView):
    template_name = 'birdie/admin.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(AdminView, self).dispatch(request, *args, **kwargs)
