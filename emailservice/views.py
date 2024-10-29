from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import EmailCampaign
from user.models import User
from .forms import EmailCampaignForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CampaignDeleteForm

# Create your views here.
class CustomLoginRequiredMixin(LoginRequiredMixin):
    def get_login_url(self):
        return reverse_lazy('user:login')





class CreateNewCampain(CustomLoginRequiredMixin,CreateView):
    template_name = 'emailservice/new_campain.html'
    form_class = EmailCampaignForm
    success_url = reverse_lazy('campain:email_list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user  # Pass the user to the form
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class EmailList(CustomLoginRequiredMixin, ListView):
    model = EmailCampaign
    template_name = 'emailservice/email_list.html'
    context_object_name = 'email_campaigns'
    ordering = ['-created_at']  # Proper way to apply sorting

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pass the fields to the template
        context['fields'] = ["name", "subject", "number_of_opens", "email_list"]
        return context




class EmailDetail(CustomLoginRequiredMixin, DetailView):
    model = EmailCampaign
    template_name = 'emailservice/email_detail.html'
    context_object_name = 'email_campaign'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pass the fields to the template
        context['fields'] = ["name", "subject", "number_of_opens", "email_list"]
        return context

class EmailUpdate(CustomLoginRequiredMixin, UpdateView):
    model = EmailCampaign
    template_name = 'emailservice/update_campain.html'
    form_class = EmailCampaignForm

    def get_success_url(self):
        return reverse_lazy('campain:update', kwargs={'pk': self.object.pk})


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user  # Pass the user to the form
        return kwargs


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Dummy data for email opens and regions
        total_email_opens = 150  # Example: Total email opens
        top_regions = [
            ("New York", 40),   # Region with number of opens
            ("London", 35),
            ("Tokyo", 30),
            ("Delhi", 25),
            ("Berlin", 20)
        ]
        top_times = [
            ("10:00 AM", 50),   # Time with number of opens
            ("2:00 PM", 40),
            ("5:00 PM", 30)
        ]
        least_active_time = "12:00 PM"   # Example: Least active time
        least_active_time_count = 5      # Example: Number of opens at that time

        # Pass the dummy data into the context
        context["campain_key"] = self.kwargs["pk"]
        context['total_email_opens'] = total_email_opens
        context['top_regions'] = top_regions
        context['top_times'] = top_times
        context['least_active_time'] = least_active_time
        context['least_active_time_count'] = least_active_time_count

        return context





class EmailDelete(CustomLoginRequiredMixin, DeleteView):
    model = EmailCampaign
    template_name = 'emailservice/delete_campain.html'
    success_url = reverse_lazy('campain:list')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CampaignDeleteForm(campaign=self.object)
        return self.render_to_response(self.get_context_data(form=form))

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CampaignDeleteForm(self.object, request.POST)

        if form.is_valid():
            return self.delete(request, *args, **kwargs)
        else:
            return self.render_to_response(self.get_context_data(form=form))


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["campain_name"] = self.object.name
        return context
