from django.urls import path
from . import views


app_name = 'easydilemma'
urlpatterns = [
    path('', views.index, name="index"),
    path('dilemma', views.dilemma, name="dilemma"),
    path('dilemma/<int:dilemma_id>/', views.edit_dilemma, name="edit_dilemma"),
    path('all_dilemmas', views.all_dilemmas, name="all_dilemmas"),

    path('handle_dilemma', views.handle_dilemma, name="handle_dilemma"),
    path('handle_dilemma/<int:dilemma_id>/', views.handle_revised_dilemma, name='handle_revised_dilemma'),
    
    path('reasons', views.reasons, name="reasons"),
    path('result/<int:dilemma_id>/', views.store_and_calc_reasons, name="store_and_calc_reasons"),
]