from django.db import models
from django.utils.safestring import mark_safe
from django.conf import settings
import json
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Project(models.Model):
    project_name = models.CharField(max_length=256, unique = True, verbose_name='项目名称')

    def __str__(self):
        return self.project_name

    class Meta:
        verbose_name = "项目名称"
        verbose_name_plural = "项目名称"

class Mine(models.Model):
    mine_name = models.CharField(max_length=256, unique = True, verbose_name='矿井名称')

    def __str__(self):
        return self.mine_name

    class Meta:
        verbose_name = "试验矿井名称"
        verbose_name_plural = "试验矿井名称"

class MineDetail(models.Model):
    MINE_GAS_GRADE = (
          (u'hybrid', u'煤与瓦斯突出矿井'),
          (u'hign', u'高瓦斯矿井'),
          (u'low', u'低瓦斯矿井'),
          (u'other', u'其他灾害情况')
      )
    YES_NO = (
          (u'是', u'是'),
          (u'否', u'否')
     )

    def get_project(self):
        return self.mine.project
        
    project = models.ForeignKey(Project, on_delete=models.CASCADE, default='1', verbose_name='项目名称')
    mine = models.ForeignKey(Mine, on_delete=models.CASCADE, default='1', verbose_name='矿井名称')

    project_role = models.CharField(max_length=256,default='',  blank=True,  verbose_name='项目作用')
    mine_status = models.CharField(max_length=256, default='', blank=True, verbose_name='矿井状态')
    mine_gas_grade = models.CharField(max_length=256, default='low', blank=True, verbose_name='矿井瓦斯等级', choices=MINE_GAS_GRADE)

    geological_condition = models.TextField(max_length=4096, default='',blank=True, verbose_name='地质条件')
    coal_seam_occurrence = models.TextField(max_length=4096 , default='',blank=True, verbose_name='煤层赋存')
    mining_order_method_process = models.TextField(max_length=4096, default='',blank=True, verbose_name='开采顺序、方法、工艺')
    gas_storage = models.TextField(max_length=4096,default='', blank=True,  verbose_name='瓦斯赋存')
    staff_composition_quality = models.TextField(max_length=4096, default='', blank=True, verbose_name='人员构成及素质')
    staff_technical_foundation = models.TextField(max_length=4096, default='', blank=True, verbose_name='人的技术基础')

    process_adaptation_conditions = models.TextField(max_length=4096, default='', blank=True, verbose_name='工艺适应条件')
    implementation_period = models.TextField(max_length=4096, default='', blank=True, verbose_name='实施工期')
    whether_it_is_necessary = models.TextField(max_length=4096, default='是', blank=True, verbose_name='是否需分别在煤、岩层中施工',choices=YES_NO)
    technical_complexity = models.TextField(max_length=4096, default='', blank=True, verbose_name='技术复杂程度')
    impact_on_mine_production_system = models.TextField(max_length=4096, default='', blank=True, verbose_name='对矿井生产系统布局和采掘施工的影响')

    technical_description = models.TextField(max_length=4096, default='', blank=True, verbose_name='技术描述')
    technical_characteristics = models.TextField(max_length=4096, default='', blank=True, verbose_name='技术特征')
    quantitative_effect_achieved = models.TextField(max_length=4096, default='', blank=True, verbose_name='达到的量化效果')

    organization = RichTextUploadingField(max_length=40960, default='', blank=True, verbose_name='组织机构')
    management_responsibility = models.TextField(max_length=4096, default='', blank=True, verbose_name='管理职责')
    resource_matching = models.TextField(max_length=4096, default='', blank=True, verbose_name='资源配套')

    work_link = models.TextField(max_length=4096, default='', blank=True, verbose_name='工作环节')
    technical_process_control_document = models.TextField(max_length=4096, default='', blank=True, verbose_name='技术过程控制文件')
    job_control_program = RichTextUploadingField(max_length=40960, default='', blank=True, verbose_name='作业控制程序')


    the_best_technical_indicators_and_standards = models.TextField(max_length=4096, default='', blank=True, verbose_name='达到的最佳技术指标及标准')
    the_best_time_standard = models.TextField(max_length=4096, default='', blank=True, verbose_name='完成效果的最佳时间标准')
    quantity_of_work = models.TextField(max_length=4096, default='', blank=True, verbose_name='工程量')

    work_instruction_document = models.FileField(upload_to='upload/%Y/%m/%d/%H/%M/%S', blank=True, verbose_name='作业指导文件')
    operating_procedure = models.FileField(upload_to='upload/%Y/%m/%d/%H/%M/%S', blank=True, verbose_name='操作规程')
    

    def __str__(self):
        return self.project.project_name

    class Meta:
        unique_together=("mine", "project")
        verbose_name = "试验矿井"
        verbose_name_plural = '试验矿井'
