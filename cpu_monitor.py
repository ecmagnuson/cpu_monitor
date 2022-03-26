import psutil

cpu_count = psutil.cpu_count()

with open('core_monitor.csv', 'w') as f:
    for i in range(1, cpu_count + 1):
        f.write('core' + str(i) + ', ')
    f.write('\n') 

with open('core_monitor.csv', 'a') as f:
    while True:
        str_cpu = str(psutil.cpu_percent(interval=1, percpu=True))
        f.write(str_cpu[1:-1] + '\n')