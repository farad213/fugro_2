from django import forms


class Length_form(forms.Form):
    ccs = forms.CharField(max_length=100, required=False)
    vvs = forms.CharField(max_length=100, required=False)

    ccs.widget.attrs = {"class": "ccs", "id": "ccs", "placeholder": "Cölöpcsúcs szint", "autocomplete": "off"}
    vvs.widget.attrs = {"class": "vvs", "id": "vvs", "placeholder": "Visszavésési szint", "autocomplete": "off"}
