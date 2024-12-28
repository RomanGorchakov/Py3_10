#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import threading


def calculate_term(x, n, result_list):
    term = x**n
    result_list.append(term)


def calculate_series_sum(x, tolerance):
    result_list = []
    threads = []
    n = 0

    while True:
        thread = threading.Thread(target=calculate_term, args=(x, n, result_list))
        threads.append(thread)
        thread.start()

        thread.join()

        if abs(x**n) < tolerance:
            break
        
        n += 1

    for thread in threads:
        thread.join()

    return sum(result_list)


if __name__ == "__main__":
    x = 0.7
    tolerance = 1e-6

    series_sum = calculate_series_sum(x, tolerance)

    control_value = 1 / (1 - x)

    print(f"Сумма ряда с точностью {tolerance}: {series_sum}")
    print(f"Контрольное значение функции: {control_value}")
    print(f"Разница: {abs(series_sum - control_value)}")