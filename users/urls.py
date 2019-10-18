from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'users'
urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout', auth_views.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
    path('deleteme/', views.del_user, name="del_user"),

    # Delete specific dilemma
    path('del_dilemma/<int:dilemma_id>/', views.del_dilemma, name="del_dilemma"),

    # Make private dilemma public
    path('make_public/<int:dilemma_id>/', views.make_public, name="make_public"),

    # Make private dilemma public
    path('make_private/<int:dilemma_id>/', views.make_private, name="make_private"),

    path('profile_update/', views.profile_update, name='profile_update'),

]