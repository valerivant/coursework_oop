import json
import operator

from json_read import read_json

filter_data = filter(None, read_json())
sort_by_date = sorted(filter_data, key=operator.itemgetter('date'), reverse=True)


# 8906171742833215

def operation_executed():
    sorted_by_state = []
    for item in sort_by_date:
        if "EXECUTED" in item['state']:
            card = str(item.get("from", "").split()[-1:])
            card_digit = "".join(c for c in card if c.isdigit())
            card_text = "".join(c for c in item.get("from", "") if c.isalpha())
            private_number = str(card_digit[:6]) + (len(card_digit[6:-4]) * "*") + str(card_digit[-4:])
            number_card = private_number[0:4] + " " + private_number[4:8] + " " + private_number[8:12] \
                          + " " + private_number[-4:]
            sorted_by_state.append(item["date"][:10] + " "
                                   + item["description"] + "\n"
                                   + card_text + " " + number_card
                                   + " ---> "
                                   + "**" + item["to"][-4:] + "\n"
                                   + item['operationAmount']['amount']
                                   + item["operationAmount"]["currency"]["code"])
    return "\n\n".join(str(el) for el in sorted_by_state[:5])


print(operation_executed())
print()