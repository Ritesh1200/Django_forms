from django import forms
from .models import FakeUser

class NormalFroms(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(error_messages={"required":"enter password"} , widget=forms.PasswordInput())
    age = forms.IntegerField(required=False , widget=forms.HiddenInput())

    def clean_name(self):
        """
        validation for single field
        """
        name = self.cleaned_data["name"]
        if len(name) < 5 or len(name) >10:
            raise forms.ValidationError("enter correct name")
        return name

    def clean(self):
        """
        validation for whole form 
        """
        print("this is normal")

        self.cleaned_datas = super().clean()
        print(self.cleaned_datas)
        name = self.cleaned_datas["name"]
        if len(name) < 5 or len(name) >100:
            raise forms.ValidationError("enter correct name")
        
        print(self.cleaned_datas)
        email = self.cleaned_datas["email"]
        if len(email) < 5 or len(email) >100:
            raise forms.ValidationError("enter correct email")
        


class ModelForms(forms.ModelForm):
    class Meta:
        model = FakeUser
        fields = ["name","email","password","age"]

    # def clean_name(self):
    #     """
    #     validation for single field
    #     """
    #     name = self.cleaned_data["name"]
    #     if name == None:
    #         raise forms.ValidationError("Name not found")
    #     if len(name) < 5 or len(name) >100:
    #         raise forms.ValidationError("enter correct name")
    #     return name

    # def clean(self):
    #     """
    #     validation for whole form 
    #     """
    #     self.cleaned_data = super().clean()
    #     name = self.cleaned_data["name"]
    #     if name == "none":
    #         raise forms.ValidationError("Name not found")
    #     if len(name) < 5 or len(name) >100:
    #         raise forms.ValidationError("enter correct name")

    #     email = self.cleaned_data["email"]
    #     if email == None:
    #         raise forms.ValidationError("email not found")
    #     if len(email) < 5 or len(email) >100:
    #         raise forms.ValidationError("enter correct email")
