from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.conf import settings

from django.contrib.auth.tokens import default_token_generator
#ユーザー特有のトークンを生成するため
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

subject = "登録確認"
message_template = """
ご登録ありがとうございます。
以下URLをクリックして登録を完了してください。

"""
#メールの本文

def get_activate_url(user):
    #URLを生成する関数
    #関数にuserを代入するとuidとtokenを生成する
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = default_token_generator.make_token(user)
    return settings.FRONTEND_URL + "/activate/{}/{}/".format(uid, token)
    #FRONTEND_URLはsettings.pyに設定したメールの本文に載せるurl。

User = get_user_model()
#form .models import Userの呼び出し方は非推奨
#Userモデルを変えようとした時に反映されないことがある。

class SignUpForm(UserCreationForm):
    #emailを必須で入力させるフォーム
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        # formがsaveされた時にこの関数が呼ばれる
        
        user = super().save(commit=False)
        # まずemail以外の、usernameとpasswordをuserに代入してホームに保存
        # commit=Falseだと、DBに保存されない
        #メールアドレスが誰かと被った時にusernameとpasswordだけDBに保存されるのを防ぐ
        
        user.email = self.cleaned_data["email"]
        #userのメールアドレスに代入
        
        # 確認するまでログイン不可にする
        user.is_active = False
        
        if commit:
            user.save()
            
            #認証用のurlを生成
            activate_url = get_activate_url(user)
            
            message = message_template + activate_url
            
            #user1人にメールアドレスを送信
            user.email_user(subject, message)
        return user
        
#認証urlをクリックしたらユーザーを有効化する関数
def activate_user(uidb64, token):    
    try:
        #uidを復元
        uid = urlsafe_base64_decode(uidb64).decode()
        
        #uidからユーザーを探す
        user = User.objects.get(pk=uid)
    except Exception:
        #ユーザーが見つからなければFalseを返す
        return False
    
    if default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return True
    
    return False