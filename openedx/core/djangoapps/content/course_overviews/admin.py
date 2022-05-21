"""
Django admin page for CourseOverviews, the basic metadata about a course that
is used in user dashboard queries and other places where you need info like
name, and start dates, but don't actually need to crawl into course content.
"""

from common.djangoapps.student.models import CourseAccessRole
from config_models.admin import ConfigurationModelAdmin
from django.contrib import admin

from .models import CourseOverview, CourseOverviewImageConfig, CourseOverviewImageSet, SimulateCoursePublishConfig
from openedx.features.branch.utils import get_user_branch_id, is_system_admin, is_branch_admin

class CourseOverviewAdmin(admin.ModelAdmin):
    """
    Simple, read-only list/search view of Course Overviews.
    """
    list_display = [
        'id',
        'display_name',
        'version',
        'enrollment_start',
        'enrollment_end',
        'created',
        'modified',
    ]

    search_fields = ['id', 'display_name']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser or is_system_admin(request.user):
            return qs

        # Filter here by user branch, so user only see users from the same branch
        branch_id = get_user_branch_id(request.user)
        if branch_id:
            # Return all courses within branch for Branch Admin.
            if is_branch_admin(request.user):
                return qs.filter(branch_id=branch_id)

            # Return all own courses for Instructor.
            course_access_role = CourseAccessRole.objects.filter(user_id=request.user)
            return qs.filter(id__in=[accessible_course.course_id for accessible_course in course_access_role])

        return qs.none()

    def get_readonly_fields(self, request, obj=None):
        django_readonly = super().get_readonly_fields(request, obj)

        if not (is_system_admin(request.user) or request.user.is_superuser):
            return django_readonly + ('branch',)
        return django_readonly

    def save_model(self, request, obj, form, change):
        """
        Newly customized by FinzTrust
        This is to implicitly link course to the same branch as the creator's.
        """
        branch_id = get_user_branch_id(request.user)
        if branch_id:
            obj.branch_id = branch_id

        super().save_model(request, obj, form, change)


class CourseOverviewImageConfigAdmin(ConfigurationModelAdmin):
    """
    Basic configuration for CourseOverview Image thumbnails.

    By default this is disabled. If you change the dimensions of the images with
    a new config after thumbnails have already been generated, you need to clear
    the entries in CourseOverviewImageSet manually for new entries to be
    created.
    """
    list_display = [
        'change_date',
        'changed_by',
        'enabled',
        'large_width',
        'large_height',
        'small_width',
        'small_height'
    ]

    def get_list_display(self, request):
        """
        Restore default list_display behavior.

        ConfigurationModelAdmin overrides this, but in a way that doesn't
        respect the ordering. This lets us customize it the usual Django admin
        way.
        """
        return self.list_display


class CourseOverviewImageSetAdmin(admin.ModelAdmin):
    """
    Thumbnail images associated with CourseOverviews. This should be used for
    debugging purposes only -- e.g. don't edit these values.
    """
    list_display = [
        'course_overview',
        'small_url',
        'large_url',
    ]
    search_fields = ['course_overview__id']
    readonly_fields = ['course_overview_id']
    fields = ('course_overview_id', 'small_url', 'large_url')


class SimulateCoursePublishConfigAdmin(ConfigurationModelAdmin):
    pass


admin.site.register(CourseOverview, CourseOverviewAdmin)
admin.site.register(CourseOverviewImageConfig, CourseOverviewImageConfigAdmin)
admin.site.register(CourseOverviewImageSet, CourseOverviewImageSetAdmin)
admin.site.register(SimulateCoursePublishConfig, SimulateCoursePublishConfigAdmin)
