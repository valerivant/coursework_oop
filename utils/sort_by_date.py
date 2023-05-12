from utils.data_read import read_json


def sort_func():
    """функиция для сортировки данных по дате (выводит самые новые транзакиции по дате )"""
    filter_data = filter(None, read_json())
    sort_by_date = sorted(filter_data, key=lambda x: x['date'], reverse=True)
    return sort_by_date
