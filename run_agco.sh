#!/bin/bash

atom_typ1="Ag"
atom_typ2="Co"

export path_xyz="../Data/MD_data/${atom_typ1}${atom_typ2}/XYZ"
export path_processed="../Data/Data_processed"
export path_new_xyz="${path_processed}/XYZ"
export path_hrtem="../Data/Data_HRTEM"
export path_img="${path_hrtem}/HRTEM_image"

mkdir -p $path_new_xyz $path_img
rm -f $path_processed/data.dat $path_hrtem/data.dat

export electron_energy=300
export nx=64
export ny=64
export nz=10


liste=("${path_xyz}"/*.xyz)
total=${#liste[@]}
n=$(( $total / 48 ))
rest=$(( $total % 48 ))
cpt=0
for i in {1..48}
do  
    n_file=$n
    if ((rest > 0 && i > 48 - rest)); then
        n_file=$(($n + 1))
    fi
    sub_list=("${liste[@]:$cpt:$n_file}")
    cpt=$(($cpt + $n_file))
    ./run.sh $i ${sub_list[@]} &
done

rm -f $path_hrtem/data_prov.dat