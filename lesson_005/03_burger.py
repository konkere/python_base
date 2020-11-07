# -*- coding: utf-8 -*-

# Создать модуль my_burger. В нем определить функции добавления инградиентов:
#  - булочки
#  - котлеты
#  - огурчика
#  - помидорчика
#  - майонеза
#  - сыра
# В каждой функции выводить на консоль что-то вроде "А теперь добавим ..."

# В этом модуле создать рецепт двойного чизбургера (https://goo.gl/zA3goZ)
# с помощью фукций из my_burger и вывести на консоль.

# Создать рецепт своего бургера, по вашему вкусу.
# Если не хватает инградиентов - создать соответствующие функции в модуле my_burger

import my_burger as mb

mb.begin_burger('двойной чизбургер')
mb.bun_ingredient()
mb.cutlet_ingredient()
mb.cheese_ingredient()
mb.cutlet_ingredient()
mb.cheese_ingredient()
mb.cucumber_ingredient()
mb.tomato_ingredient()
mb.mayonnaise_ingredient()
mb.bun_ingredient()
mb.end_burger()

mb.next_burger()
mb.begin_burger('хрустящий острый бургер')
mb.bun_ingredient()
mb.french_fries_ingredient()
mb.cutlet_ingredient()
mb.special_secret_sauce_ingredient()
mb.pickle_ingredient()
mb.bun_ingredient()
mb.end_burger()
