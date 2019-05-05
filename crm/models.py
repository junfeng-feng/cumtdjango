from django.db import models

# Create your models here.

class Project(models.Model):
    project_name = models.CharField(max_length=256, verbose_name='项目名称')

    def __str__(self):
        return self.project_name

    class Meta:
        verbose_name = "项目名称"
        verbose_name_plural = "项目名称"

class Mine(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='项目名称')
    mine_name = models.CharField(max_length=256, verbose_name='矿井名称')
    #votes = models.IntegerField(default=0)

    def __str__(self):
        return self.mine_name

    class Meta:
        verbose_name = "试验矿井名称"
        verbose_name_plural = "试验矿井名称"

class MineDetail(models.Model):
    MINE_GAS_GRADE = (
          (u'hybrid', u'煤与瓦斯突出矿井'),
          (u'hign', u'高瓦斯矿井'),
          (u'low', u'低瓦斯矿井')
      )
    YES_NO = (
          (u'是', u'是'),
          (u'否', u'否')
     )

    mine = models.ForeignKey(Mine, on_delete=models.CASCADE, verbose_name='矿井名称')
    project_role = models.CharField(max_length=256, verbose_name='项目作用')
    mine_status = models.CharField(max_length=256,default='空', verbose_name='矿井状态')
    mine_gas_grade = models.CharField(max_length=256, default='low',verbose_name='矿井瓦斯等级', choices=MINE_GAS_GRADE)
    #geological_condition = models.CharField(max_length=256, verbose_name='地质条件')
    #coal_seam_occurrence = models.CharField(max_length=256, verbose_name='煤层赋存')
    #mining_order_method_process = models.CharField(max_length=256, verbose_name='开采顺序、方法、工艺')
    #gas_storage = models.CharField(max_length=256, verbose_name='瓦斯赋存')
    #staff_composition_quality = models.CharField(max_length=256, verbose_name='人员构成及素质')
    
    work_instruction_document = models.FileField(upload_to='upload/%Y/%m/%d/%H/%M/%s', blank=True,verbose_name='作业指导文件')
    def __str(self):
        return self.mine

    class Meta:
        verbose_name = "试验矿井详情"
        verbose_name_plural = '试验矿井详情'