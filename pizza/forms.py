from django import forms

from .models import Pizza, Size

# form is created based on Model
class PizzaForm(forms.ModelForm):
    # -if we want to change size field options
    # -queryset=Size.objects -> pulls values set in admin area
    # size = forms.ModelChoiceField(
    #     queryset=Size.objects, empty_label=None, widget=forms.RadioSelect)

    class Meta:

        # email = forms.EmailField()
        # url = forms.URLField()

        model = Pizza
        # size field automatically pulls options set in admin area
        fields = ['topping1', 'topping2', 'size']
        labels = {'topping1': 'Topping 1', 'topping2': 'Topping 2'}

        # widgets: use to change options/input types of fields
        # widgets = {'topping1': forms.Textarea, 'topping2': forms.PasswordInput,
        #            'size': forms.CheckboxSelectMultiple}


class MultiplePizzaForm(forms.Form):
    number = forms.IntegerField(min_value=2, max_value=6)


# Manual way to create form
# class PizzaForm(forms.Form):
#     topping1 = forms.CharField(
#         label='Topping 1', max_length=100, widget=forms.PasswordInput)
#     topping2 = forms.CharField(
#         label='Topping 2', max_length=100, widget=forms.Textarea)
#     toppings = forms.MultipleChoiceField(
#         choices=[('pep', 'Pepperoni'), ('cheese', 'Cheese'), ('olive', 'Olive')],
#           widget=forms.CheckboxSelectMultiple)
#     size = forms.ChoiceField(label='Size', choices=[(
#         'Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large')])
