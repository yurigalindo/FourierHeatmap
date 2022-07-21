BLACK_LIST = "/media/4TB/datasets/ILSVRC2015/ILSVRC2015/devkit/data/ILSVRC2015_clsloc_validation_blacklist.txt"
VAL_CLASS_PATH = "/media/4TB/datasets/ILSVRC2015/ILSVRC2015/devkit/data/ILSVRC2015_clsloc_validation_ground_truth.txt"
 
VAL_DATA_PATH = "/media/4TB/datasets/ILSVRC2015/ILSVRC2015/Data/CLS-LOC/val/"
 
VAL_ORI_DATA_PATH = "/media/4TB/datasets/ILSVRC2015/ILSVRC2015/Data/CLS-LOC/val_original/*.JPEG"
 
black_list = []
 
with open(BLACK_LIST) as b_file:
    rows = b_file.readlines()
    for row in rows:
        row = int(row.strip())
        black_list.append(row)

val_class = []
 
with open(VAL_CLASS_PATH) as val_file:
    rows = val_file.readlines()
    for row in rows:
        row = int(row.strip())
        val_class.append(row)

val_files = glob.glob(VAL_ORI_DATA_PATH)
 
for file in val_files:
    seq_num = int(file.split("/")[-1].split("_")[-1].split(".")[0])
    if seq_num not in black_list:
        class_id = val_class[seq_num - 1]
        class_name = id_class_map[class_id]
 
        if not os.path.isdir(VAL_DATA_PATH + class_name):
            os.mkdir(VAL_DATA_PATH + class_name)
 
        os.rename(file, VAL_DATA_PATH + class_name + "/" + file.split("/")[-1])