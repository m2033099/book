from django.views.generic import View
from django.template.response import TemplateResponse

class IndexView(View):
    def get(self, request, *args, **kwargs):
        
        
        return TemplateResponse(request, 'bookshelf/index.html')

index = IndexView.as_view()
        