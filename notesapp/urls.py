from django.urls import path
from .import views

urlpatterns = [
    path('',views.Index,name="index"),
    path("login/",views.Login,name="Login"),
    path("signup/", views.Signup, name="Signup"),
    path('note/<int:id>',views.Note,name="note"),
    path('<int:id>/update/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete')
]

