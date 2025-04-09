from django.db import models # type: ignore


class Maison(models.Model):
    # Identifiant de la maison (généré automatiquement par Django)
    id = models.AutoField(primary_key=True)

    # Attributs de la maison
    nombre_de_chambres = models.IntegerField()
    couleur = models.CharField(max_length=100)
    adresse = models.CharField(max_length=255)
    superficie = models.DecimalField(max_digits=10, decimal_places=2)
    type_maison = models.CharField(max_length=50)
    quartier = models.ForeignKey('Quartier', on_delete=models.CASCADE, related_name='maisons')

    def __str__(self):
        return f"{self.nombre_de_chambres} chambres, {self.couleur}, {self.adresse}"