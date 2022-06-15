from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "git_sync.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import git_sync.users.signals  # noqa F401
        except ImportError:
            pass
