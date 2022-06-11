from django.urls import path
from .views import home, inscripcion, productos, quienessomos

urlpatterns = [
    path('', home,name="home"),
    path('inscripcion/', inscripcion,name="inscripcion"),
    path('productos/', productos,name="productos"),
    path('quienessomos/', quienessomos,name="quienessomos"),
]