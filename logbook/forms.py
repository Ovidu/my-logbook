class MyModelForm(forms.ModelForm):
    class Meta:
        model = MyModel
        widgets = {
            'yes_or_no': forms.RadioSelect
        }
