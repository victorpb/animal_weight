from django.views.generic import ListView


from .models import FarmModel, AnimalWeigthModel


class HomeView(ListView):

    template_name = 'home.html'

    def get_queryset(self):
        return FarmModel.objects.filter(owner=self.request.user)


class ListAnimalWeigth(ListView):
    template_name = 'list_animals.html'

    def get_queryset(self):
        return AnimalWeigthModel.objects.filter(farm__token=self.kwargs['farm'])
