# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = 10000, 12000

month_in_education = 0
request_funds = 0

while month_in_education < 10:
    month_in_education += 1
    request_funds += expenses - educational_grant
    expenses *= 1.03

request_funds = round(request_funds, 2)
print('Студенту надо попросить', request_funds, 'рублей')

# зачет!
