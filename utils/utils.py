import operator

from json_read import read_json

read_file = read_json()

filter_data = filter(None, read_file)
sort_by_date = sorted(filter_data, key=operator.itemgetter('date'), reverse=True)


def operation_executed():
    sorted_by_state = []
    for item in sort_by_date:
        if "EXECUTED" in item['state']:
            sorted_by_state.append(item["date"][:10] + " "
                                   + item["description"] + "\n"
                                   + str(item.get("from")) + " ---> "
                                   + item["to"] + "\n"
                                   + item['operationAmount']['amount']
                                   + item["operationAmount"]["currency"]["code"])
    return '\n'.join(str(el) for el in sorted_by_state[:5])



