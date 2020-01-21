from django import forms

class EmailForm(forms.Form):
    mail = forms.EmailField(label='Email',
                            widget= forms.TextInput(attrs={'class':'form-control flex-fill mr-0 mr-sm-2 mb-3 mb-sm-0',
                                                           'placeholder':'Digite aqui seu melhor e-mail'})
                            )