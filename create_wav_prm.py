#!/usr/bin/python3

import os
import numpy as np

nx = int(os.getenv('nx'))
ny = int(os.getenv('ny'))
electron_energy = float(os.getenv('electron_energy'))
#file_cel = os.getenv('file_cel')

path_id_sim = os.getenv('path_id_sim')
path_processed = os.getenv('path_processed')
path_hrtem = os.getenv("path_hrtem")
path_processus = os.getenv("path_processus")
id_cluster = os.getenv("id_cluster")

with open(os.path.join(path_processus, f"{id_cluster}.cel"), 'r') as cel_file:
    lines = cel_file.readlines()
    line = lines[1].split()
    a = float(line[1])
    b = float(line[2])

aberrations = [[0.0, 0.0],    # image shift
               [-4.0, -8.0],  # defocus
               [0.0, 0.0],    # astigmatism
               [0.0, 0.0],    # coma
               [0.0, 0.0],    # three-lobe aberration
               [0.0, 0.0],    # spherical aberration
               [0.0, 0.0]]    # star aberration
aberrations = np.array(aberrations)
aberrations_values = np.zeros_like(aberrations)

with open(os.path.join(path_processus, 'wavimg.prm'), "w") as f:
    print(f"'{os.path.join(path_processus, 'msa.wav')}'", file=f)      # line 1
    print(f"{nx} {ny}", file=f)
    print(f"{a/nx} {b/ny}", file=f)
    print(f"{electron_energy}", file=f)
    print(f"{0}", file=f)               # line 5
    print(f"'{os.path.join(path_processus, 'image.dat')}'", file=f)
    print(f"{nx} {ny}", file=f)
    print(f"{0} {1.0} {1.0} {0.0}", file=f)
    print(f"{0}", file=f)
    print(f"{0.0}", file=f)            # line 10
    print(f"{0.0} {0.0}", file=f)
    print(f"{0.0}", file=f)
    print(f"{1}", file=f)
    print(f"{1} {3.8}", file=f)
    print(f"{1} {0.4}", file=f)        # line 15
    print(f"{0} {1.0} '{'mtf.dat'}'", file=f)
    print(f"{0} {1.0} {1.0} {0.0}", file=f)
    print(f"{len(aberrations)}", file=f)
    for i, abr in enumerate(aberrations):
        value = np.random.uniform(aberrations[i, 0], aberrations[i, 1])
        valx = value * np.cos(np.random.uniform(0, 2*np.pi))
        valy = value * np.sin(np.random.uniform(0, 2*np.pi))
        aberrations_values[i] = [valx, valy]
        print(f"{i} {valx} {valy}", file=f) 
    print(f"{250.0} {0.03}", file=f)   # line 19+Nabr
    print(f"{0.0} {0.0}", file=f)
    print(f"{0}", file=f)

dtype = np.dtype([('i_sim', 'U10'), ('n_atoms', int), ('nat1', int), ('nat2', int), ('n_steps', int), ('initial_temperature', float), ("epot", float), ("surface_area", float), ("solid_volume", float), ("cna_others", int), ("cna_fcc", int), ("cna_hcp", int), ("cna_bcc", int), ("cna_ico", int), ("bond_angle_others", int), ("bond_angle_fcc", int), ("bond_angle_hcp", int), ("bond_angle_bcc", int), ("bond_angle_ico", int), ("d_com", float), ("gyration_radius", float), ("nat1_out", int), ("nat2_out", int), ("nat1_in", int), ("nat2_in", int), ("r_cm_x", float), ("r_cm_y", float), ("r_cm_z", float), ("r_cm1_x", float), ("r_cm1_y", float), ("r_cm1_z", float), ("r_cm2_x", float),("r_cm2_y", float),("r_cm2_z", float),("csp", float)])

#i_sim = path_id_sim.split("/")[-1]
md_data = np.genfromtxt(os.path.join(path_processed, "data.dat"), dtype=dtype)
index = np.where(md_data['i_sim'] == id_cluster)[0]
param = md_data[index[0]]

data_file = os.path.join(path_hrtem, "data_prov.dat")
if not os.path.exists(data_file):
    with open(data_file, "w") as f:
        print("i_sim", "n_atoms", "nat1", "nat2", "n_steps", "initial_temperature", "epot", "surface_area", "solid_volume", "cna_others", "cna_fcc", "cna_hcp", "cna_bcc", "cna_ico", "bond_angle_others", "bond_angle_fcc", "bond_angle_hcp", "bond_angle_bcc", "bond_angle_ico", "d_com", "gyration_radius", "nat1_out", "nat2_out", "nat1_in", "nat2_in", "r_cm_x", "r_cm_y", "r_cm_z", "r_cm1_x", "r_cm1_y", "r_cm1_z", "r_cm2_x","r_cm2_y","r_cm2_z","csp" , "image_shift_x", "image_shift_y", "defocus_x", "defocus_y", "two_fold_astigmatism_x", "two_fold_astigmatism_y", "coma_x", "coma_y", "three_fold_astigmatism_x", "three_fold_astigmatism_y", "spherical_aberration_x", "spherical_aberration_y", "star_aberration_x", "star_aberration_y", sep="\t", file=f)
        print(param['i_sim'], param['n_atoms'], param["nat1"], param["nat2"], param['n_steps'], param['initial_temperature'], param['epot'], param['surface_area'], param['solid_volume'], param['cna_others'], param['cna_fcc'], param['cna_hcp'], param['cna_bcc'], param['cna_ico'], param['bond_angle_others'], param['bond_angle_fcc'], param['bond_angle_hcp'], param['bond_angle_bcc'], param['bond_angle_ico'], param['d_com'], param['gyration_radius'], param['nat1_out'], param['nat2_out'], param['nat1_in'], param['nat2_in'], param['r_cm_x'], param['r_cm_y'], param['r_cm_z'], param['r_cm1_x'], param['r_cm1_y'], param['r_cm1_z'], param['r_cm2_x'],param['r_cm2_y'],param['r_cm2_z'],param["csp"], aberrations_values[0][0], aberrations_values[0][1], aberrations_values[1][0], aberrations_values[1][1], aberrations_values[2][0], aberrations_values[2][1], aberrations_values[3][0], aberrations_values[3][1], aberrations_values[4][0], aberrations_values[4][1], aberrations_values[5][0], aberrations_values[5][1], aberrations_values[6][0], aberrations_values[6][1], sep="\t", file=f)
else:
    with open(data_file, "a") as f:
        print(param['i_sim'], param['n_atoms'], param["nat1"], param["nat2"], param['n_steps'], param['initial_temperature'], param['epot'], param['surface_area'], param['solid_volume'], param['cna_others'], param['cna_fcc'], param['cna_hcp'], param['cna_bcc'], param['cna_ico'], param['bond_angle_others'], param['bond_angle_fcc'], param['bond_angle_hcp'], param['bond_angle_bcc'], param['bond_angle_ico'], param['d_com'], param['gyration_radius'], param['nat1_out'], param['nat2_out'], param['nat1_in'], param['nat2_in'], param['r_cm_x'], param['r_cm_y'], param['r_cm_z'], param['r_cm1_x'], param['r_cm1_y'], param['r_cm1_z'], param['r_cm2_x'],param['r_cm2_y'],param['r_cm2_z'],param["csp"], aberrations_values[0][0], aberrations_values[0][1], aberrations_values[1][0], aberrations_values[1][1], aberrations_values[2][0], aberrations_values[2][1], aberrations_values[3][0], aberrations_values[3][1], aberrations_values[4][0], aberrations_values[4][1], aberrations_values[5][0], aberrations_values[5][1], aberrations_values[6][0], aberrations_values[6][1], sep="\t", file=f)
