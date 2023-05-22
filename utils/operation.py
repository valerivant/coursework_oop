from utils.sort_by_date import sort_func


def operation_executed():
    """функция добавления в список и последующего вывода нужной инфы по банк. операциям"""
    sorted_by_state = []
    for item in sort_func():
        if "EXECUTED" in item['state']:
            card = item.get("from", "").split()[-1:]
            card_digit = ''.join(c for c in card if c.isdigit())
            card_text = ''.join(c for c in item.get("from", "") if c.isalpha())
            private_number = card_digit[:6] + len(card_digit[6:-4]) * "*" + card_digit[-4:]
            number_card = f"{private_number[0:4]} {private_number[4:8]} {private_number[8:12]} {private_number[-4:]}"
            sorted_by_state.append(
                f"{item['date'][8:10]}{item['date'][4:7]}-{item['date'][:4]} {item['description']}\n{card_text} "
                f"{number_card} ---> **{item['to'][-4:]}\n"
                f"{item['operationAmount']['amount']}{item['operationAmount']['currency']['code']}"
            )
    return '\n\n'.join(sorted_by_state[:5])



