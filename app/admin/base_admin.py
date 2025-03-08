from django.contrib.admin import register, site
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from unfold.widgets import INPUT_CLASSES, SELECT_CLASSES

from unfold.admin import ModelAdmin, StackedInline

from django_celery_results.models import GroupResult, TaskResult
from django_celery_results.admin import (
    GroupResultAdmin as BaseGroupResultAdmin,
    TaskResultAdmin as BaseTaskResultAdmin,
)


from django_celery_beat.models import (
    ClockedSchedule,
    CrontabSchedule,
    IntervalSchedule,
    PeriodicTask,
    SolarSchedule,
)
from django_celery_beat.admin import (
    PeriodicTaskAdmin as BasePeriodicTaskAdmin,
    ClockedScheduleAdmin as BaseClockedScheduleAdmin,
    CrontabScheduleAdmin as BaseCrontabScheduleAdmin,
)

from app.models import Profile


class ProfileInline(StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = "Profile"


site.unregister(User)
site.unregister(PeriodicTask)
site.unregister(ClockedSchedule)
site.unregister(IntervalSchedule)
site.unregister(CrontabSchedule)
site.unregister(SolarSchedule)
site.unregister(GroupResult)
site.unregister(TaskResult)


@register(User)
class DjangoUserAdmin(BaseUserAdmin, ModelAdmin):
    inlines = (ProfileInline,)


@register(SolarSchedule)
class SolarScheduleAdmin(ModelAdmin):
    pass


@register(ClockedSchedule)
class ClockedScheduleAdmin(BaseClockedScheduleAdmin, ModelAdmin):
    pass


@register(IntervalSchedule)
class IntervalScheduleAdmin(ModelAdmin):
    pass


@register(CrontabSchedule)
class CrontabScheduleAdmin(BaseCrontabScheduleAdmin, ModelAdmin):
    pass


@register(GroupResult)
class GroupResultAdmin(BaseGroupResultAdmin, ModelAdmin):
    pass


@register(TaskResult)
class TaskResultAdmin(BaseTaskResultAdmin, ModelAdmin):
    pass


@register(PeriodicTask)
class PeriodicTaskAdmin(BasePeriodicTaskAdmin, ModelAdmin):
    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        form.base_fields["regtask"].widget.attrs = {"class": " ".join(SELECT_CLASSES)}
        form.base_fields["task"].widget.attrs = {"class": " ".join(INPUT_CLASSES)}
        return form
