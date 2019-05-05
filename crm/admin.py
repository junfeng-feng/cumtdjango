from django.contrib import admin

# Register your models here.

from .models import Project
from .models import Mine
from .models import MineDetail


# Register your models here.
class ProjectConfigAdmin(admin.ModelAdmin):   
    #要显示的字段列表
    list_display = ['project_name']   
    #要搜索的字段列表
    search_fields = ['project_name']
    list_filter = ['project_name']
    #max show count
    list_max_show_all = 20

admin.site.register(Project, ProjectConfigAdmin)

# Register your models here.
class MineConfigAdmin(admin.ModelAdmin):   
    #要显示的字段列表
    list_display = ['project', 'mine_name']   
    #要搜索的字段列表
    search_fields = ['project', 'mine_name']
    list_filter = ['project', 'mine_name']
    #max show count
    list_max_show_all = 20

admin.site.register(Mine, MineConfigAdmin)


# Register your models here.
class MineDetailConfigAdmin(admin.ModelAdmin):   
    #要显示的字段列表
    list_display = ['mine','project_role','mine_status','mine_gas_grade','work_instruction_document']   
    #要搜索的字段列表
    search_fields = ['mine','project_role','mine_status']
    list_filter = ['mine']
    #max show count
    list_max_show_all = 2

admin.site.register(MineDetail, MineDetailConfigAdmin)
