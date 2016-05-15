from django.db import models

class GeneralMat(models.Model):
        numberOf = models.IntegerField(default=1)
        title = models.CharField(max_length=100)
        description = models.CharField(max_length=1000)
        storeDestination = models.CharField(max_length=100)

class Picasso(models.Model):
        Position = models.CharField(max_length=30)
        Title = models.CharField(max_length=50)
        Type = models.CharField(max_length=2) # LA Lageraktivitaet, LS Lagersport, AN Andacht, VA Vereinsaktivitaet
        Destination = models.CharField(max_length=50)
        TimekDate = models.DateTimeField('date published')
        TargetGroup = models.CharField(max_length=15)   # Kinder, Jugendliche
        Responsibles = models.CharField(max_length=35)
        Atachements = models.CharField(max_length=50)   # Rutenplanung, Kartenausschnitt, Zeitberechnung, Spielplan
        SpecialSecurit = models.BooleanField(default=0)
        LinkToSecurity = models.CharField(max_length=100)
        LinkToAlternative = models.CharField(max_length=100)
        
class blockEvents(models.Model):
        event = models.ForeignKey(Picasso)
        TimeFrom = models.DateTimeField('date published')
        TimeTo = models.DateTimeField('date published')
        Description = models.CharField(max_length=1000)
        Responsible = models.CharField(max_length=35)
        
class blockMatList(models.Model):
        mat = models.ForeignKey(Picasso)
        numberOf = models.IntegerField(default=0)
        item = models.ForeignKey(GeneralMat)
        responsible = models.CharField(max_length=20)


        