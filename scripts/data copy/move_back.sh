for D in imagenet100/moved_images/val/*; do
    if [ -d "${D}" ]; then
        CLASS=$(basename $D)
        ls $D | shuf -n 40 | xargs -i mv $D/{} imagenet100/val/$CLASS
    fi
done