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
    list_filter = ['project']
    #max show count
    list_max_show_all = 20

admin.site.register(Mine, MineConfigAdmin)


# Register your models here.
class MineDetailConfigAdmin(admin.ModelAdmin):   
    #要显示的字段列表
    list_display = ['mine','project_role','mine_status','mine_gas_grade',
        'geological_condition','coal_seam_occurrence', 'mining_order_method_process',
        'gas_storage','staff_composition_quality',
        'staff_technical_foundation',

        'process_adaptation_conditions',
        'implementation_period',
        'whether_it_is_necessary',
        'technical_complexity',
        'impact_on_mine_production_system',


        'technical_description',
        'technical_characteristics',
        'quantitative_effect_achieved',


        'organization',
        'management_responsibility',
        'resource_matching',

        'work_link',
        'technical_process_control_document',
        'job_control_program',

        'the_best_technical_indicators_and_standards',
        'the_best_time_standard',
        'quantity_of_work',

        'work_instruction_document_link',
        'operating_procedure_link']  

    #要搜索的字段列表
    search_fields = ['project_role','mine_status']
    list_filter = ['mine']
    #max show count
    list_max_show_all = 20

admin.site.register(MineDetail, MineDetailConfigAdmin)
