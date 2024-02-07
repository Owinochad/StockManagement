from django.shortcuts import render, redirect, get_object_or_404
from .forms import AddStockForm, EditStockForm, SalesForm
from .models import LiquorStock

# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')

def stocks(request):
    liquor_stocks = LiquorStock.objects.all()
    for liquor in liquor_stocks:
        liquor.quantity_price = liquor.stock_quantity * liquor.price
        liquor.save()
    return render(request, 'stocks.html',{'liquor_stocks': liquor_stocks})

def add_stock(request):
    if request.method == 'POST':
        form = AddStockForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/stocks')  # Redirect to the stocks page (adjust the URL name as needed)
    else:
        form = AddStockForm()

    return render(request, 'add_stock.html', {'form': form})

def sales(request):
    if request.method == 'POST':
        form = SalesForm(request.POST)
        if form.is_valid():
            sale = form.save(commit=False)

            # Fetch the corresponding LiquorStock object based on the selected liquor_name
            liquor_stock = get_object_or_404(LiquorStock, liquor_name=sale.liquor_name)

            # Subtract the stock_sold from the stock_quantity
            if sale.stock_sold <= liquor_stock.stock_quantity:
                liquor_stock.stock_quantity -= sale.stock_sold
                liquor_stock.save()

                # Save the Sale object after updating the liquor stock
                sale.quantity_price = liquor_stock.price * sale.stock_sold
                sale.save()

                return redirect('/stocks')  # Redirect to the sales page after making the sale
            else:
                # Handle the case where stock_sold exceeds stock_quantity (optional)
                # You may want to display an error message or handle it differently
                return redirect('/stock_check?liquor_name=' + sale.liquor_name)
    else:
        form = SalesForm()

    return render(request, 'sales.html', {'form': form})

def edit_stock(request, id):
    liquor = get_object_or_404(LiquorStock, id=id)

    if request.method == 'POST':
        form = EditStockForm(request.POST, instance=liquor)
        if form.is_valid():
            form.save()
            return redirect('/stocks')  # Redirect to the stock page after updating
    else:
        form = EditStockForm(instance=liquor)

    return render(request, 'edit_stock.html', {'form': form, 'liquor': liquor})

def stock_check(request):
    # Fetch the corresponding LiquorStock object based on the selected liquor_name
    liquor_stock = get_object_or_404(LiquorStock, liquor_name=request.GET.get('liquor_name'))

    # Fetch the corresponding Liquor object based on the selected liquor_name
    liquor = liquor_stock.liquor_name

    # Pass the liquor object and its stock quantity to the template
    return render(request, 'stock_check.html', {'liquor': liquor, 'liquor_stocks': liquor_stock.stock_quantity})
