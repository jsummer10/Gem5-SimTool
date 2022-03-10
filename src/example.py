"""
Project     : SimTool
Authors     : Jake Summerville
File        : example.py
Description : An example to run through the simulation
"""

import os
import logging
import simconfig


def example1():
    """ Run example simulation """

    predictor_list = ['LocalBP', 'BiModeBP', 'MultiperspectivePerceptron8KB', 'MultiperspectivePerceptron64KB', 'TournamentBP']
    benchmark_list = ['a2time01', 'cacheb01', 'bitmnp01', 'mcf', 'libquantum']

    sim_queue = []

    for predictor in predictor_list:
        os.makedirs('m5out/simtool_data/example/' + predictor + '/', exist_ok=True)
        for benchmark in benchmark_list:
            sim = simconfig.SimConfig(predictor, benchmark, 'simtool_data/example/' + predictor + '/')
            sim_queue.append(sim)

    return sim_queue