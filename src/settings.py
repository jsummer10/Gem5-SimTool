"""
Project     : SimTool
Authors     : Jake Summerville
File        : settings.py
Description : Used to describe the settings for the simulation
"""

#---------------
#      CPU
#---------------
CPU_CLOCK   = '1.6GHz'
CPU_TYPE    = 'O3_ARM_v7a_3'
CORE_COUNT  = '1'


#---------------
#   L1 Cache
#---------------

L1_CACHE_INCLUDE = True
L1_ICACHE_SIZE   = '32kB'
L1_ICACHE_ASSOC  = '4'
L1_DCACHE_SIZE   = '32kB'
L1_DCACHE_ASSOC  = '4'
CACHE_LINE_SIZE  = '64'


#---------------
#   L2 Cache
#---------------

L2_CACHE_INCLUDE = True
L2_CACHE_SIZE    = '1MB'
L2_CACHE_ASSOC   = '8'


#---------------
#     Other
#---------------

MAXINSTS    = '100000000'
