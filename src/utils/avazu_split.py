import fire
import csv
import datetime


def avazu_random_split(
    source_file_name, train_ratio,
    train_file_name, test_file_name
):
    source_file = open(source_file_name, "r")
    train_file = open(train_file_name, "w")
    test_file = open(test_file_name, "w")

    source_file_reader = csv.DictReader(source_file)
    train_file_writer = csv.DictWriter(
        train_file,
        fieldnames=source_file_reader.fieldnames+['time_weekday', 'time_hour']
    )
    test_file_writer = csv.DictWriter(
        test_file,
        fieldnames=source_file_reader.fieldnames+['time_weekday', 'time_hour']
    )

    idx = 0
    train_file_writer.writeheader()
    test_file_writer.writeheader()

    for line in source_file_reader:

        time_list = [line['hour'][i:(i+2)] for i in (0, 2, 4, 6)]
        time_date = datetime.datetime(
            year=int('20'+time_list[0]),
            month=int(time_list[1]),
            day=int(time_list[2]),
            hour=int(time_list[3])
        )
        line['time_weekday'] = str(time_date.weekday())
        line['time_hour'] = str(time_date.hour)

        if float(idx) % 1000.0 / 1000.0 <= train_ratio:
            train_file_writer.writerow(line)
        else:
            test_file_writer.writerow(line)
        idx += 1

    source_file.close()
    train_file.close()
    test_file.close()

if __name__ == "__main__":
    fire.Fire({
        "avazu_random_split": avazu_random_split
    })
