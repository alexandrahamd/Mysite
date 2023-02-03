from django import forms
from catalog.models import Product, Version


class ProductForm(forms.ModelForm):
    list_of_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево',
                     'бесплатно', 'обман', 'полиция', 'радар']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'publication_status', 'category')

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']

        if cleaned_data in self.list_of_words:
            raise forms.ValidationError('Запрещенное название')

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']

        if cleaned_data in self.list_of_words:
            raise forms.ValidationError('Запрещенное описание')

        return cleaned_data


class VersionForm(forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'
