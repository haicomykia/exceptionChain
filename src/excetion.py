"""
Pythonでの例外伝播
https://analytics-note.xyz/programming/re-raise-exception/
"""


def div(x: int, y: int) -> float:
    try:
        return x / y
    except ZeroDivisionError as e:
        print(e)
        # 例外を呼び出し元へ伝播
        raise


def print_div_by_zero(x: int) -> None:
    try:
        print(div(x, 0))
    except Exception as e:
        print(e)
    else:
        print('例外は発生しませんでした。')


def print_div(x):
    try:
        print(div(x, 5))
    except Exception as e:
        print(e)
    else:
        print('例外は発生しませんでした。')


if __name__ == "__main__":
    print_div_by_zero(5)
