from my_utils import myutils

if __name__ == "__main__":
    test_data = [123, "hello", [1, 2, 3], {"key": "value"}]
    for data in test_data:
        data_type = myutils.checktype(data)
        print(f"The type of {data} is {data_type}")
