from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name','email', 'phone','subject','message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'İsminiz'}),
            'description': forms.Textarea(
                attrs={'placeholder': 'Telefon numarası'}),
            'email': forms.TextInput(attrs={'placeholder': 'E-mail Adresiniz'}),
            'description': forms.Textarea(
                attrs={'placeholder': 'Email adresi'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Telefon Numaranız'}),
            'subject': forms.Select(attrs={'placeholder': 'Talebiniz'}),
            'message': forms.Textarea(attrs={'placeholder': 'Mesajınız'}),
        }

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    
