import nidaqmx
import csv
from datetime import datetime,date
import os

task1 = nidaqmx.system.storage.persisted_task.PersistedTask('brandttemptask').load()
task1.timing.adc_sample_high_speed()
today = datetime.now()
date = today.strftime("%Y-%m-%d")
nidaqmx._task_modules.ai_channel_collection.AIChannelCollection
iteration = 1

while os.path.exists('nidaq_client/Logs/{}_thrmcpllog_{}.csv'.format(date,iteration)):
    iteration += 1

with open('nidaq_client/Logs/{}_thrmcpllog_{}.csv'.format(date,iteration),'w',newline='') as write_file:
    while True:
        csv_writer = csv.writer(write_file, delimiter= ',')
        csv_writer.writerow([datetime.now().strftime("%H:%M:%S.%f")[:-3],"%.03f" % task1.read()])

write_file.close()
task1.close()