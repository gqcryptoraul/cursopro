from django import forms
from .models import Personas

from ckeditor.widgets import CKEditorWidget

class PersonasForm(forms.ModelForm):

    class Meta:
        model = Personas
        fields = (
            'name', 'last_name', 'correo', 'fec_nac', 'direccion',
              'departamento', 'job', 'habilidades', 'salario','full_name','cv','avatar',
        )

        widgets = { 
            'habilidades': forms.CheckboxSelectMultiple(),
            'cv': forms.CharField(widget=CKEditorWidget(config_name='awesome_ckeditor'))
            

        }