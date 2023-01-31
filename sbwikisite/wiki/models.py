from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey

# Create your models here.

#for reading he images in the view
#def image(request):
#   image_file = request.FILES['image_file'].file.read()
#   MyModel.objects.create(image=image_file)



class GameClass(models.Model):
    name_text = models.CharField(max_length=150)
    icon = models.ImageField(upload_to='media')
    description = models.TextField(max_length=1000, blank=True, null=True)
   

    def __str__(self):
        return self.name_text

class BaseClass(models.Model):
    name_text = models.CharField(max_length=150)
    icon = models.ImageField(upload_to='media')
    description = models.TextField(max_length=1000, blank=True, null=True)
    effects = models.TextField(max_length=1000, blank=True, null=True)
    
    def __str__(self):
        return self.name_text

class BaseGameClassRelationship(models.Model):
    classkey = models.ForeignKey(GameClass, on_delete=CASCADE)
    basekey = models.ForeignKey(BaseClass, on_delete=CASCADE)

    def __str__(self):
        return self.classkey.name_text + ' - ' + self.basekey.name_text

class Race(models.Model):
    name_text = models.CharField(max_length=150)
    icon = models.ImageField(upload_to='media')
    description = models.TextField(max_length=1000, blank=True, null=True)
    effects = models.TextField(max_length=1000, blank=True, null=True)
    str_b = models.IntegerField(blank=True, null=True)
    str_m = models.IntegerField(blank=True, null=True)
    dex_b = models.IntegerField(blank=True, null=True)
    dex_m = models.IntegerField(blank=True, null=True)
    con_b = models.IntegerField(blank=True, null=True)
    con_m = models.IntegerField(blank=True, null=True)
    int_b = models.IntegerField(blank=True, null=True)
    int_m = models.IntegerField(blank=True, null=True)
    spi_b = models.IntegerField(blank=True, null=True)
    spi_m = models.IntegerField(blank=True, null=True)
    cost = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return self.name_text

class RaceBaseRelationship(models.Model):
    racekey = models.ForeignKey(Race, on_delete=CASCADE)
    basekey = models.ForeignKey(BaseClass, on_delete=CASCADE)

    def __str__(self):
        return self.racekey.name_text + ' - ' + self.basekey.name_text

class ClassRaceRelationship(models.Model):
    classkey = models.ForeignKey(GameClass, on_delete=CASCADE)
    racekey = models.ForeignKey(Race, on_delete=CASCADE)

    def __str__(self):
        return self.classkey.name_text + ' - ' + self.racekey.name_text


class Discipline(models.Model):
    name_text = models.CharField(max_length=150)
    icon = models.ImageField(upload_to='media')
    description = models.TextField(max_length=1000, blank=True, null=True)
    effects = models.TextField(max_length=1000)
    items =  models.TextField(max_length=500)
    dropper = models.TextField(max_length=500)
    trainer =  models.TextField(max_length=500)

    def __str__(self):
        return self.name_text

class DiscClassRaceRelationship(models.Model):
    disckey = models.ForeignKey(Discipline, on_delete=CASCADE)
    classkey = models.ForeignKey(GameClass, on_delete=CASCADE, blank=True, null=True)
    racekey = models.ForeignKey(Race, on_delete=CASCADE, blank=True, null=True)
    basekey = models.ForeignKey(BaseClass, on_delete=CASCADE, blank=True, null=True)

    def __str__(self):
        result = self.disckey.name_text
        if(self.racekey != None):
            result += '/' + self.racekey.name_text
        if(self.classkey != None):
            result += '/' + self.classkey.name_text
        if(self.basekey != None):
            result += '/' + self.basekey.name_text

        return result

class WeaponPower(models.Model):
    name_text = models.CharField(max_length=150)
    #find a way to reuse existing icons because they repoeat
    icon = models.ImageField(upload_to='media',blank=True, null=True)

    def __str__(self):
        return self.name_text

class WeaponPowerClassRelationship(models.Model):
    classkey = models.ForeignKey(GameClass, on_delete=CASCADE, blank=True, null=True)
    weaponkey = models.ForeignKey(WeaponPower, on_delete=CASCADE)
    basekey = models.ForeignKey(BaseClass, on_delete=CASCADE, blank=True, null=True)
    power_level = models.IntegerField()

    def __str__(self):
        result = self.weaponkey.name_text
        if(self.classkey != None):
            result += '/' + self.classkey.name_text
        if(self.basekey != None):
            result += '/' + self.basekey.name_text

        return result

class SkillLine(models.Model):
    name_text = models.CharField(max_length=150)
    level_granted = models.IntegerField()
    is_mastery = models.BooleanField()

    def __str__(self):
        return self.name_text

class SkillClassRelationship(models.Model):
    classkey = models.ForeignKey(GameClass, on_delete=CASCADE)
    skillkey = models.ForeignKey(SkillLine, on_delete=CASCADE)
    bonus = models.TextField(max_length=300, blank=True, null=True)
    resrictions = models.TextField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.classkey.name_text + ' - ' + self.skillkey.name_text 

class Stance(models.Model):
    name_text = models.CharField(max_length=150)
    powerlevel = models.IntegerField()
    classkey = models.ForeignKey(GameClass, on_delete=CASCADE, blank=True, null=True)
    basekey = models.ForeignKey(BaseClass, on_delete=CASCADE, blank=True, null=True)
    effects = models.TextField(max_length=1000, blank=True, null=True)

    def __str__(self):
        result = self.name_text
        if(self.classkey != None):
            result += '/' + self.classkey.name_text
        if(self.basekey != None):
            result += '/' + self.basekey.name_text

        return result

class Abilities(models.Model):
    name_text = models.CharField(max_length=150)
    icon = models.ImageField(upload_to='media',blank=True, null=True)
    granted_level = models.IntegerField()
    granted_rank = models.IntegerField()
    type = models.CharField(max_length=150)
    cost = models.IntegerField()
    cast_time = models.FloatField()
    cooldown = models.IntegerField()
    hitroll = models.BooleanField()
    description = models.TextField(max_length=1500 ,default=None)
    classkey = models.ForeignKey(GameClass, on_delete=CASCADE, blank=True, null=True)
    basekey = models.ForeignKey(BaseClass, on_delete=CASCADE, blank=True, null=True)
    racekey = models.ForeignKey(Race, on_delete=CASCADE, blank=True, null=True)
    disckey = models.ForeignKey(Discipline, on_delete=CASCADE, blank=True, null=True)


    def __str__(self):
        result = self.name_text
        if(self.racekey != None):
            result += '/' + self.racekey.name_text
        if(self.classkey != None):
            result += '/' + self.classkey.name_text
        if(self.basekey != None):
            result += '/' + self.basekey.name_text
        if(self.disckey != None):
            result += '/' + self.disckey.name_text
        return result

