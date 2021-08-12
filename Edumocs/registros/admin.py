from django.contrib import admin
from .models import Profesores
from .models import Cursos
from .models import Usuario


admin.site.register(Profesores)
admin.site.register(Cursos)
admin.site.register(Usuario)
