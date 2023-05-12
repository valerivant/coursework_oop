import pytest

from utils.operation import operation_executed


def test_sort_func():
    return [
        {
            'state': 'EXECUTED',
            'from': '1234 5678 9012 3456',
            'date': '2023-05-10',
            'description': 'Transaction 1',
            'to': '9876',
            'operationAmount': {
                'amount': '100',
                'currency': {
                    'code': 'USD'
                }
            }
        },
        {
            'state': 'PENDING',
            'from': '5678 1234 9012 3456',
            'date': '2023-05-09',
            'description': 'Transaction 2',
            'to': '5432',
            'operationAmount': {
                'amount': '50',
                'currency': {
                    'code': 'EUR'
                }
            }
        },
        {
            'state': 'EXECUTED',
            'from': '9012 3456 7890 1234',
            'date': '2023-05-08',
            'description': 'Transaction 3',
            'to': '2109',
            'operationAmount': {
                'amount': '200',
                'currency': {
                    'code': 'RUB'
                }
            }
        }
    ]


def test_operation_executed():
    expected_output = "2023-05-10 Transaction 1\n1234 **** **** 3456 ---> **9876\n100USD\n\n" \
                      "2023-05-08 Transaction 3\n9012 **** **** 1234 ---> **2109\n200RUB"
    assert operation_executed() == expected_output


# Run the tests
pytest.main()
