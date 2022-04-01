from django import forms # Djangoが準備しているforms
from .models import test_database1 # モデルの部分で定義したDBのテーブル

class InputForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(InputForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"
    # DBの内容のメタ情報を記載しています
    class Meta:
        model = test_database1
        exclude = ['id', 'str_aria1', 'str_aria2', 'date_field']