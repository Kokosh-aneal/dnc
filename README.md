# Dynamic Name Changer
Simple tool written in python, which changes names of hosts in Zabbix via API. It uses names gathered by system.name key. 

## Installation
All you have to do is to add "dnc" tag with "1" value to hosts which you want to changed names dynamically and add script to cron. Cron executes script as often as user wants.
You can also create group dnc - it will be easier to recognise hosts with dnc tag.
