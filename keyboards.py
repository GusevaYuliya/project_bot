from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

kb_1 = InlineKeyboardMarkup(row_width=1)
button_1 = InlineKeyboardButton(text='Информация', callback_data='/inf')
button_2 = InlineKeyboardButton(text='Пройти опрос', callback_data='/go')
kb_1.add(button_2, button_1)
# add- подряд
# insert - если есть место сбоку
# row - в строку
kb_question_1 = InlineKeyboardMarkup(row_width=1)
button_1 = InlineKeyboardButton(text='Исключительно сельское хозяйство\nи смежные отрасли', callback_data='/first')
button_2 = InlineKeyboardButton(
    text='Это лишь один из вариантов,\nдля меня важно иметь возможность работать не только в этой сфере',
    callback_data='/second')
button_3 = InlineKeyboardButton(
    text='50/50',
    callback_data='/third')
button_4 = InlineKeyboardButton(text='Назад', callback_data='/Назад')
kb_question_1.add(button_1, button_2, button_3, button_4)

kb_question_2 = InlineKeyboardMarkup(row_width=1)
button_1 = InlineKeyboardButton(text='Готов руководить', callback_data='/first')
button_2 = InlineKeyboardButton(
    text='Лучше делать строго свою\n часть работы',
    callback_data='/second')
button_3 = InlineKeyboardButton(
    text='Не принципиально/не решил',
    callback_data='/third')
button_4 = InlineKeyboardButton(text='Назад', callback_data='/Назад')
kb_question_2.add(button_1, button_2, button_3, button_4)

kb_question_3 = InlineKeyboardMarkup(row_width=1)
button_1 = InlineKeyboardButton(text='Интересами', callback_data='/first')
button_2 = InlineKeyboardButton(
    text='Престижностью профессии и заработком',
    callback_data='/second')
button_4 = InlineKeyboardButton(text='Назад', callback_data='/Назад')
kb_question_3.add(button_1, button_2, button_4)

kb_question_4 = InlineKeyboardMarkup(row_width=5)
kb_question_4.add(InlineKeyboardButton(text='1', callback_data=f'/1'),
                  InlineKeyboardButton(text='2', callback_data=f'/2'),
                  InlineKeyboardButton(text='3', callback_data=f'/3'),
                  InlineKeyboardButton(text='4', callback_data=f'/4'),
                  InlineKeyboardButton(text='5', callback_data=f'/5'))
kb_question_4.add(InlineKeyboardButton(text='6', callback_data=f'/6'),
                  InlineKeyboardButton(text='7', callback_data=f'/7'),
                  InlineKeyboardButton(text='8', callback_data=f'/8'),
                  InlineKeyboardButton(text='9', callback_data=f'/9'),
                  InlineKeyboardButton(text='10', callback_data=f'/10'))
button_4 = InlineKeyboardButton(text='Назад', callback_data='/Назад')
kb_question_4.add(button_4)

kb_question_5 = InlineKeyboardMarkup(row_width=5)
kb_question_5.add(InlineKeyboardButton(text='1', callback_data=f'/1'),
                  InlineKeyboardButton(text='2', callback_data=f'/2'),
                  InlineKeyboardButton(text='3', callback_data=f'/3'),
                  InlineKeyboardButton(text='4', callback_data=f'/4'),
                  InlineKeyboardButton(text='5', callback_data=f'/5'))
kb_question_5.add(InlineKeyboardButton(text='6', callback_data=f'/6'),
                  InlineKeyboardButton(text='7', callback_data=f'/7'),
                  InlineKeyboardButton(text='8', callback_data=f'/8'),
                  InlineKeyboardButton(text='9', callback_data=f'/9'),
                  InlineKeyboardButton(text='10', callback_data=f'/10'))
button_4 = InlineKeyboardButton(text='Назад', callback_data='/Назад')
kb_question_5.add(button_4)

kb_question_6 = InlineKeyboardMarkup(row_width=5)
kb_question_6.add(InlineKeyboardButton(text='1', callback_data=f'/1'),
                  InlineKeyboardButton(text='2', callback_data=f'/2'),
                  InlineKeyboardButton(text='3', callback_data=f'/3'),
                  InlineKeyboardButton(text='4', callback_data=f'/4'),
                  InlineKeyboardButton(text='5', callback_data=f'/5'))
kb_question_6.add(InlineKeyboardButton(text='6', callback_data=f'/6'),
                  InlineKeyboardButton(text='7', callback_data=f'/7'),
                  InlineKeyboardButton(text='8', callback_data=f'/8'),
                  InlineKeyboardButton(text='9', callback_data=f'/9'),
                  InlineKeyboardButton(text='10', callback_data=f'/10'))
button_4 = InlineKeyboardButton(text='Назад', callback_data='/Назад')
kb_question_6.add(button_4)

kb_question_7 = InlineKeyboardMarkup(row_width=5)
kb_question_7.add(InlineKeyboardButton(text='1', callback_data=f'/1'),
                  InlineKeyboardButton(text='2', callback_data=f'/2'),
                  InlineKeyboardButton(text='3', callback_data=f'/3'),
                  InlineKeyboardButton(text='4', callback_data=f'/4'),
                  InlineKeyboardButton(text='5', callback_data=f'/5'))
kb_question_7.add(InlineKeyboardButton(text='6', callback_data=f'/6'),
                  InlineKeyboardButton(text='7', callback_data=f'/7'),
                  InlineKeyboardButton(text='8', callback_data=f'/8'),
                  InlineKeyboardButton(text='9', callback_data=f'/9'),
                  InlineKeyboardButton(text='10', callback_data=f'/10'))
button_4 = InlineKeyboardButton(text='Назад', callback_data='/Назад')
kb_question_7.add(button_4)

kb_question_8 = InlineKeyboardMarkup(row_width=1)
button_1 = InlineKeyboardButton(text='1. Проектирование новых объектов\n(зданий, производственных территорий и тд)',
                                callback_data='/1')
button_2 = InlineKeyboardButton(text='2. Создание или эксплуатация технических\n средств',
                                callback_data='/2')
button_3 = InlineKeyboardButton(text='3. Создание новых веществ/препаратов\n и т.д.',
                                callback_data='/3')
button_4 = InlineKeyboardButton(text='4. Управление',
                                callback_data='/4')
button_5 = InlineKeyboardButton(text='5. Работа с животными',
                                callback_data='/5')
button_6 = InlineKeyboardButton(text='6. IT',
                                callback_data='/6')
button_0 = InlineKeyboardButton(text='Назад', callback_data='/Назад')
kb_question_8.add(button_1, button_2, button_3, button_4, button_5, button_6, button_0)

kb_client_back_1 = InlineKeyboardMarkup(row_width=1)
button_1 = InlineKeyboardButton(text='Назад', callback_data='/Назад')
kb_client_back_1.add(button_1)

kb_question_10 = InlineKeyboardMarkup(row_width=2)
button_1 = InlineKeyboardButton(text='Да', callback_data='/1')
button_2 = InlineKeyboardButton(text='Нет', callback_data='/0')
button_3 = InlineKeyboardButton(text='Назад', callback_data='/Назад')
kb_question_10.add(button_1, button_2)
kb_question_10.add(button_3)

kb_question_9 = InlineKeyboardMarkup(row_width=2)
button_1 = InlineKeyboardButton(text='1. Наукой/Введением инноваций', callback_data='/1')
button_2 = InlineKeyboardButton(text='2. Производственным процессом', callback_data='/0')
button_3 = InlineKeyboardButton(text='Назад', callback_data='/Назад')
kb_question_9.add(button_1, button_2)
kb_question_9.add(button_3)

kb_final_client = InlineKeyboardMarkup(row_width=2)
button_1 = InlineKeyboardButton(text='Управление в сельском хозяйстве', callback_data='/1')
button_2 = InlineKeyboardButton(text='Технологии производства и переработки\n сельскохозяйственной продукции',
                                callback_data='/2')
button_3 = InlineKeyboardButton(text='Селекция', callback_data='/3')
button_4 = InlineKeyboardButton(text='Зоотехника', callback_data='/4')
button_5 = InlineKeyboardButton(text='Природопользование и экология', callback_data='/5')
button_6 = InlineKeyboardButton(text='Водопользование и гидромелеорация', callback_data='/6')
button_7 = InlineKeyboardButton(text='Ветеринария', callback_data='/7')
button_8 = InlineKeyboardButton(text='Биология/Биотехнологии', callback_data='/8')
button_9 = InlineKeyboardButton(text='Агрохимия/Почвоведение', callback_data='/9')
button_10 = InlineKeyboardButton(text='Агрономия', callback_data='/10')
button_11 = InlineKeyboardButton(text='Агроинформатика', callback_data='/11')
button_12 = InlineKeyboardButton(text='Агроиженерия', callback_data='/12')
button_13 = InlineKeyboardButton(text='Назад', callback_data='/Назад')
kb_final_client.add(button_1, button_3)
kb_final_client.add(button_4, button_5)
kb_final_client.add(button_6, button_7)
kb_final_client.add(button_8)
kb_final_client.add(button_9)
kb_final_client.add(button_2)
kb_final_client.add(button_10)
kb_final_client.add(button_11)
kb_final_client.add(button_12)
kb_final_client.add(button_13)

kb_answ = InlineKeyboardMarkup(row_width=1)
button_0 = InlineKeyboardButton(text='Полезные материалы для изучения специальности', callback_data='/0')
button_1 = InlineKeyboardButton(text='Пройти опрос заново', callback_data='/again')
button_2 = InlineKeyboardButton(text='О практике и стажировке', callback_data='/ra')
kb_answ.add(button_0, button_2, button_1)

kb_final_client_end = InlineKeyboardMarkup(row_width=1)
button_1 = InlineKeyboardButton(text='Пройти опрос заново', callback_data='/again')
button_2 = InlineKeyboardButton(text='Назад', callback_data='/Назад')
kb_final_client_end.add(button_1, button_2)

kb_all = InlineKeyboardMarkup(row_width=1)
button_0 = InlineKeyboardButton(text='Другие специальности', callback_data='/0')
button_1 = InlineKeyboardButton(text='Пройти опрос заново', callback_data='/again')
kb_all.add(button_0, button_1)

kb_ra = InlineKeyboardMarkup(row_width=1)
button_2 = InlineKeyboardButton(text='Назад', callback_data='/Назад')
kb_ra.add(button_2)
