from django import forms
from .models import LiquorStock,Sale

class AddStockForm(forms.ModelForm):
    class Meta:
        model = LiquorStock
        fields = ['liquor_name', 'price', 'stock_quantity']

class SalesForm(forms.ModelForm):
    liquor_name = forms.ModelChoiceField(
        queryset=LiquorStock.objects.all(),  # Use the LiquorStock model queryset
        to_field_name="liquor_name",  # Specify the field to use for display
        label="Liquor Name"
    )

    class Meta:
        model = Sale
        fields = ['liquor_name', 'stock_sold']

class EditStockForm(forms.ModelForm):
    class Meta:
        model = LiquorStock
        fields = ['liquor_name', 'price', 'stock_quantity']

