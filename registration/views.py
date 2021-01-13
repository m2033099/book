from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from .forms import activate_user

from .forms import SignUpForm


class SignUpView(CreateView):
    form_class = SignUpForm
    #foms.pyのSignUpFormを代入
    
    success_url = reverse_lazy('login')
    #登録が成功したらloginの画面に飛ばす
    
    template_name = 'registration/signup.html'

class ActivateView(TemplateView):
    template_name = "registration/activate.html"
    
    def get(self, request, uidb64, token, *args, **kwargs):
        # 認証トークンを検証
        result = activate_user(uidb64, token)
        # コンテクストのresultにTrue/Falseの結果を渡します。
        return super().get(request, result=result, **kwargs)