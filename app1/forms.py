from django import forms

class NameForm(forms.Form):
    name = forms.CharField(label='name', max_length=100)
    akey = forms.CharField(label='key', max_length=100)

class Counter(forms.Form):
    counter = forms.IntegerField(label='counter', max_value=1000)

class OutputS(forms.Form):
    akey = forms.CharField(label='key', max_length=100)

class OutputM(forms.Form):
    min_num = forms.IntegerField(label='Minimum Number', max_value=1000)
    max_num = forms.IntegerField(label='Max Number', max_value=1000)