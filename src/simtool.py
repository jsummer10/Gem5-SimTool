"""
Project     : SimTool
Authors     : Jake Summerville
File        : simtool.py
Description : Used to run gem5 simulations
"""

import subprocess, os, time, threading, logging
from datetime import datetime
import example

#------ IMPORTANT: Change to relevant gem5 path ------

PATHGEM5 = '~/simulation/gem5/'

#-----------------------------------------------------

exitFlag = 0

class myThread (threading.Thread):
    """ This class handles multithreading """
   def __init__(self, threadID, name, counter, simtool):
      threading.Thread.__init__(self)
      self.threadID  = threadID
      self.name      = name
      self.counter   = counter
      self.simtool   = simtool
   def run(self):
      self.simtool.Run()


def CreateLogFile():
    """ Create log file to be used during runtime """
    os.makedirs('m5out/simtool_data/logs', exist_ok=True)

    logging.basicConfig(filename='m5out/simtool_data/logs' + datetime.now().strftime("%Y%m%d_%H%M") + '.log', 
                        format='%(asctime)s - %(levelname)s: %(message)s', 
                        datefmt='%Y-%m-%d %H:%M:%S',
                        level=logging.DEBUG)


def StartSimulations(sim_queue):
    """ Run multithreaded simulations """
    threads = []

    count = 1
    for sim in sim_queue:
        thread = myThread(count, 'Thread-' + str(count), count, sim)
        thread.start()
        threads.append(thread)
        count += 1

    for thread in threads:
        thread.join()


def main():
    """ Main simtool function """
    start_time = time.time()
    os.chdir(PATHGEM5)
    CreateLogFile()

    print('\n-------------- Testing --------------\n')

    sim_queue = example.example1()
    StartSimulations(sim_queue)

    print('\n-------------------------------------\n')

    time_dif = (time.time() - start_time) / 60
    
    print('Testing Complete ({:.2f} minutes)\n'.format(time_dif))


if __name__ == '__main__':
    main()
    

