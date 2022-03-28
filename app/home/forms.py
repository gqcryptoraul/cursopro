from logging import PlaceHolder
from django import forms
from .models import Test

class TestForm(forms.ModelForm):
    """Form definition for MODELNAME."""

    class Meta:
        """Meta definition for MODELNAMEform."""

        model = Test
        fields = (
            'titulo',
            'subtitulo',
            'cantidad',
        )
        widgets= {
            'titulo': forms.TextInput(  
                attrs = {
                    'placeHolder': 'Ingrese el tituilo aqui',

                }

            )
        }

    def clean_cantidad(self):
        cantidad= self.cleaned_data['cantidad']
        if cantidad <10:
            raise forms.ValidationError('Ingrese un Numero Mayor 10')

        return cantidad

