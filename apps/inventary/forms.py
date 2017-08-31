from django import forms

from apps.inventary.models import Computer

class InventoryForm(forms.ModelForm):
    class Meta:
        model = Computer
        fields = [
            'oficina',
            'nom_usuario',
            'sis_operativo',
            'cap_disco',
            'memoria',
            'procesador',
            'monitor',
            'perifericos',
            'estado',
        ]
        labels = {
            'oficina': 'Localización Física',
            'nom_usuario': 'Nombre de Usuario',
            'sis_operativo': 'Sistema Operativo',
            'cap_disco': 'Capacidad de Disco Duro',
            'memoria': 'Memoria RAM',
            'procesador':'Procesador',
            'monitor': 'Monitor',
            'perifericos': 'Periféricos',
            'estado': 'Estado',
        }
        widgets = {
            'oficina':forms.Select(attrs={'class':'form-control'}),
            'nom_usuario':forms.TextInput(attrs={'class':'form-control'}),
            'sis_operativo':forms.TextInput(attrs={'class':'form-control'}),
            'cap_disco':forms.TextInput(attrs={'class':'form-control'}),
            'memoria':forms.TextInput(attrs={'class':'form-control'}),
            'procesador':forms.TextInput(attrs={'class':'form-control'}),
            'monitor':forms.TextInput(attrs={'class':'form-control'}),
            'perifericos':forms.Textarea(attrs={'class':'form-control'}),
            'estado':forms.Select(attrs={'class':'form-control'}),
        }
