#!/bin/bash

process_id=$1
list_file=${@:2}
for file_xyz in ${list_file[@]}
do
    export id_sim=$(basename "${file_xyz%.xyz}")
    $ovitos cluster_separation.py
    $ovitos particle_analyze.py
    for file in ${path_new_xyz}/${id_sim}_*.xyz
    do
        export id_cluster=$(basename "${file%.xyz}")
        export path_processus="../Data/Data_HRTEM/${process_id}"
        mkdir -p $path_processus

        ./xyz_to_cel.py
        ./create_msa_prm.py
        ./create_wav_prm.py

        celslc -cel ${path_processus}/${id_cluster}.cel -slc ${path_processus}/slice -nx $nx -ny $ny -nz $nz -ht $electron_energy -dwf -abs
        msa -prm ${path_processus}/msa.prm -out ${path_processus}/msa.wav /ctem
        mv ${path_processus}/msa_*.wav ${path_processus}/msa.wav
        wavimg -prm ${path_processus}/wavimg.prm -out ${path_processus}/image.dat
        ./hrtem_image.py

        mv ${path_processus}/image.png ${path_img}/${id_cluster}.png
        rm -r $path_processus
    done
done
