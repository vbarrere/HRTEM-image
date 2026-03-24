#!/usr/bin/python3

import os

import matplotlib.pyplot    as plt
import numpy                as np

path_id_sim = os.getenv('path_id_sim')
path_processed = os.getenv('path_processed')
path_hrtem = os.getenv("path_hrtem")

path_processus = os.getenv("path_processus")
id_cluster = os.getenv("id_cluster")

data = np.fromfile(os.path.join(path_processus, 'image.dat'), dtype=np.float32)
nx = int(os.getenv('nx'))
ny = int(os.getenv('ny'))
counts = np.random.uniform(500, 1000)
#image = np.random.poisson(counts*data.reshape((nx, ny)))
image = data.reshape((nx, ny))

plt.imshow(image, cmap='gray')
plt.axis('off')
plt.savefig(os.path.join(path_processus, 'image.png'), bbox_inches='tight', pad_inches=0)


dtype = np.dtype([('i_sim', 'U10'), ('n_atoms', int), ("nat1", int), ("nat2", int), ('n_steps', int), ('initial_temperature', float), ("epot", float), ("surface_area", float), ("solid_volume", float), ("cna_others", int), ("cna_fcc", int), ("cna_hcp", int), ("cna_bcc", int), ("cna_ico", int), ("bond_angle_others", int), ("bond_angle_fcc", int), ("bond_angle_hcp", int), ("bond_angle_bcc", int), ("bond_angle_ico", int), ("d_com", float), ("gyration_radius", float), ("nat1_out", int), ("nat2_out", int), ("nat1_in", int), ("nat2_in", int), ("r_cm_x", float), ("r_cm_y", float), ("r_cm_z", float), ("r_cm1_x", float), ("r_cm1_y", float), ("r_cm1_z", float), ("r_cm2_x", float),("r_cm2_y", float),("r_cm2_z", float),("csp", float), ("image_shift_x", float), ("image_shift_y", float), ("defocus_x", float), ("defocus_y", float), ("two_fold_astigmatism_x", float), ("two_fold_astigmatism_y", float), ("coma_x", float), ("coma_y", float), ("three_fold_astigmatism_x", float), ("three_fold_astigmatism_y", float), ("spherical_aberration_x", float), ("spherical_aberration_y", float), ("star_aberration_x", float), ("star_aberration_y", float)])

md_data = np.genfromtxt(os.path.join(path_hrtem, "data_prov.dat"), dtype=dtype)
index = np.where(md_data['i_sim'] == id_cluster)[0]
param = md_data[index[0]]

data_file = os.path.join(path_hrtem, "data.dat")
if not os.path.exists(data_file):
    with open(data_file, "w") as f:
        print("i_sim", "n_atoms", "nat1", "nat2", "n_steps", "initial_temperature", "epot", "surface_area", "solid_volume", "cna_others", "cna_fcc", "cna_hcp", "cna_bcc", "cna_ico", "bond_angle_others", "bond_angle_fcc", "bond_angle_hcp", "bond_angle_bcc", "bond_angle_ico", "d_com", "gyration_radius", "nat1_out", "nat2_out", "nat1_in", "nat2_in", "r_cm_x", "r_cm_y", "r_cm_z", "r_cm1_x", "r_cm1_y", "r_cm1_z", "r_cm2_x", "r_cm2_y", "r_cm2_z", "csp", "image_shift_x", "image_shift_y", "defocus_x", "defocus_y", "two_fold_astigmatism_x", "two_fold_astigmatism_y", "coma_x", "coma_y", "three_fold_astigmatism_x", "three_fold_astigmatism_y", "spherical_aberration_x", "spherical_aberration_y", "star_aberration_x", "star_aberration_y", "counts", sep="\t", file=f)
        print(param['i_sim'], param['n_atoms'], param['nat1'], param['nat2'], param['n_steps'], param['initial_temperature'], param['epot'], param['surface_area'], param['solid_volume'], param['cna_others'], param['cna_fcc'], param['cna_hcp'], param['cna_bcc'], param['cna_ico'], param['bond_angle_others'], param['bond_angle_fcc'], param['bond_angle_hcp'], param['bond_angle_bcc'], param['bond_angle_ico'], param['d_com'], param['gyration_radius'], param['nat1_out'], param['nat2_out'], param['nat1_in'], param['nat2_in'], param['r_cm_x'], param['r_cm_y'], param['r_cm_z'], param['r_cm1_x'], param['r_cm1_y'], param['r_cm1_z'], param['r_cm2_x'], param['r_cm2_y'], param['r_cm2_z'], param["csp"], param['image_shift_x'], param['image_shift_y'], param['defocus_x'], param['defocus_y'], param['two_fold_astigmatism_x'], param['two_fold_astigmatism_y'], param['coma_x'], param['coma_y'], param['three_fold_astigmatism_x'], param['three_fold_astigmatism_y'], param['spherical_aberration_x'], param['spherical_aberration_y'], param['star_aberration_x'], param['star_aberration_y'], counts, sep="\t", file=f)
else:
    with open(data_file, "a") as f:
        print(param['i_sim'], param['n_atoms'], param['nat1'], param['nat2'], param['n_steps'], param['initial_temperature'], param['epot'], param['surface_area'], param['solid_volume'], param['cna_others'], param['cna_fcc'], param['cna_hcp'], param['cna_bcc'], param['cna_ico'], param['bond_angle_others'], param['bond_angle_fcc'], param['bond_angle_hcp'], param['bond_angle_bcc'], param['bond_angle_ico'], param['d_com'], param['gyration_radius'], param['nat1_out'], param['nat2_out'], param['nat1_in'], param['nat2_in'], param['r_cm_x'], param['r_cm_y'], param['r_cm_z'], param['r_cm1_x'], param['r_cm1_y'], param['r_cm1_z'], param['r_cm2_x'], param['r_cm2_y'], param['r_cm2_z'], param["csp"], param['image_shift_x'], param['image_shift_y'], param['defocus_x'], param['defocus_y'], param['two_fold_astigmatism_x'], param['two_fold_astigmatism_y'], param['coma_x'], param['coma_y'], param['three_fold_astigmatism_x'], param['three_fold_astigmatism_y'], param['spherical_aberration_x'], param['spherical_aberration_y'], param['star_aberration_x'], param['star_aberration_y'], counts, sep="\t", file=f)
