""" Esse arquivo foi criado do zero para configurar os paths do blog.
No urls.py geral (já existente na pasta mysite), precisaremos incluir (include) nos
urlpatterns, um path para este arquivo blog>urls.py
Normalmente, a função path recebe 3 argumentos:
1. caminho acessado, 
2. view que será executada ou include('aplicação.urls'), 
3. nome opcional.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]
"""


from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]