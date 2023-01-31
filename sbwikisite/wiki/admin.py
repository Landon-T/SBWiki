from django.contrib import admin

from .models import BaseClass
from .models import GameClass
from .models import BaseGameClassRelationship
from .models import Race
from .models import ClassRaceRelationship
from .models import Discipline
from .models import DiscClassRaceRelationship
from .models import WeaponPower
from .models import WeaponPowerClassRelationship
from .models import SkillLine
from .models import SkillClassRelationship
from .models import Stance
from .models import Abilities
from .models import RaceBaseRelationship



# Register your models here.

admin.site.register(BaseClass)
admin.site.register(GameClass)
admin.site.register(BaseGameClassRelationship)
admin.site.register(Race)
admin.site.register(ClassRaceRelationship)
admin.site.register(Discipline)
admin.site.register(DiscClassRaceRelationship)
admin.site.register(WeaponPower)
admin.site.register(WeaponPowerClassRelationship)
admin.site.register(SkillLine)
admin.site.register(SkillClassRelationship)
admin.site.register(Stance)
admin.site.register(Abilities)
admin.site.register(RaceBaseRelationship)
