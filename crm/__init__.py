from django.apps import AppConfig
import os

default_app_config = 'crm.CrmConfig'

def get_current_app_name(_file):
	return os.path.split(os.path.dirname(_file))[-1]