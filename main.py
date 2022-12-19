from aiogram.utils import executor
from aiogram import types

from text import start_text, info_text, question_text_1, question_text_2, question_text_3, question_text_4, \
    question_text_5, question_text_6, question_text_7, question_text_8, question_text_9, question_text_10, help_text, \
    other_text, answer, text_ra
from create_bot import dp, bot
from keyboards import kb_1, kb_client_back_1, kb_question_1, kb_question_2, kb_question_3, kb_question_4, kb_question_6, \
    kb_question_5, kb_question_7, kb_question_8, kb_question_9, kb_question_10, kb_answ, kb_all, kb_final_client, kb_ra
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from regress import pred
from datetime import datetime
from aiogram.types.message import ContentTypes



async def on_startup(_):
    print('Бот вышел в онлайн \nhttps://t.me/Infa_project_2022_bot')


class FSMClient(StatesGroup):
    first_state = State()
    inf = State()
    question_1 = State()
    question_2 = State()
    question_3 = State()
    question_4 = State()
    question_5 = State()
    question_6 = State()
    question_7 = State()
    question_8 = State()
    question_9 = State()
    question_10 = State()
    answ = State()
    answ_1 = State()
    all = State()
    all_1 = State()
    all_2 = State()
    ra = State()
    ra_all_1 = State()


# Начало диалога с машиной состояний
@dp.message_handler(commands='start', state=None)
async def start(message: types.Message):
    await FSMClient.first_state.set()
    await bot.send_message(message.from_user.id, start_text, reply_markup=kb_1)


# Ловим ответ
@dp.callback_query_handler(text='/inf', state=FSMClient.first_state)
async def info(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    await FSMClient.inf.set()
    await bot.send_message(callback.from_user.id, info_text, reply_markup=kb_client_back_1)


@dp.callback_query_handler(text='/Назад', state=FSMClient.inf)
async def back_first_choice(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    await FSMClient.first_state.set()
    await bot.send_message(callback.from_user.id, start_text, reply_markup=kb_1)


@dp.callback_query_handler(text='/go', state=FSMClient.first_state)
async def rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    await FSMClient.question_1.set()
    await bot.send_message(callback.from_user.id, question_text_1, reply_markup=kb_question_1)


######_______________1 Вопрос_______________######
@dp.callback_query_handler(text='/first', state=FSMClient.question_1)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    async with state.proxy() as data:
        data['question_1'] = 2
    await FSMClient.question_2.set()
    await bot.send_message(callback.from_user.id, question_text_2, reply_markup=kb_question_2)


@dp.callback_query_handler(text='/second', state=FSMClient.question_1)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    async with state.proxy() as data:
        data['question_1'] = 1
    await FSMClient.question_2.set()
    await bot.send_message(callback.from_user.id, question_text_2, reply_markup=kb_question_2)


@dp.callback_query_handler(text='/third', state=FSMClient.question_1)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    async with state.proxy() as data:
        data['question_1'] = 0
    await FSMClient.question_2.set()
    await bot.send_message(callback.from_user.id, question_text_2, reply_markup=kb_question_2)


@dp.callback_query_handler(text='/Назад', state=FSMClient.question_1)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    await FSMClient.first_state.set()
    await bot.send_message(callback.from_user.id, start_text, reply_markup=kb_1)


######_______________2 Вопрос_______________######
@dp.callback_query_handler(text='/first', state=FSMClient.question_2)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    async with state.proxy() as data:
        data['question_2'] = 2
    await FSMClient.question_3.set()
    await bot.send_message(callback.from_user.id, question_text_3, reply_markup=kb_question_3)


@dp.callback_query_handler(text='/second', state=FSMClient.question_2)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    async with state.proxy() as data:
        data['question_2'] = 1
    await FSMClient.question_3.set()
    await bot.send_message(callback.from_user.id, question_text_3, reply_markup=kb_question_3)


@dp.callback_query_handler(text='/third', state=FSMClient.question_2)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    async with state.proxy() as data:
        data['question_2'] = 0
    await FSMClient.question_3.set()
    await bot.send_message(callback.from_user.id, question_text_3, reply_markup=kb_question_3)


@dp.callback_query_handler(text='/Назад', state=FSMClient.question_2)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    await FSMClient.question_1.set()
    await bot.send_message(callback.from_user.id, question_text_1, reply_markup=kb_question_1)


######_______________3 Вопрос_______________######
@dp.callback_query_handler(text='/first', state=FSMClient.question_3)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    async with state.proxy() as data:
        data['question_3'] = 1
    await FSMClient.question_4.set()
    await bot.send_message(callback.from_user.id, question_text_4, reply_markup=kb_question_4)


@dp.callback_query_handler(text='/second', state=FSMClient.question_3)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    async with state.proxy() as data:
        data['question_3'] = 0
    await FSMClient.question_4.set()
    await bot.send_message(callback.from_user.id, question_text_4, reply_markup=kb_question_4)


@dp.callback_query_handler(text='/Назад', state=FSMClient.question_3)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    await FSMClient.question_2.set()
    await bot.send_message(callback.from_user.id, question_text_2, reply_markup=kb_question_2)


######_______________4 Вопрос_______________######
@dp.callback_query_handler(text='/1', state=FSMClient.question_4)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    async with state.proxy() as data:
        data['question_4'] = 1
    await FSMClient.question_5.set()
    await bot.send_message(callback.from_user.id, question_text_5, reply_markup=kb_question_5)


@dp.callback_query_handler(text='/2', state=FSMClient.question_4)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    async with state.proxy() as data:
        data['question_4'] = 2
    await FSMClient.question_5.set()
    await bot.send_message(callback.from_user.id, question_text_5, reply_markup=kb_question_5)


@dp.callback_query_handler(text='/3', state=FSMClient.question_4)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    async with state.proxy() as data:
        data['question_4'] = 3
    await FSMClient.question_5.set()
    await bot.send_message(callback.from_user.id, question_text_5, reply_markup=kb_question_5)


@dp.callback_query_handler(text='/4', state=FSMClient.question_4)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    async with state.proxy() as data:
        data['question_4'] = 4
    await FSMClient.question_5.set()
    await bot.send_message(callback.from_user.id, question_text_5, reply_markup=kb_question_5)


@dp.callback_query_handler(text='/5', state=FSMClient.question_4)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    async with state.proxy() as data:
        data['question_4'] = 5
    await FSMClient.question_5.set()
    await bot.send_message(callback.from_user.id, question_text_5, reply_markup=kb_question_5)


@dp.callback_query_handler(text='/6', state=FSMClient.question_4)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    async with state.proxy() as data:
        data['question_4'] = 6
    await FSMClient.question_5.set()
    await bot.send_message(callback.from_user.id, question_text_5, reply_markup=kb_question_5)


@dp.callback_query_handler(text='/7', state=FSMClient.question_4)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    async with state.proxy() as data:
        data['question_4'] = 7
    await FSMClient.question_5.set()
    await bot.send_message(callback.from_user.id, question_text_5, reply_markup=kb_question_5)


@dp.callback_query_handler(text='/8', state=FSMClient.question_4)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    async with state.proxy() as data:
        data['question_4'] = 8
    await FSMClient.question_5.set()
    await bot.send_message(callback.from_user.id, question_text_5, reply_markup=kb_question_5)


@dp.callback_query_handler(text='/9', state=FSMClient.question_4)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    async with state.proxy() as data:
        data['question_4'] = 9
    await FSMClient.question_5.set()
    await bot.send_message(callback.from_user.id, question_text_5, reply_markup=kb_question_5)


@dp.callback_query_handler(text='/10', state=FSMClient.question_4)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    async with state.proxy() as data:
        data['question_4'] = 10
    await FSMClient.question_5.set()
    await bot.send_message(callback.from_user.id, question_text_5, reply_markup=kb_question_5)


@dp.callback_query_handler(text='/Назад', state=FSMClient.question_4)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    await FSMClient.question_3.set()
    await bot.send_message(callback.from_user.id, question_text_3, reply_markup=kb_question_3)


######_______________5 Вопрос_______________######
@dp.callback_query_handler(text='/1', state=FSMClient.question_5)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    async with state.proxy() as data:
        data['question_5'] = 1
    await FSMClient.question_6.set()
    await bot.send_message(callback.from_user.id, question_text_6, reply_markup=kb_question_6)


@dp.callback_query_handler(text='/2', state=FSMClient.question_5)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    async with state.proxy() as data:
        data['question_5'] = 2
    await FSMClient.question_6.set()
    await bot.send_message(callback.from_user.id, question_text_6, reply_markup=kb_question_6)


@dp.callback_query_handler(text='/3', state=FSMClient.question_5)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    async with state.proxy() as data:
        data['question_5'] = 3
    await FSMClient.question_6.set()
    await bot.send_message(callback.from_user.id, question_text_6, reply_markup=kb_question_6)


@dp.callback_query_handler(text='/4', state=FSMClient.question_5)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    async with state.proxy() as data:
        data['question_5'] = 4
    await FSMClient.question_6.set()
    await bot.send_message(callback.from_user.id, question_text_6, reply_markup=kb_question_6)


@dp.callback_query_handler(text='/5', state=FSMClient.question_5)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    async with state.proxy() as data:
        data['question_5'] = 5
    await FSMClient.question_6.set()
    await bot.send_message(callback.from_user.id, question_text_6, reply_markup=kb_question_6)


@dp.callback_query_handler(text='/6', state=FSMClient.question_5)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    async with state.proxy() as data:
        data['question_5'] = 6
    await FSMClient.question_6.set()
    await bot.send_message(callback.from_user.id, question_text_6, reply_markup=kb_question_6)


@dp.callback_query_handler(text='/7', state=FSMClient.question_5)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    async with state.proxy() as data:
        data['question_5'] = 7
    await FSMClient.question_6.set()
    await bot.send_message(callback.from_user.id, question_text_6, reply_markup=kb_question_6)


@dp.callback_query_handler(text='/8', state=FSMClient.question_5)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    async with state.proxy() as data:
        data['question_5'] = 8
    await FSMClient.question_6.set()
    await bot.send_message(callback.from_user.id, question_text_6, reply_markup=kb_question_6)


@dp.callback_query_handler(text='/9', state=FSMClient.question_5)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    async with state.proxy() as data:
        data['question_5'] = 9
    await FSMClient.question_6.set()
    await bot.send_message(callback.from_user.id, question_text_6, reply_markup=kb_question_6)


@dp.callback_query_handler(text='/10', state=FSMClient.question_5)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    async with state.proxy() as data:
        data['question_5'] = 10
    await FSMClient.question_6.set()
    await bot.send_message(callback.from_user.id, question_text_6, reply_markup=kb_question_6)


@dp.callback_query_handler(text='/Назад', state=FSMClient.question_5)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    await FSMClient.question_4.set()
    await bot.send_message(callback.from_user.id, question_text_4, reply_markup=kb_question_4)


######_______________6 Вопрос_______________######
@dp.callback_query_handler(text='/1', state=FSMClient.question_6)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    async with state.proxy() as data:
        data['question_6'] = 1
    await FSMClient.question_7.set()
    await bot.send_message(callback.from_user.id, question_text_7, reply_markup=kb_question_7)


@dp.callback_query_handler(text='/2', state=FSMClient.question_6)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    async with state.proxy() as data:
        data['question_6'] = 2
    await FSMClient.question_7.set()
    await bot.send_message(callback.from_user.id, question_text_7, reply_markup=kb_question_7)


@dp.callback_query_handler(text='/3', state=FSMClient.question_6)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    async with state.proxy() as data:
        data['question_6'] = 3
    await FSMClient.question_7.set()
    await bot.send_message(callback.from_user.id, question_text_7, reply_markup=kb_question_7)


@dp.callback_query_handler(text='/4', state=FSMClient.question_6)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    async with state.proxy() as data:
        data['question_6'] = 4
    await FSMClient.question_7.set()
    await bot.send_message(callback.from_user.id, question_text_7, reply_markup=kb_question_7)


@dp.callback_query_handler(text='/5', state=FSMClient.question_6)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    async with state.proxy() as data:
        data['question_6'] = 5
    await FSMClient.question_7.set()
    await bot.send_message(callback.from_user.id, question_text_7, reply_markup=kb_question_7)


@dp.callback_query_handler(text='/6', state=FSMClient.question_6)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    async with state.proxy() as data:
        data['question_6'] = 6
    await FSMClient.question_7.set()
    await bot.send_message(callback.from_user.id, question_text_7, reply_markup=kb_question_7)


@dp.callback_query_handler(text='/7', state=FSMClient.question_6)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    async with state.proxy() as data:
        data['question_6'] = 7
    await FSMClient.question_7.set()
    await bot.send_message(callback.from_user.id, question_text_7, reply_markup=kb_question_7)


@dp.callback_query_handler(text='/8', state=FSMClient.question_6)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    async with state.proxy() as data:
        data['question_6'] = 8
    await FSMClient.question_7.set()
    await bot.send_message(callback.from_user.id, question_text_7, reply_markup=kb_question_7)


@dp.callback_query_handler(text='/9', state=FSMClient.question_6)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    async with state.proxy() as data:
        data['question_6'] = 9
    await FSMClient.question_7.set()
    await bot.send_message(callback.from_user.id, question_text_7, reply_markup=kb_question_7)


@dp.callback_query_handler(text='/10', state=FSMClient.question_6)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    async with state.proxy() as data:
        data['question_6'] = 10
    await FSMClient.question_7.set()
    await bot.send_message(callback.from_user.id, question_text_7, reply_markup=kb_question_7)


@dp.callback_query_handler(text='/Назад', state=FSMClient.question_6)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    await FSMClient.question_5.set()
    await bot.send_message(callback.from_user.id, question_text_5, reply_markup=kb_question_5)


######_______________7 Вопрос_______________######

@dp.callback_query_handler(text='/1', state=FSMClient.question_7)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    async with state.proxy() as data:
        data['question_7'] = 1
    await FSMClient.question_8.set()
    await bot.send_message(callback.from_user.id, question_text_8, reply_markup=kb_question_8)


@dp.callback_query_handler(text='/2', state=FSMClient.question_7)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    async with state.proxy() as data:
        data['question_7'] = 2
    await FSMClient.question_8.set()
    await bot.send_message(callback.from_user.id, question_text_8, reply_markup=kb_question_8)


@dp.callback_query_handler(text='/3', state=FSMClient.question_7)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    async with state.proxy() as data:
        data['question_7'] = 3
    await FSMClient.question_8.set()
    await bot.send_message(callback.from_user.id, question_text_8, reply_markup=kb_question_8)


@dp.callback_query_handler(text='/4', state=FSMClient.question_7)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    async with state.proxy() as data:
        data['question_7'] = 4
    await FSMClient.question_8.set()
    await bot.send_message(callback.from_user.id, question_text_8, reply_markup=kb_question_8)


@dp.callback_query_handler(text='/5', state=FSMClient.question_7)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    async with state.proxy() as data:
        data['question_7'] = 5
    await FSMClient.question_8.set()
    await bot.send_message(callback.from_user.id, question_text_8, reply_markup=kb_question_8)


@dp.callback_query_handler(text='/6', state=FSMClient.question_7)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    async with state.proxy() as data:
        data['question_7'] = 6
    await FSMClient.question_8.set()
    await bot.send_message(callback.from_user.id, question_text_8, reply_markup=kb_question_8)


@dp.callback_query_handler(text='/7', state=FSMClient.question_7)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    async with state.proxy() as data:
        data['question_7'] = 7
    await FSMClient.question_8.set()
    await bot.send_message(callback.from_user.id, question_text_8, reply_markup=kb_question_8)


@dp.callback_query_handler(text='/8', state=FSMClient.question_7)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    async with state.proxy() as data:
        data['question_7'] = 8
    await FSMClient.question_8.set()
    await bot.send_message(callback.from_user.id, question_text_8, reply_markup=kb_question_8)


@dp.callback_query_handler(text='/9', state=FSMClient.question_7)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    async with state.proxy() as data:
        data['question_7'] = 9
    await FSMClient.question_8.set()
    await bot.send_message(callback.from_user.id, question_text_8, reply_markup=kb_question_8)


@dp.callback_query_handler(text='/10', state=FSMClient.question_7)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    async with state.proxy() as data:
        data['question_7'] = 10
    await FSMClient.question_8.set()
    await bot.send_message(callback.from_user.id, question_text_8, reply_markup=kb_question_8)


@dp.callback_query_handler(text='/Назад', state=FSMClient.question_7)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    await FSMClient.question_6.set()
    await bot.send_message(callback.from_user.id, question_text_6, reply_markup=kb_question_6)


######_______________8 Вопрос_______________######
@dp.callback_query_handler(text='/1', state=FSMClient.question_8)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    async with state.proxy() as data:
        data['question_8'] = 1
    await FSMClient.question_9.set()
    await bot.send_message(callback.from_user.id, question_text_9, reply_markup=kb_question_9)


@dp.callback_query_handler(text='/2', state=FSMClient.question_8)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    async with state.proxy() as data:
        data['question_8'] = 2
    await FSMClient.question_9.set()
    await bot.send_message(callback.from_user.id, question_text_9, reply_markup=kb_question_9)


@dp.callback_query_handler(text='/3', state=FSMClient.question_8)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    async with state.proxy() as data:
        data['question_8'] = 3
    await FSMClient.question_9.set()
    await bot.send_message(callback.from_user.id, question_text_9, reply_markup=kb_question_9)


@dp.callback_query_handler(text='/4', state=FSMClient.question_8)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    async with state.proxy() as data:
        data['question_8'] = 4
    await FSMClient.question_9.set()
    await bot.send_message(callback.from_user.id, question_text_9, reply_markup=kb_question_9)


@dp.callback_query_handler(text='/5', state=FSMClient.question_8)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    async with state.proxy() as data:
        data['question_8'] = 5
    await FSMClient.question_9.set()
    await bot.send_message(callback.from_user.id, question_text_9, reply_markup=kb_question_9)


@dp.callback_query_handler(text='/6', state=FSMClient.question_8)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    async with state.proxy() as data:
        data['question_8'] = 6
    await FSMClient.question_9.set()
    await bot.send_message(callback.from_user.id, question_text_9, reply_markup=kb_question_9)


@dp.callback_query_handler(text='/Назад', state=FSMClient.question_8)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    await FSMClient.question_7.set()
    await bot.send_message(callback.from_user.id, question_text_7, reply_markup=kb_question_7)


######_______________9 Вопрос_______________######
@dp.callback_query_handler(text='/0', state=FSMClient.question_9)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    async with state.proxy() as data:
        data['question_9'] = 0
    await FSMClient.question_10.set()
    await bot.send_message(callback.from_user.id, question_text_10, reply_markup=kb_question_10)


@dp.callback_query_handler(text='/1', state=FSMClient.question_9)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    async with state.proxy() as data:
        data['question_9'] = 1
    await FSMClient.question_10.set()
    await bot.send_message(callback.from_user.id, question_text_10, reply_markup=kb_question_10)


@dp.callback_query_handler(text='/Назад', state=FSMClient.question_9)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    await FSMClient.question_8.set()
    await bot.send_message(callback.from_user.id, question_text_8, reply_markup=kb_question_8)


######_______________10 Вопрос_______________######
answ = ["Управление в сельском хозяйстве",
        "Технологии производства и переработки сельскохозяйственной продукции/Производство продуктов питания",
        "Cелекционер", "Зоотехник", "Экология и природопользование",
        "Природообустройства и водопользование/Гидромелиорация", "Ветеринария", "Биотехнологии/биология",
        "Агрохимия/агропочвоведение", "Агрономия", "Агроинформатика", "Агроинженерия"]


@dp.callback_query_handler(text='/0', state=FSMClient.question_10)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    async with state.proxy() as data:
        data['question_10'] = 0
    await FSMClient.answ.set()
    async with state.proxy() as data:
        arr = []
        for i in range(1, 11):
            arr.append(data[f"question_{i}"])
        # print(arr)
        # print(pred(arr))
        result = answ[pred(arr) - 1]
        data['result'] = pred(arr)
        # print(result)
    await bot.send_message(callback.from_user.id, f"И ваш результат: {result}")
    await bot.send_message(callback.from_user.id, answer[f"{pred(arr)}_0"], reply_markup=kb_answ)


@dp.callback_query_handler(text='/1', state=FSMClient.question_10)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)

    async with state.proxy() as data:
        data['question_10'] = 1
    await FSMClient.answ.set()
    async with state.proxy() as data:
        arr = []
        for i in range(1, 11):
            arr.append(data[f"question_{i}"])
        result = answ[pred(arr) - 1]
        data['result'] = pred(arr)
    await bot.send_message(callback.from_user.id, f"И ваш результат: {result}")
    await bot.send_message(callback.from_user.id, answer[f"{pred(arr)}_0"], reply_markup=kb_answ)


@dp.callback_query_handler(text='/Назад', state=FSMClient.question_10)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    await FSMClient.question_9.set()
    await bot.send_message(callback.from_user.id, question_text_9, reply_markup=kb_question_9)


######_______________11 Step_______________######
@dp.callback_query_handler(text='/again', state=FSMClient.answ)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    await FSMClient.question_1.set()
    await bot.send_message(callback.from_user.id, question_text_1, reply_markup=kb_question_1)


@dp.callback_query_handler(text='/0', state=FSMClient.answ)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    await FSMClient.answ_1.set()
    async with state.proxy() as data:
        r = data['result']
    await bot.send_message(callback.from_user.id, answer[f"{r}_1"], reply_markup=kb_all)


@dp.callback_query_handler(text='/ra', state=FSMClient.answ)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    await FSMClient.ra.set()
    await bot.send_message(callback.from_user.id, text_ra, reply_markup=kb_ra)


######_______________Обработка ra_______________######
@dp.callback_query_handler(text='/Назад', state=FSMClient.ra)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    await FSMClient.answ.set()
    async with state.proxy() as data:
        arr = []
        for i in range(1, 11):
            arr.append(data[f"question_{i}"])
        result = answ[pred(arr) - 1]
        data['result'] = pred(arr)
    await bot.send_message(callback.from_user.id, f"И ваш результат: {result}")
    await bot.send_message(callback.from_user.id, answer[f"{pred(arr)}_0"], reply_markup=kb_answ)


######_______________Обработка ra_______________######
######_______________12 Step_______________######
@dp.callback_query_handler(text='/0', state=FSMClient.answ_1)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    await FSMClient.all.set()
    await bot.send_message(callback.from_user.id, "Популярнве агротехнические специальности",
                           reply_markup=kb_final_client)


@dp.callback_query_handler(text='/again', state=FSMClient.answ_1)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    await FSMClient.question_1.set()
    await bot.send_message(callback.from_user.id, question_text_1, reply_markup=kb_question_1)


######_______________13 Step_______________######
@dp.callback_query_handler(text='/1', state=FSMClient.all)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    async with state.proxy() as data:
        data['result_1'] = 1
    await FSMClient.all_1.set()
    await bot.send_message(callback.from_user.id, answer["1_0"], reply_markup=kb_answ)


@dp.callback_query_handler(text='/2', state=FSMClient.all)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    async with state.proxy() as data:
        data['result_1'] = 2
    await FSMClient.all_1.set()
    await bot.send_message(callback.from_user.id, answer["2_0"], reply_markup=kb_answ)


@dp.callback_query_handler(text='/3', state=FSMClient.all)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    async with state.proxy() as data:
        data['result_1'] = 3
    await FSMClient.all_1.set()
    await bot.send_message(callback.from_user.id, answer["3_0"], reply_markup=kb_answ)


@dp.callback_query_handler(text='/4', state=FSMClient.all)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    async with state.proxy() as data:
        data['result_1'] = 4
    await FSMClient.all_1.set()
    await bot.send_message(callback.from_user.id, answer["4_0"], reply_markup=kb_answ)


@dp.callback_query_handler(text='/5', state=FSMClient.all)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    async with state.proxy() as data:
        data['result_1'] = 5
    await FSMClient.all_1.set()
    await bot.send_message(callback.from_user.id, answer["5_0"], reply_markup=kb_answ)


@dp.callback_query_handler(text='/6', state=FSMClient.all)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    async with state.proxy() as data:
        data['result_1'] = 6
    await FSMClient.all_1.set()
    await bot.send_message(callback.from_user.id, answer["6_0"], reply_markup=kb_answ)


@dp.callback_query_handler(text='/7', state=FSMClient.all)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    async with state.proxy() as data:
        data['result_1'] = 7
    await FSMClient.all_1.set()
    await bot.send_message(callback.from_user.id, answer["7_0"], reply_markup=kb_answ)


@dp.callback_query_handler(text='/8', state=FSMClient.all)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    async with state.proxy() as data:
        data['result_1'] = 8
    await FSMClient.all_1.set()
    await bot.send_message(callback.from_user.id, answer["8_0"], reply_markup=kb_answ)


@dp.callback_query_handler(text='/9', state=FSMClient.all)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    async with state.proxy() as data:
        data['result_1'] = 9
    await FSMClient.all_1.set()
    await bot.send_message(callback.from_user.id, answer["9_0"], reply_markup=kb_answ)


@dp.callback_query_handler(text='/10', state=FSMClient.all)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    async with state.proxy() as data:
        data['result_1'] = 10
    await FSMClient.all_1.set()
    await bot.send_message(callback.from_user.id, answer["10_0"], reply_markup=kb_answ)


@dp.callback_query_handler(text='/11', state=FSMClient.all)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    async with state.proxy() as data:
        data['result_1'] = 11
    await FSMClient.all_1.set()
    await bot.send_message(callback.from_user.id, answer["11_0"], reply_markup=kb_answ)


@dp.callback_query_handler(text='/12', state=FSMClient.all)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    async with state.proxy() as data:
        data['result_1'] = 12
    await FSMClient.all_1.set()
    await bot.send_message(callback.from_user.id, answer["12_0"], reply_markup=kb_answ)


######_______________14 Step_______________######
@dp.callback_query_handler(text='/again', state=FSMClient.all_1)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    await FSMClient.question_1.set()
    await bot.send_message(callback.from_user.id, question_text_1, reply_markup=kb_question_1)


@dp.callback_query_handler(text='/0', state=FSMClient.all_1)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    await FSMClient.all_2.set()
    async with state.proxy() as data:
        r = data['result_1']
    await bot.send_message(callback.from_user.id, answer[f"{r}_1"], reply_markup=kb_all)


@dp.callback_query_handler(text='/ra', state=FSMClient.all_1)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    await FSMClient.ra_all_1.set()
    await bot.send_message(callback.from_user.id, text_ra, reply_markup=kb_ra)


######_______________Обработка ra_______________######
@dp.callback_query_handler(text='/Назад', state=FSMClient.ra_all_1)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    async with state.proxy() as data:
        r = data['result_1']
    await FSMClient.all_1.set()
    await bot.send_message(callback.from_user.id, answer[f"{r}_0"], reply_markup=kb_answ)


######_______________Обработка ra_______________######

######_______________15 Step_______________######
@dp.callback_query_handler(text='/0', state=FSMClient.all_2)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    await FSMClient.all.set()
    await bot.send_message(callback.from_user.id, "Популярнве агротехнические специальности",
                           reply_markup=kb_final_client)


@dp.callback_query_handler(text='/again', state=FSMClient.all_2)
async def back_info_rates(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    await FSMClient.question_1.set()
    await bot.send_message(callback.from_user.id, question_text_1, reply_markup=kb_question_1)


####################################################

@dp.message_handler(commands=['help'])
async def command_help(message: types.Message):
    await bot.send_message(message.from_user.id, help_text)


@dp.message_handler()
async def other(message: types.Message):
    await bot.send_message(message.from_user.id, other_text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)  # False- будет отвечать после OFFline
