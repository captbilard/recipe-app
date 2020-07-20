from django.forms import ModelForm, Textarea, TextInput, Select
from recipe.models import Meals

class AddMealForm(ModelForm):
    class Meta:
        model = Meals
        fields = ('name', 'category','ingredients', 'steps')
        widgets = {
            'name': TextInput(attrs={'class':'form-control', 'type':'text', 'placeholder':'Name of Meal..'}),
            'category':Select(attrs={'class':'btn btn-secondary dropdown-toggle', 'type':'button',}),
            'ingredients':Textarea(attrs={'class':'form-control', 'cols':40,'rows':10}),
            'steps':Textarea(attrs={'class':'form-control', 'cols':40, 'rows':10})
        }