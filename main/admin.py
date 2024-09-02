from django.contrib import admin
from .models import Center, ControlCard, Group, Reporter, DocumentType, AuthorResolution, TypeSolution, Letter, \
    CheckFile, ControlFile, Manager


class CenterAdmin(admin.ModelAdmin):
    list_display = ('name', 'short', 'user')
    search_fields = ('name', 'short')
    list_filter = ('user__is_superuser', 'user__is_staff')
    ordering = ('name', 'short')


class ControlCardAdmin(admin.ModelAdmin):
    list_display = ('name', 'create_at', 'update_at')
    search_fields = ('name', 'create_at', 'update_at')
    ordering = ('name', 'create_at', 'update_at')


class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'create_at', 'update_at')
    search_fields = ('name', 'create_at', 'update_at')
    ordering = ('name', 'create_at', 'update_at')


class ReporterDocumentTypeAuthorTypeSolutionAdmin(admin.ModelAdmin):
    list_display = ('name', 'create_at', 'update_at')
    search_fields = ('name', 'create_at', 'update_at')
    ordering = ('name', 'create_at', 'update_at')


class LetterAdmin(admin.ModelAdmin):
    list_display = ('control_card', 'group', 'document_type', 'registration_number', 'document_number')
    search_fields = ('control_card', 'group', 'reporter', 'document_type')
    ordering = ('control_card', 'group', 'document_type', 'registration_number', 'document_number')


class CheckFileAdmin(admin.ModelAdmin):
    list_display = ('id', 'file', 'create_at', 'update_at')
    search_fields = ('file', 'create_at', 'update_at')
    ordering = ('file', 'create_at', 'update_at')


class ControlFileAdmin(admin.ModelAdmin):
    list_display = ('id', 'file', 'create_at', 'update_at')
    search_fields = ('file', 'create_at', 'update_at')
    ordering = ('file', 'create_at', 'update_at')


class ManagerAdmin(admin.ModelAdmin):
    list_display = ('id', 'center', 'letter', 'lifetime', 'control')
    search_fields = ('center', 'letter', 'lifetime')
    ordering = ('id', 'letter', 'lifetime', 'control')


admin.site.register(Center, CenterAdmin)
admin.site.register(ControlCard, ControlCardAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Reporter, ReporterDocumentTypeAuthorTypeSolutionAdmin)
admin.site.register(DocumentType, ReporterDocumentTypeAuthorTypeSolutionAdmin)
admin.site.register(AuthorResolution, ReporterDocumentTypeAuthorTypeSolutionAdmin)
admin.site.register(TypeSolution, ReporterDocumentTypeAuthorTypeSolutionAdmin)
admin.site.register(Letter, LetterAdmin)
admin.site.register(CheckFile, CheckFileAdmin)
admin.site.register(ControlFile, ControlFileAdmin)
admin.site.register(Manager, ManagerAdmin)
