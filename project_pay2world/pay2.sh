#!/bin/bash
project_task_name="app_pay2world"
projectport=5030
supervisorctl stop $project_task_name
porttext=$(netstat -lnp | grep :$projectport)

IFS=' ' read -ra arrayll <<< $porttext
pt_length=${#arrayll[@]}
ptlast_value=${arrayll[length-1]}

IFS='/' read -ra ppl <<< $ptlast_value
pt_length=${#ppl[@]}
ppid=${ppl[0]}
kill -s 9 $ppid

supervisorctl start $project_task_name
