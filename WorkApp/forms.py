from django import forms # Djangoが準備しているforms
from .models import Series, test_database1# モデルの部分で定義したDBのテーブル
from django.contrib.auth.forms import AuthenticationForm

class InputForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(InputForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"
    # DBの内容のメタ情報を記載しています
    class Meta:
        model = Series
        fields = ['id', 'title', 'Syusai', 'start_day', 'end_day']
    
class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class']='form-control'
            field.widget.attrs['placeholder']=field.label
