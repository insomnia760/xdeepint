import fire
import glob
import pandas as pd


def ipinyou_random_split(
    source_file_dir,
    train_file_name, test_file_name
):
    # Training Files
    train_feature_filenames = sorted(glob.glob(source_file_dir+'train_input_*'))
    train_label_filenames = sorted(glob.glob(source_file_dir+'train_output_*'))

    assert len(train_feature_filenames) == len(train_label_filenames)
    num_train_files = len(train_feature_filenames)

    train_df_list = []
    for i in range(0, num_train_files, +1):
        train_feature = pd.read_hdf(train_feature_filenames[i])
        train_label = pd.read_hdf(train_label_filenames[i])
        train_feature_label = pd.concat([train_feature, train_label], axis=1)
        train_df_list.append(train_feature_label)
    train_df = pd.concat(train_df_list, axis=0)

    # Testing Files
    test_feature_filenames = sorted(glob.glob(source_file_dir+'test_input_*'))
    test_label_filenames = sorted(glob.glob(source_file_dir+'test_output_*'))

    assert len(test_feature_filenames) == len(test_label_filenames)
    num_test_files = len(test_feature_filenames)

    test_df_list = []
    for i in range(0, num_test_files, +1):
        test_feature = pd.read_hdf(test_feature_filenames[i])
        test_label = pd.read_hdf(test_label_filenames[i])
        test_feature_label = pd.concat([test_feature, test_label], axis=1)
        test_df_list.append(test_feature_label)
    test_df = pd.concat(test_df_list, axis=0)

    # Writing
    train_df.to_csv(train_file_name, index=False)
    test_df.to_csv(test_file_name, index=False)

if __name__ == "__main__":
    fire.Fire({
        "ipinyou_random_split": ipinyou_random_split
    })
