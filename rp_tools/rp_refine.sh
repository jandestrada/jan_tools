out_dir=$1 # which folder contains the data for this
echo "using $out_dir"

cd $out_dir


scp -r ~/templates/DE-GSM ./
scp ./output_geodesic.xyz ./DE-GSM/
scp ./endpoints.xyz ./DE-GSM
sbatch DE-GSM/refine.sh


cd - 
