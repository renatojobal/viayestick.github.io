from django.db import models

"""Modelos para el portal"""

class Welcome_message(models.Model):
    """ Clase para guardar el mensaje de bienvenida """

    # Attributes
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=900)


class About(models.Model):
    """ Clase para  guardar la descripcion sobre nosotros """

    # Attributes
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=900)


class Portal(models.Model):
    """ Clase central"""

    # Attributes
    logo_url = models.URLField()
    name = models.CharField(max_length=100, help_text="Introduzca el título del portal")

    # Realitional attributes
    about = models.OneToOneField(About, blank=True, null=True, on_delete=models.SET_NULL)
    welcome_message = models.OneToOneField(Welcome_message, blank=True, null=True, on_delete=models.SET_NULL)



class External_link(models.Model):
    """ Clase para referenciar a redes sociales y links de descarga"""

    # Attributes
    name = models.CharField(max_length=100)
    url_logo = models.URLField()
    link = models.URLField()

    # Realitional attributes
    portal = models.ForeignKey(to=Portal, null=False, blank=False, on_delete=models.CASCADE)


class Review(models.Model):
    """ Clase para guardar una resena de una peresona sobre el proyecto """

    # Attribute
    person_name = models.CharField(max_length=200)
    content = models.CharField(max_length=500)
    person_photo_url = models.URLField()

    # Realitional attributes
    portal = models.ForeignKey(to=Portal, null=False, blank=False, on_delete=models.CASCADE)

