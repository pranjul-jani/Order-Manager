from django import forms
from .models import Order


# Because we use bootstrap on frontend,we create a BaseForm that informs all the fields get the class form-control.
# Then the forms we want to create inherits from both BaseForm and forms.ModelForm.
from django import forms

from .models import Order


class BaseForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class OrderCreateForm(BaseForm, forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Order
        fields = ['date', 'title' ]


class OrderEditForm(BaseForm, forms.ModelForm):

    class Meta:
        model = Order
        fields = ['date', 'title', 'discount', 'is_paid']