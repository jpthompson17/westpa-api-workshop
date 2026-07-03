"""Demonstrates initializing and running a WESTPA + OpenMM simulation
using the new Python API. Usage::

    python -m init_and_run

"""
import logging
import os
import shutil

import mdtraj
import numpy as np
import westpa

logger = logging.getLogger(__name__)


def main():
    clean_up_previous_output()
    logging.basicConfig(filename='west.log', level=logging.INFO)

    topology_file = os.path.abspath('topol.top')
    initial_state = westpa.State(file=os.path.abspath('initial_state.gro'))

    simulation = westpa.Simulation(
        datafile='west.h5',
        propagator=propagator(topology_file),
        pcoord_calculator=pcoord_calculator,
        bin_mapper=bin_mapper(),
        bin_target_counts=5,
        source=westpa.Source(states=[initial_state]),
        sinks=westpa.Sink(indicator=is_bound, label='bound'),
    )

    simulation.initialize(states=[initial_state] * 5)
    simulation.run(n_iters=3)


def propagator(topology_file):
    return westpa.GromacsPropagator(
        topology_file,
        md_parameters={
            'integrator': 'sd',
            'dt': 0.002,
            'nsteps': 1000,
            'nstcomm': 500,
            'comm_mode': 'linear',
            'comm-grps': 'system',
            'ref_t': 300,
            'tau_t': 1.0,
            'tc_grps': 'System',
            'constraints': 'hbonds',
            'constraint_algorithm': 'LINCS',
            'coulombtype': 'PME',
            'fourierspacing': 0.1,
            'pme_order': 6,
            'ewald_rtol': 0.000001,
            'pbc': 'xyz',
            'rcoulomb': 0.9,
            'rcoulomb_switch': 0.9,
            'vdwtype': 'Cut-off',
            'vdw_modifier': 'Potential-switch',
            'rvdw': 0.9,
            'rvdw_switch': 0.8,
            'DispCorr': 'Ener',
            'nstlist': 20,
            'nstlog': 100,
            'nstcalcenergy': 100,
            'nstenergy': 100,
            'nstxout-compressed': 500,
        }
    )


def pcoord_calculator(segment):
    traj = mdtraj.load(segment.final_state.file)
    distances = mdtraj.compute_distances(traj, atom_pairs=[[0, 1]])
    segment.pcoord = distances * 10  # nanometer -> angstrom
    return segment


def bin_mapper():
    return westpa.RectilinearBinMapper(
        boundaries=[
            [0, 2.6, 2.8, 3, 3.2, 3.4, 3.6, 3.8, 4, 4.5, 5, 5.5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, np.inf]
        ],
    )


def is_bound(segment):
    return segment.pcoord[-1, 0] < 2.6


def clean_up_previous_output():
    for file in ['west.h5', 'west.log']:
        if os.path.exists(file):
            os.remove(file)
    if os.path.exists('traj_segs'):
        shutil.rmtree('traj_segs')


if __name__ == '__main__':
    main()
