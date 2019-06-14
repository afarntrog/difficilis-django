from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('dilemma', views.dilemma, name="dilemma"),
    path('dilemma/<int:dilemma_id>/', views.edit_dilemma, name="edit_dilemma"),
    path('all_dilemmas', views.all_dilemmas, name="all_dilemmas"),
    path('reasons', views.reasons, name="reasons"),
    path('handle_dilemma', views.handle_dilemma, name="handle_dilemma"),
    path('test_reason/<int:dilemma_id>/', views.test_reason, name="test_reason"),

    # path('bla', views.create_book_normal, name="create_book_normal"),
]