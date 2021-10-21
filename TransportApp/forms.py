from django import forms
from TransportApp.models import Cars, Transport, Orders, Drivers


class CarsModelForm(forms.ModelForm):
    class Meta:
        model = Cars
        fields = '__all__'
        labels = {
            'name': 'Nazwa pojazdu'
        }


class DriversModelForm(forms.ModelForm):
    class Meta:
        model = Drivers
        fields = '__all__'
        labels = {
            'name': 'Nazwa kierowcy'
        }


class TransportModelForm(forms.ModelForm):
    class Meta:
        model = Transport
        fields = '__all__'
        labels = {
            'car': 'Samochód',
            'driver': 'Kierowca',
            'order': 'Zamówienie'
        }


class OrdersModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(OrdersModelForm, self).__init__(*args, **kwargs)
        self.fields['opis'].required = False

    class Meta:
        model = Orders
        fields = ('client', 'phone_number', 'delivery_address', 'delivery_day', 'delivery_hour', 'opis')
        labels = {
            'client': 'Klient',
            'phone_number': 'Numer Telefonu',
            'delivery_address': 'Adres dostawy',
            'delivery_day': 'Dzień dostawy',
            'delivery_hour': 'Godzina dostawy',
            'opis': 'Dodatkowe info',
        }
        widgets = {
            'delivery_day': forms.DateInput(attrs={'type': 'date'}),
            'delivery_hour': forms.TimeInput(attrs={'type': 'time'})
        }


class TransportForm(forms.Form):
    car = forms.ModelChoiceField(queryset=Cars.objects.all(), label="Samochód")
    driver = forms.ModelChoiceField(queryset=Drivers.objects.all(), label='Kierowca')
