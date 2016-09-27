from resource_management import *
from resource_management.libraries.script.script import Script
import sys, os, glob,socket

# server configurations
config = Script.get_config()
service_packagedir = os.path.realpath(__file__).split('/scripts')[0]
java64_home = config['hostLevelParams']['java_home']
download_url=config['configurations']['config']['download.url']
packageweb_dir=config['configurations']['config']['packageweb.dir']
log_file=  config['configurations']['config']['log_file']

