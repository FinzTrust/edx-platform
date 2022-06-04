from django.conf import settings
from common.djangoapps.util.cache import cache


def get_user_branch_id(user):
    """
    This is for getting login user branch id.
    """
    from common.djangoapps.student.models import UserProfile

    try:
        if not user.is_authenticated:
            return []
    except:
        pass

    # TODO: Rewrite in Django
    key = f'user_branch_id_{user.id}'
    cache_expiration = 60 * 60  # one hour

    # Kill caching on dev machines -- we switch groups a lot
    branch_id = cache.get(key)
    if settings.DEBUG:
        branch_id = None

    if branch_id is None:
        user_profile = UserProfile.objects.get(user_id=user.id)
        branch_id = getattr(user_profile, 'branch_id')
        cache.set(key, branch_id, cache_expiration)

    return branch_id


def get_user_branch(user):
    """
    This is for getting login user branch information.
    """
    from common.djangoapps.student.models import UserProfile
    from openedx.features.branch.models import Branch

    if not user.is_authenticated:
        return []

    # TODO: Rewrite in Django
    key = f'user_branch_id_{user.id}'
    cache_expiration = 60 * 60  # one hour

    # Kill caching on dev machines -- we switch groups a lot
    branch_id = cache.get(key)
    if settings.DEBUG:
        branch_id = None

    branch = {}
    user_profile = UserProfile.objects.get(user_id=user.id)
    branch_id = getattr(user_profile, 'branch_id')
    if branch_id:
        cache.set(key, branch_id, cache_expiration)
        branch = Branch.objects.get(id=branch_id)

    return branch


def is_system_admin(user):
    """
    This is to figure out whether is System Admin or not
    """
    return [g.name for g in user.groups.all() if g.name == 'System Admin']


def is_branch_admin(user):
    """
    This is to figure out whether is Branch Admin or not
    """
    return [g.name for g in user.groups.all() if g.name == 'Branch Admin']
