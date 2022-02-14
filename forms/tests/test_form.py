import pytest
from forms.forms import ModelForms

class TestForm:

    def test_Correct(self):    

        form = ModelForms(data = {
            "name":"ritesh pandey",
            "email":"riteshpandey1200@gmail.com",
            "password":"Hello1200",
            "age":"12"
        })
        assert form.is_valid()
    
    def test_empty_data(self):    

        form = ModelForms(data = {})
        assert form.is_valid() == False