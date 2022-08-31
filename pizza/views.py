from django.shortcuts import render
from .forms import PizzaForm, MultiplePizzaForm
from django.forms import formset_factory
from .models import Pizza
def home(request):
    return render(request, 'pizza/home.html')


def order(request):
    multiple_form = MultiplePizzaForm()
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST)
        if filled_form.is_valid():
            # save pizza to DB
            created_pizza = filled_form.save()
            created_pizza_pk = created_pizza.id
            topping1 = filled_form.cleaned_data['topping1']
            topping2 = filled_form.cleaned_data['topping2']
            size = filled_form.cleaned_data['size']
            note = f'Thanks for ordering! Your {size} {topping1} {topping2} pizza is on its way.'
            # clears out form so new pizza can be created
            filled_form = PizzaForm()
        else:
            created_pizza_pk = None
            note = 'Pizza order has failed. Try again.'
        # 'pizzaform': filled_form
        # if form not valid, we pass back filled_form so they can edit it.
        # If valid we pass back new form to enter new pizza
        return render(request, 'pizza/order.html', {'pizzaform': filled_form, 'note': note, 'multiple_form': multiple_form, 'created_pizza_pk': created_pizza_pk})
    else:
        form = PizzaForm()
        return render(request, 'pizza/order.html', {'pizzaform': form, 'multiple_form': multiple_form})

# this view will create as many pizza forms as user requested
def pizzas(request):
    # set default value for # for pizzas
    number_of_pizzas = 2
    # get the value from URL
    filled_multiple_pizza_form = MultiplePizzaForm(request.GET)
    if filled_multiple_pizza_form.is_valid():
        number_of_pizzas = filled_multiple_pizza_form.cleaned_data['number']
    # create form set of pizzaform
    PizzaFormSet = formset_factory(PizzaForm, extra=number_of_pizzas)
    formset = PizzaFormSet()

    if request.method == 'POST':
        # Post means forms were submitted
        filled_formset = PizzaFormSet(request.POST)
        if filled_formset.is_valid():
            for form in filled_formset:
                print(form.cleaned_data['topping1'])
            note = 'Pizzas have been ordered!'
        else:
            note = 'Order was not created. Please try again'
        return render(request, 'pizza/pizzas.html', {'note': note, 'formset': formset})
    else:
        # if GET request we want to show forms
        return render(request, 'pizza/pizzas.html', {'formset': formset})


def edit_order(request, pk):
    # pull pizza from DB
    pizza = Pizza.objects.get(pk=pk)
    # create a pizzaform and pass instance=pizza so its filled out already
    form = PizzaForm(instance=pizza)
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST, instance=pizza)
        if filled_form.is_valid():
            filled_form.save()
            form = filled_form
            note = 'Order has been updated.'
            return render(request, 'pizza/edit_order.html', {'pizzaform': form, 'pizza': pizza, 'note': note})

    return render(request, 'pizza/edit_order.html', {'pizzaform': form, 'pizza': pizza})
