from django.urls import path

from formulas.views import ViewFormulasAboutTheme, ViewThemes


urlpatterns = [
    path('themes/', ViewThemes.as_view(), name='view-themes'),
    path('themes/theme/<int:theme_pk>', ViewFormulasAboutTheme.as_view(), name='view-formulas'),
#    path('view-movie/<slug:movie_slug>', ViewMovie.as_view(), name='view-movie'),
#    path('like-movie/<int:movie_pk>', AddLikeToMovie.as_view(), name='like-movie'),
#    path('dislike-movie/<int:movie_pk>', AddDislikeToMovie.as_view(), name='dislike-movie'),
]

