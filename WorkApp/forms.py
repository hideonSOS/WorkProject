from django import forms # Djangoが準備しているforms
from .models import Series, test_database1# モデルの部分で定義したDBのテーブル

class InputForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(InputForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"
    # DBの内容のメタ情報を記載しています
    class Meta:
        model = Series
        fields = ['id', 'title', 'Syusai', 'start_day', 'end_day']