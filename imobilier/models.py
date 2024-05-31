from django.db import models

class Employé(models.Model):
    nom=models.CharField(max_length=100)
    prenom=models.CharField(max_length=100)
    date_de_naissance=models.DateField()
    email=models.EmailField()
    poste_choices = [
         ('agent_imobilier', 'agent_imobilier'),
         ('comptable', 'comptable'),
         ('secretaire', 'secretaire'),
        
        
    ]

    poste=models.CharField(max_length=50, choices=poste_choices)

    def __str__(self):
        return f' L\'employé {self.prenom} {self.nom} a été ajouté'


# Create your models here.
