# x, n - индекс и количество закупов
# y, m - индекс и количество продаж
# m_1, m_2 - количества (quantity) первой и последней продажи x_1 и x_2 в интервале (fromTime, toTime).
# n_1, n_2 - количества (quantity) принадлежащие определенным закупам y_1 и y_2 с которого начинается и заканчивается подсчет для cost

# Algorithm for identifying m_1 and y_1 
def sales_before_time(sales, fromTime):
    # Summing up quantities of m_i until saleTime >= fromTime, and taking the last sale element as y_1
    # INPUT: sales <list>, fromTime <string>
    # OUTPUT: m_sum_1 <int>, y_1_id <int>
    i = 0
    m_sum_1 = 0
    y_1_id = 0

    while sales[i]['saleTime'] < fromTime:
        m_sum_1 += sales[i]['quantity']
        y_1_id = sales[i]['id']

    return m_sum_1, y_1_id

