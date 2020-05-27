import os
from datetime import datetime

today = datetime.now()
date = today.strftime("%d-%m-%Y")

os.popen("mysqldump --user=root --password=rootdevops --no-data devops > devops_dump_"+str(date)+".sql")

print("Dump généré")
