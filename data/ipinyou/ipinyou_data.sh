# Untar
tar -xvzf ./data/ipinyou/raw/ipinyou.tar \
--directory ./data/ipinyou/raw/

# Split
python ./src/utils/ipinyou_split.py ipinyou-random-split \
--source_file_dir="./data/ipinyou/raw/iPinYou-all/hdf/" \
--train_file_name="./data/ipinyou/csv/train.csv" \
--test_file_name="./data/ipinyou/csv/test.csv"
