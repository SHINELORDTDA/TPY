from django.db import models # type: ignore

class Quartier(models.Model):
    # Identifiant de la maison (généré automatiquement par Django)
    id = models.AutoField(primary_key=True)

    # Attributs de la maison
    nom_quartier = models.CharField(max_length=100)
    ville = models.CharField(max_length=100)
    superficie = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nom_quartier}, {self.ville} - {self.superficie} m²"


