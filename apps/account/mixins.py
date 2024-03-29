# Core imports.
from django.contrib.auth.mixins import LoginRequiredMixin


class AuthorAccessMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.groups.filter(name='author').exists() or request.user.is_superuser:
                return super().dispatch(request, *args, **kwargs)
            else:
                return self.handle_no_permission()
        else:
            return self.handle_no_permission()
