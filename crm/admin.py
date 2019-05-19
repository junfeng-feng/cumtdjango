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
    list_display = [ 'mine_name']   
    #要搜索的字段列表
    search_fields = [ 'mine_name']
    list_filter = ['mine_name']
    #max show count
    list_max_show_all = 20

admin.site.register(Mine, MineConfigAdmin)

# Register your models here.
class MineDetailConfigAdmin(admin.ModelAdmin):   
    #要显示的字段列表
    list_display = [
    'mine','project',

    'project_role','mine_status','mine_gas_grade',

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


        #'organization',
        'management_responsibility',
        'resource_matching',

        'work_link',
        #'technical_process_control_document',
        'job_control_program',

        'the_best_technical_indicators_and_standards',
        'the_best_time_standard',
        'quantity_of_work',

        'work_instruction_document',
        'operating_procedure'

        ]  

    fieldsets = (
        ("基本信息", {'fields': ['mine', 'project']}),

        ("适用条件", {'fields': ['project_role', 'mine_status','mine_gas_grade']}),

        ("技术基础", {'fields': ['geological_condition','coal_seam_occurrence', 'mining_order_method_process',
                'gas_storage','staff_composition_quality',
                'staff_technical_foundation',]}),
                
        ("工艺特征", {'fields': [        'process_adaptation_conditions',
        'implementation_period',
        'whether_it_is_necessary',
        'technical_complexity',
        'impact_on_mine_production_system',
]}),

        ("技术描述方法及技术特征指标", {'fields': [        'technical_description',
        'technical_characteristics',
        'quantitative_effect_achieved',

]}),

        ("管理体系结构", {'fields': [        'organization',
        'management_responsibility',
        'resource_matching',

]}),
        ("过程控制管理", {'fields': [        'work_link',
        'technical_process_control_document',
        'job_control_program',
]}),

        ("作业指导文件", {'fields': ['work_instruction_document',
]}),
        ("操作规程", {'fields': [  
        'operating_procedure'
]}),

        ("技术管理效果评价标准", {'fields': ['the_best_technical_indicators_and_standards',
        'the_best_time_standard',
        'quantity_of_work',
]}),

    )
    #要搜索的字段列表
    search_fields = ['project_role','mine_status']
    list_filter = ['mine']
    #max show count
    list_max_show_all = 20
    #save_on_top = True
    preserve_filters = True

admin.site.register(MineDetail, MineDetailConfigAdmin)
