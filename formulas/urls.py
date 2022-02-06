from django.urls import path

from formulas.views import ViewFormulasAboutTheme, ViewThemes


urlpatterns = [
    path('themes/', ViewThemes.as_view(), name='view-themes'),
    path('themes/theme/<int:theme_pk>', ViewFormulasAboutTheme.as_view(), name='view-formulas'),
]

