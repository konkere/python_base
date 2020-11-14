# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

from district.central_street.house1.room1 import folks as folks_central_h1r1
from district.central_street.house1.room2 import folks as folks_central_h1r2
from district.central_street.house2.room1 import folks as folks_central_h2r1
from district.central_street.house2.room2 import folks as folks_central_h2r2
from district.soviet_street.house1.room1 import folks as folks_soviet_h1r1
from district.soviet_street.house1.room2 import folks as folks_soviet_h1r2
from district.soviet_street.house2.room1 import folks as folks_soviet_h2r1
from district.soviet_street.house2.room2 import folks as folks_soviet_h2r2

folks_all = folks_central_h1r1 + folks_central_h1r2 + folks_central_h2r1 + folks_central_h2r2 +\
            folks_soviet_h1r1 + folks_soviet_h1r2 + folks_soviet_h2r1 + folks_soviet_h2r2

district_ppl = ', '.join(folks_all)

print('На районе живут:', district_ppl)
