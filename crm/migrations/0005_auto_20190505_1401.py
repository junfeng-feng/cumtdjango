# Generated by Django 2.2.1 on 2019-05-05 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0004_minedetail_mine_gas_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='minedetail',
            name='work_instruction_document',
            field=models.FilePathField(default='空', verbose_name='作业指导文件'),
        ),
        migrations.AlterField(
            model_name='minedetail',
            name='mine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Mine', verbose_name='矿井名称'),
        ),
    ]
