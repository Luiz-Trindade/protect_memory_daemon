# Programa para proteção da memória ram
# Criado por: Luiz Gabriel Magalhães Trindade.
# Distribuído sob a licença GPL3.

import psutil
from time import sleep
from daemon import DaemonContext
from threading import Thread
from os import getpgid
from random import randint

percent_to_use = 0.8
memory_to_use = int(psutil.virtual_memory().total * percent_to_use)

def VerifyEnergyProfile():
    energy = psutil.sensors_battery().power_plugged
    sleep(0.5 if energy else randint(1, 2))

def VerifyMemory():
    all_processes = psutil.process_iter(attrs=["pid"])

    for process in all_processes:
        pid = process.info["pid"]
        process_pid = psutil.Process(pid)
        memory = int(process_pid.memory_info().rss)

        if memory >= memory_to_use and pid != getpid():
            try:
                process_pid.terminate()
            except: pass

def Main():
    with DaemonContext():
        try:
            while True:
                VerifyMemory()
                VerifyEnergyProfile()
        except KeyboardInterrupt:
            exit()
            

if __name__ == "__main__":
    main_thread = Thread(target=Main)

    try:
        main_thread.start()        
        main_thread.join()
    except:
        pass
