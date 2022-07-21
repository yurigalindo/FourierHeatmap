for D in ../deep_feature_reweighting/waterbirds/*; do
    if [ -d "${D}" ]; then
        CLASS=$(basename $D)
        mkdir -p data/waterbirds/$CLASS
        ls $D | shuf -n 1 | xargs -i cp $D/{} data/waterbirds/$CLASS
    fi
done