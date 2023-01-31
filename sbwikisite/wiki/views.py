from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from django.template import loader
from .models import Abilities, DiscClassRaceRelationship, Discipline, GameClass, BaseClass, BaseGameClassRelationship, Race, ClassRaceRelationship, RaceBaseRelationship, SkillClassRelationship, Stance, WeaponPowerClassRelationship

# Create your views here.
def index(request):

    all_classes = GameClass.objects.all().order_by('name_text')
    all_discs = Discipline.objects.all().order_by('name_text')
    all_races = Race.objects.all().order_by('name_text')

    context = {
        "class_list":all_classes,
        "disc_list":all_discs,
        "race_list":all_races
    }
    template = loader.get_template('wiki/home.html')
    return HttpResponse(template.render(context, request))

def gameClass(request, game_class):
    #base_classes = BaseGameClassRelationship.objects.all()
    base_classes = BaseGameClassRelationship.objects.filter(classkey__name_text=game_class.capitalize())
    game_class_object = GameClass.objects.get(name_text=game_class.capitalize())
    
    races = ClassRaceRelationship.objects.filter(classkey__name_text=game_class.capitalize())

    discs = DiscClassRaceRelationship.objects.filter(classkey__name_text=game_class.capitalize())

    skills = SkillClassRelationship.objects.filter(classkey__name_text=game_class.capitalize())

    wp_base = WeaponPowerClassRelationship.objects.filter(classkey__name_text=game_class.capitalize()).values('basekey__name_text').distinct()
    wp_dict = {}
    for base in wp_base:
        temp = WeaponPowerClassRelationship.objects.filter(classkey__name_text=game_class.capitalize(), basekey__name_text=base['basekey__name_text']).values('weaponkey__name_text','power_level','weaponkey__icon').order_by('weaponkey__name_text')
        wp_dict[base['basekey__name_text']] = temp

    abilities_list = Abilities.objects.filter(classkey__name_text=game_class.capitalize())
    abilities_list = abilities_list.order_by('granted_level')


    stance_base = Stance.objects.filter(classkey__name_text=game_class.capitalize()).values('basekey__name_text').distinct()
    stance_dict = {}
    for base in stance_base:
        temp = Stance.objects.filter(classkey__name_text=game_class.capitalize(), basekey__name_text=base['basekey__name_text']).values('name_text','powerlevel')
        stance_dict[base['basekey__name_text']] = temp

    template = loader.get_template('wiki/class-info.html')
    context = {
        'base_class_list':base_classes,
        'game_class':game_class_object,
        'race_list': races,
        'disc_list': discs,
        'skill_list': skills,
        'wp_list': wp_dict,
        'ab_list': abilities_list,
        'stance_list':stance_dict,

    }

    return HttpResponse(template.render(context, request))


def DisciplineView(request, disc):
    

    disc_object =  Discipline.objects.get(name_text=disc) 
    classes = DiscClassRaceRelationship.objects.filter(disckey__name_text=disc).exclude(classkey=None)
    races = DiscClassRaceRelationship.objects.filter(disckey__name_text=disc).exclude(racekey=None)
    abilities = Abilities.objects.filter(disckey=disc_object.pk)



    context = {
        "disc":disc_object,
        "class_list":classes,
        "race_list": races,
        "ab_list":abilities,
        
    }
    template = loader.get_template('wiki/disc-info.html')
    return HttpResponse(template.render(context, request))



def RaceView(request, race):
    

    race_object =  Race.objects.get(name_text=race) 
    classes = ClassRaceRelationship.objects.filter(racekey=race_object.pk).exclude(racekey=None)
    base_classes = RaceBaseRelationship.objects.filter(racekey=race_object.pk).exclude(racekey=None)
    abilities = Abilities.objects.filter(racekey=race_object.pk)

    context = {
        "race":race_object,
        "class_list":classes,
        "base_list": base_classes,
        "ab_list":abilities,
        
    }
    template = loader.get_template('wiki/race-info.html')
    return HttpResponse(template.render(context, request))

def MediaQuery (request, name):
    img = open('media/'+name, 'rb')

    response = FileResponse(img)

    return response

def BaseClassView(request, base):
    

    base_object =  BaseClass.objects.get(name_text=base)
    classes = BaseGameClassRelationship.objects.filter(basekey=base_object.pk).exclude(classkey=None)
    races = DiscClassRaceRelationship.objects.filter(basekey=base_object.pk).exclude(racekey=None)
    abilities = Abilities.objects.filter(basekey=base_object.pk)
    

    context = {
        "base_class":base_object,
        "class_list":classes,
        "race_list": races,
        "ab_list":abilities,
        
    }
    template = loader.get_template('wiki/base-class-info.html')
    return HttpResponse(template.render(context, request))