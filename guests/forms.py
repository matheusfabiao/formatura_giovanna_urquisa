from django import forms
from .models import Guest


class GuestForm(forms.ModelForm):
    honeypot = forms.CharField(widget=forms.HiddenInput(), required=False)
    
    class Meta:
        model = Guest
        fields = ['name', 'email', 'phone', 'image', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seu nome completo'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Seu endereço de e-mail'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seu número de telefone'}),
            'image': forms.FileInput(attrs={'class': 'form-control-file'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Sua mensagem', 'rows': 5}),
        }

        labels = {
            'name': 'Nome',
            'email': 'E-mail',
            'phone': 'Telefone',
            'image': 'Foto de perfil',
            'message': 'Mensagem',
        }
        
        error_messages = {
            'name': {
                'required': 'Por favor, insira seu nome completo.',
            },
            'email': {
                'required': 'Por favor, insira seu endereço de e-mail.',
                'invalid': 'Por favor, insira um endereço de e-mail válido.',
            },
            'phone': {
                'required': 'Por favor, insira seu número de telefone.',
            },
        }

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = True
        self.fields['email'].required = True
        self.fields['phone'].required = True
        
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Guest.objects.filter(email=email).exists():
            raise forms.ValidationError("Já existe um convidado com esse e-mail.")
        return email


    def clean_honeypot(self):
        if self.cleaned_data.get('honeypot'):
            raise forms.ValidationError("O campo honeypot não deve ser preenchido.")
        return self.cleaned_data.get('honeypot')
