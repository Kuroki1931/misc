cql_alphas=(0.01 0.1 1 10)
temp=(0.01 0.1 1 10)
method_type=(0)

GPUS=(0 1 2 3)
NUM_GPUS=${#GPUS[@]}
NUM_REPEATS=4

# for number of experiments
INDEX_START=0
INDEX_END=$((INDEX_START + NUM_GPUS * NUM_REPEATS))
CURRENT_INDEX=0

echo "=========================================================="
echo "Running with $((${NUM_GPUS} * ${NUM_REPEATS})) parallel jobs"
echo "INDEX_START: $INDEX_START"
echo "INDEX_END: $INDEX_END"
echo "=========================================================="


for i in "${cql_alphas[@]}"
do
    for j in "${temp[@]}"
    do
        for k in "${method_type[@]}"
        do

            if [ $CURRENT_INDEX -ge $INDEX_START ] && [ $CURRENT_INDEX -lt $INDEX_END ]
            then
                WHICH_GPU=${GPUS[$((CURRENT_INDEX - INDEX_START)) % NUM_GPUS]}
                echo "=========================================================="
                echo "Running experiment $CURRENT_INDEX on GPU $WHICH_GPU"
                echo "CQL_ALPHA: $i"
                echo "TEMP: $j"
                echo "METHOD_TYPE: $k"
                echo "=========================================================="
                python train_offline.py agent=cql expl_agent=proto task=walker_run agent.alpha=$i agent.method_type=$k agent.method_temp=$j &
                sleep 5.0
            fi
            CURRENT_INDEX=$(($CURRENT_INDEX + 1))
        done
    done
done

