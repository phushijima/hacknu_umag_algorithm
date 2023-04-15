# x, n - индекс и количество закупов
# y, m - индекс и количество продаж
# m_1, m_2 - количества (quantity) первой и последней продажи x_1 и x_2 в интервале (fromTime, toTime).
# n_1, n_2 - количества (quantity) принадлежащие определенным закупам y_1 и y_2 с которого начинается и заканчивается подсчет для cost

# Algorithm for identifying m_1 and y_1 
def sales_before_time(sales, fromTime):
    # Sums up quantities of m_i until saleTime >= fromTime, and taking the last sale element as y_1
    # INPUT: sales <list>, fromTime <string>
    # OUTPUT: m_sum_1 <int>, yFirst_id <int>
    i = 0
    m_sum_1 = 0
    yFirst_id = 0

    while sales[i]['saleTime'] < fromTime:
        m_sum_1 += sales[i]['quantity']
        yFirst_id = sales[i]['id']

    return m_sum_1, yFirst_id

def supplies_before_time(supplies, m_sum_1):
    # Sums up quantities of n_i until n_sum_1 > m_sum_1
    # Takes the element n_{i-1} (before the last) and calculates the difference delta_n, where sum(0, x_{i-1}) + delta_n = sum(0, y_1)
    # INPUT: supplies <list>, m_sum_1 <int>
    # OUTPUT: delta_n <int>, xFirst_id <int>

    i = 0
    n_sum_1 = 0
    delta_n = 0
    xFirst_id = 0

    while n_sum_1 > m_sum_1:
        xFirst_id = supplies[i]['id']
        n_sum_1 += supplies[i]['quantity']
    
    delta_n = n_sum_1 - m_sum_1
    return delta_n, xFirst_id