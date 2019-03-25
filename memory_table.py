import getpass
from collections import Counter

import psutil
from psutil import ZombieProcess, AccessDenied

from utils import convert_value

if __name__ == '__main__':

    username = getpass.getuser()
    mem_dict = dict()
    for proc in list(filter(lambda x: x.username() == username, psutil.process_iter())):
        try:
            name = proc.name()
            cpu = proc.cpu_percent()
            mem = proc.memory_info().rss
            if name in mem_dict:
                mem_dict[name] = round(mem_dict[name] + mem, 3)
            else:
                mem_dict[name] = mem
        except ZombieProcess:
            pass
        except AccessDenied:
            pass

    top_three = Counter(mem_dict)
    for (proc, memory) in top_three.most_common(3):
        print(proc, "{0} {1}".format(*convert_value(memory)))
