from pickle import FALSE
from unicodedata import decimal
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Church(models.Model):
    id_church = models.BigAutoField(primary_key=True)  # Field name made lowercase.
    namet = models.CharField(db_column='nameT', max_length=50, blank=True, null=True, verbose_name='Nombre de la iglesia')  # Field name made lowercase.
    municipality = models.CharField(max_length=50, blank=True, null=True, verbose_name='Municipio')
    address = models.CharField(max_length=50, blank=True, null=True, verbose_name='Dirección')
    district = models.CharField(max_length=50, blank=True, null=True, verbose_name='Distrito')
    cp = models.IntegerField(blank=True, null=True, verbose_name='Código Postal')
    phone1 = models.CharField(max_length=255,blank=True, null=True, verbose_name='Telefono')
    phone2 = models.CharField(max_length=255, blank=True, null=True, verbose_name='Teléfono alterno')

    def __str__(self):
        return self.namet

class UserT(models.Model):
    ID_User = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=40, null=False, blank=False, verbose_name='Nombre')
    lastName = models.CharField(max_length=50, null=False, blank=False, verbose_name='Apellidos')
    gender = models.CharField(max_length=20, null=False, blank=False, verbose_name='Género')
    username = models.CharField(max_length=20, null=False, blank=False, verbose_name='Username')
    phone = models.CharField(max_length=255, null= False, blank=False, verbose_name='Teléfono')
    passwordT = models.CharField(max_length=255, null=False, blank=False, verbose_name='Contraseña')
    userType = models.CharField(max_length=20, null=False, blank=False, verbose_name='Tipo de usuario')
    mail = models.CharField(max_length=50, null=False, blank=False, verbose_name='Correro electrónico')
    id_church = models.ForeignKey(Church, on_delete=models.CASCADE, verbose_name="Iglesia")
    isAdmin = models.BooleanField(default=False, verbose_name="Administrador")

    def __str__(self):
        cadena=self.firstName+" "+self.lastName
        return cadena
        
class Extended(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="extension")
    gender = models.CharField(max_length=20, null=False, blank=False, verbose_name='Género')
    phone = models.CharField(max_length=255, null= False, blank=False, verbose_name='Teléfono')
    mail = models.CharField(max_length=50, null=False, blank=False, verbose_name='Correro electrónico')
    id_church = models.ForeignKey(Church, on_delete=models.CASCADE, verbose_name="Iglesia")
    isAdmin = models.BooleanField(default=False, verbose_name="Administrador")

class Parameter(models.Model):
    id_parameter = models.BigAutoField(primary_key=True)
    ID_User = models.OneToOneField(User, on_delete=models.CASCADE, related_name="prueba")
    lastupdate = models.DateField(db_column='lastUpdate', blank=True, null=True)  # Field name made lowercase.
    waist = models.DecimalField(decimal_places=2, max_digits=9, blank=True, null=True, verbose_name='Cintura')
    weight = models.DecimalField(decimal_places=2, max_digits=9, blank=True, null=True)
    imc = models.DecimalField(decimal_places=2, max_digits=9, blank=True, null=True)
    clock = models.DecimalField(decimal_places=2, max_digits=9, blank=True, null=True)
    gds = models.DecimalField(decimal_places=2, max_digits=9, blank=True, null=True)
    katz = models.DecimalField(decimal_places=2, max_digits=9, blank=True, null=True)
    lwb = models.DecimalField(decimal_places=2, max_digits=9, blank=True, null=True)
    sarcf = models.DecimalField(decimal_places=2, max_digits=9, db_column='sarcF', blank=True, null=True)  # Field name made lowercase.
    pantcirs = models.DecimalField(decimal_places=2, max_digits=9, db_column='pantCirs', blank=True, null=True)  # Field name made lowercase.
    leftstrong = models.DecimalField(decimal_places=2, max_digits=9, db_column='leftStrong', blank=True, null=True)  # Field name made lowercase.
    rightstrong = models.DecimalField(decimal_places=2, max_digits=9, db_column='rightStrong', blank=True, null=True)  # Field name made lowercase.
    higheststrong = models.DecimalField(decimal_places=2, max_digits=9, db_column='highestStrong', blank=True, null=True)  # Field name made lowercase.
    sppbbalance = models.DecimalField(decimal_places=2, max_digits=9, db_column='sppbBalance', blank=True, null=True)  # Field name made lowercase.
    standem = models.DecimalField(decimal_places=2, max_digits=9, db_column='sTandem', blank=True, null=True)  # Field name made lowercase.
    tandem = models.DecimalField(decimal_places=2, max_digits=9, blank=True, null=True)
    spds = models.DecimalField(decimal_places=2, max_digits=9, db_column='spdS', blank=True, null=True)  # Field name made lowercase.
    mtss = models.DecimalField(decimal_places=2, max_digits=9, db_column='mtsS', blank=True, null=True)  # Field name made lowercase.
    speed = models.DecimalField(decimal_places=2, max_digits=9, blank=True, null=True)
    globalsppb = models.DecimalField(decimal_places=2, max_digits=9, db_column='globalSppb', blank=True, null=True)  # Field name made lowercase.
    frailtysppb = models.DecimalField(decimal_places=2, max_digits=9, db_column='frailtySppb', blank=True, null=True)  # Field name made lowercase.
    frailtycfs = models.DecimalField(decimal_places=2, max_digits=9, db_column='frailtyCfs', blank=True, null=True)  # Field name made lowercase.
    gijon = models.DecimalField(decimal_places=2, max_digits=9, blank=True, null=True)
    ospace = models.DecimalField(decimal_places=2, max_digits=9, db_column='oSpace', blank=True, null=True)  # Field name made lowercase.
    otime = models.DecimalField(decimal_places=2, max_digits=9, db_column='oTime', blank=True, null=True)  # Field name made lowercase.
    calculation = models.DecimalField(decimal_places=2, max_digits=9, blank=True, null=True)
    memoryt = models.DecimalField(decimal_places=2, max_digits=9, db_column='memoryT', blank=True, null=True)  # Field name made lowercase.
    eject = models.DecimalField(decimal_places=2, max_digits=9, blank=True, null=True)
    totalmmse = models.DecimalField(decimal_places=2, max_digits=9, db_column='totalMmse', blank=True, null=True)  # Field name made lowercase.
    evaluation = models.TextField(max_length=300, blank=False, verbose_name='evaluation')
    planning = models.TextField(max_length=300, blank=False, verbose_name='planning')
    
    def __str__(self):
        fecha = str(self.lastupdate) +", "+ str(self.ID_User)
        return fecha

