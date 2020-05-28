import os
from datetime import datetime

today = datetime.now()
date = today.strftime("%d-%m-%Y")

os.popen("mysqldump --user=root --password=rootdevops --databases devops > dump/devops_dump_"+str(date)+".sql")

print("Dump généré")
