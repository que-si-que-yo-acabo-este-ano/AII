from django.contrib import admin
from principal.models import Usuario,Diario,Autor,Noticia
# Register your models here.
admin.site.register(Usuario)
admin.site.register(Diario)
admin.site.register(Autor)
admin.site.register(Noticia)