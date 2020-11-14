# -*- coding: utf-8 -*-

# Вывести на консоль жителей комнат (модули room_1 и room_2)
# Формат: В комнате room_1 живут: ...

import room_1
import room_2

ppl_room_1 = ', '.join(room_1.folks)
ppl_room_2 = ', '.join(room_2.folks)

print('В комнате room_1 живут:', ppl_room_1)
print('В комнате room_2 живут:', ppl_room_2)

# зачет!
