p = dict()  # 分布列


def int_input(text='输入数字:'):
    temp1 = input(text)
    try:
        temp2 = float(temp1)
    except ValueError:
        return None
    else:
        return temp2


if __name__ == "__main__":
    int_input('2')
    int_input()
