from django.forms import ModelForm
from .models import Notes

class NoteForm(ModelForm):
    class Meta:
        model = Notes
        fields = ('text', )
    
    def __init__(self, *args, **kwargs):
        super(NoteForm,self).__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'class' : 'textarea', 'placeholder' : 'What\'s on your mind ?'})
