from rest_framework import permissions
from .permissions import IsStaffEditorPermission


# WILL BE APPLIED TO ANY VIEW HOW INHERITES FROM IT
class StaffEditorPermissionMixin():
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

    # might be use for avoid overwrite with queryset = Model.objects.all() OR serializer_class = 

class UserQuerySetMixin():
    user_field = 'user'
    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        lookup_data = {}
        lookup_data[self.user_field] = user
        qs = super().get_queryset(*args,**kwargs)
        #if user.is_staff:
        #    return qs
        return qs.filter(**lookup_data)