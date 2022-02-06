from django import forms

from formulas.models import Theme


class QuizForm(forms.Form):
    themes = forms.ModelMultipleChoiceField(
        label="Выберите темы для теста", 
        queryset=Theme.objects.all(),
        widget=forms.SelectMultiple(
            attrs={
                'class': 'form-control',
            }
        )
    )
    quantity_questions = forms.IntegerField(
        label="Введите кол-во вопросов которые хотите прорешать.", 
        min_value=1,
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
            }
        )
    ) 
