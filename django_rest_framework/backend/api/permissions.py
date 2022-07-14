from rest_framework import permissions


class IsStaffEditorPermission(permissions.DjangoModelPermissions):
    
    # AUGMENT DJANGOMODEL PERMISSIONS FOR REST EXPECIFIC FOR EACH METHOD POSSIBLE ON MODELS.

    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS':[],
        'HEAD':[],
        'POST':['%(app_label)s.add_%(model_name)s'],
        'PUT':['%(app_label)s.change_%(model_name)s'],
        'PATCH':['%(app_label)s.change_%(model_name)s'],
        'DELETE':['%(app_label)s.delete_%(model_name)s'],
    }

    # COMENTADO PORQUE SE PUEDEN AGREGAR MULTIPLES CLASES DE PERMISO -> REVISAR QUE permissions.IsAdminUser made the same.
    #def has_permission(self, request, view):
    #    if not request.user.is_staff: # same/for permission class IsAdminUser
    #        return False
    #    return super().has_permission(request, view)
    
    #def has_permission(self, request, view):
    #    user = request.user
    #    print(user.get_all_permissions())
    #    if user.is_staff:
    # IF USER HAS ANY OF THAT WILL BE TRUE
    #        if user.has_perm("productos.add_producto"): #"<app_name>.verbo_<model_name>"
    #            return True
    #        if user.has_perm("productos.change_producto"):
    #            return True
    #        if user.has_perm("productos.delete_producto"):
    #            return True
    #        if user.has_perm("productos.view_producto"):
    #            return True
    #        return False
    #    return False
