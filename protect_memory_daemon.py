# Programa para proteção da memória ram
# Criado por: Luiz Gabriel Magalhães Trindade.
# Distribuído sob a licença GPL3.

import psutil
from time import sleep
import daemon

# Tempo de verificação
time_to_verify = 0.5
percent_to_use = 0.8

# Permitido usar até certa porcentagem da memória ram
memory_to_use = int(psutil.virtual_memory().total * percent_to_use)

def VerifyEnergyProfile():
    energy = psutil.sensors_battery().power_plugged
    if energy:
        sleep(0.5)
    else:
        sleep(1)

def VerifyMemory():
    all_processes = psutil.process_iter(attrs=["pid"])

    for process in all_processes:
        pid = process.info["pid"]
        process_pid = psutil.Process(pid)
        memory = int(process_pid.memory_info().rss)

        if memory >= memory_to_use:
            process_pid.terminate()

def Main():
        try:
            while True:
                VerifyMemory()
                VerifyEnergyProfile()
        except KeyboardInterrupt:
            exit()
            
if __name__ == "__main__":
    with daemon.DaemonContext():
        Main()
