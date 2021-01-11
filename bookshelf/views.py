from django.views.generic import View
from django.shortcuts import render 

class IndexView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'message': "Hello World!"
        }
        
        return render(request, 'index.html', context)

index = IndexView.as_view()
        