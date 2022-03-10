"""
Project     : SimTool
Authors     : Jake Summerville
File        : SimConfig.py
Description : Used to run gem5 simulations
"""

import subprocess, os, time, logging
from datetime import datetime

class SimConfig():
    """ This class configures the cpu configuration for the
        simulation
    """
    def __init__(self, predictor, benchmark, data_dir, L2 = False):
        self.setCPU()
        self.setL1Cache()
        self.setL2Cache()
        self.setOpts(predictor, benchmark, data_dir, L2)


    def setCPU(self):
        """ This function set CPU related settings """
        cpu_clock  = '1.6GHz'
        cpu_type   = 'O3_ARM_v7a_3'
        core_count = '1'

        self.cpu_opts = ['--cpu-clock=' + cpu_clock,
                         '--cpu-type=' + cpu_type,
                         '-n', core_count]


    def setL1Cache(self):
        """ This function set L1 Cache related settings """
        L1_icache_size='32kB'
        L1_icache_assoc='4'

        L1_dcache_size='32kB'
        L1_dcache_assoc='4'

        cache_line_size='64'

        self.L1_cache_opts = ['--caches',
                              '--l1i_size=' + L1_icache_size,
                              '--l1i_assoc=' + L1_icache_assoc,
                              '--l1d_size=' + L1_dcache_size,
                              '--l1d_assoc=' + L1_dcache_assoc,
                              '--cacheline_size=' + cache_line_size]


    def setL2Cache(self):
        """ This function set L2 Cache related settings.
            Note: not necessary for all applications
        """
        L2_cache_size='1MB'
        L2_cache_assoc='8'

        self.L2_cache_opts = ['--l2cache',
                              '--l2_size=' + L2_cache_size,
                              '--l2_assoc=' + L2_cache_assoc]


    def setOpts(self, predictor, benchmark, data_dir, L2 = False):
        """ Purpose : This function sets the run opts
            @param predictor - predictor type (e.g. LocalBP)
            @param benchmark - benchmark type (e.g. a2time01)
            @param data_dir  - the data directory for stats/config
            @param L2        - whether to include L2 cache or not
        """

        self.config_name = predictor + '_' + benchmark

        if self.cpu_opts is None or self.L1_cache_opts is None:
            print('Unable to run', benchmark, 'for predictor', predictor)

        self.stats_file  = data_dir + 'stats_' + predictor + '_' + benchmark + '.txt'
        config_file = data_dir + 'config_' + predictor + '_' + benchmark + '.ini'

        self.run_opts = ['build/ARM/gem5.opt',
                    '--stats-file=' + self.stats_file,
                    '--dump-config=' + config_file]

        self.run_opts += ['configs/example/se.py']
        self.run_opts += self.L1_cache_opts

        if L2:
          self.run_opts += self.L2_cache_opts  

        self.run_opts += self.cpu_opts
        self.run_opts += ['--maxinsts=100000000']
        self.run_opts += ['--bench', benchmark]
        self.run_opts += ['--bp-type=' + predictor]


    def Run(self):
        """ This function runs the architecture configuration
            through a gem5 simulation
        """

        print('Running test: ' + self.config_name + '...')

        logging.info('\n-----------------------------------------------\n')
        logging.info('Test ' + self.config_name + '\n\n')

        # Run the simulation
        result = subprocess.run(self.run_opts, capture_output=True)

        # Write the output to the log file
        logging.info(result.stderr.decode('utf-8'))
        logging.info('')
        logging.info(result.stdout.decode('utf-8'))

        if not os.path.isfile('m5out/' + self.stats_file):
            print(self.config + ' Failed -> See Log\n')

