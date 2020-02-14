# Download and untar
unzip ./data/avazu/raw/all.zip -d ./data/avazu/raw/
gunzip -Ndk ./data/avazu/raw/train.gz

# Split
python ./src/utils/avazu_split.py avazu-random-split \
--source_file_name="./data/avazu/raw/train.csv" \
--train_ratio=0.80 \
--train_file_name="./data/avazu/csv/train.csv" \
--test_file_name="./data/avazu/csv/test.csv"
