
start=$1
end=$2

for (( i=$1; i<=$2; i++ ));
  do
  echo $i
  cd $i
  scp ~/scripts/bash_helpers/discover.sh ./
  sbatch discover.sh
  cd -
  sleep 1
  done
