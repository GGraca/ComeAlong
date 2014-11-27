from django.views.generic import TemplateView, UpdateView
from models import MyUser
from forms import MyUserForm

class UsersIndex(TemplateView):
    template_name = "users/index.html"

    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
        context['users'] = MyUser.objects.all()
        return context

class UserPageView(TemplateView):
    template_name = "users/page.html"

    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
        context['this_user'] = MyUser.objects.get(username=kwargs['username'])
        return context

class UserUpdateView(UpdateView):
    template_name = "users/edit.html"
    form_class = MyUserForm

    def get_object(self):
        return MyUser.objects.get(username=self.kwargs['username'])
