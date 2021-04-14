# IMPORTS ##################################################
# aiogram packages
from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters import Text
from aiogram.types import InputFile
from aiogram.types import Message
from aiogram.types import CallbackQuery
from aiogram.types import ReplyKeyboardRemove
from utils.loader import bot
from utils.loader import dp
from utils.logging import *
from .keyboard import *
from api import *
# END IMPORTS ##############################################

def main_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    catalog_btn = KeyboardButton(text="📦 Тарифы")
    profile_btn = KeyboardButton(text="💼 Кабинет")
    payment_btn = KeyboardButton(text="🧮 Оплата")
    delivery_btn = KeyboardButton(text="🚚 Доставка")
    contacts_btn = KeyboardButton(text="📪 Контакты")
    markup.row(catalog_btn,profile_btn)
    markup.row(payment_btn,delivery_btn)
    markup.row(contacts_btn)
    return markup

def cancel_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    catalog_btn = KeyboardButton(text="↩️ Вернуться в меню")
    markup.row(catalog_btn)
    return markup

@dp.message_handler(commands=["start"], state="*")
async def bot_start(message: types.Message):
    text = """
    Бот для @art994 от @sellercoder
    https://telegra.ph/Razrabotka-bota-04-14
    """
    cover = InputFile('cover.jpg')
    await message.answer_photo(cover,caption=text,reply_markup=main_menu())

@dp.message_handler(text=["↩️ Вернуться в меню"], state="*")
async def bot_main(message: types.Message):
    text = "Дарова, отец!"
    cover = InputFile('cover.jpg')
    await message.delete()
    await message.answer("✨")
    await message.answer_photo(cover,caption=text,reply_markup=main_menu())

@dp.message_handler(text=["📦 Тарифы"])
async def catalog_page(message: types.Message):
    await message.answer("⚡️",reply_markup=cancel_menu())
    await message.answer(
        text=f"<b>💬 Выберите оператора для информации о тарифах</b>",
        reply_markup=catalog_menu())

async def show_menu(callback: CallbackQuery, **kwargs):
    await callback.answer(cache_time=1)
    await callback.message.edit_text(
        text=f"<b>💬 Выберите оператора для информации о тарифах</b>",
        reply_markup=catalog_menu())

async def show_provider(callback: CallbackQuery, provider,  **kwargs):
    provider = getProvider(provider)
    logger.info(provider.name)
    text = "<b>{}</b>\n\n<b>💬 Выберите интересующий тариф</b>".format(
        provider.name,
        provider.description)
    await callback.answer(cache_time=1)
    await callback.message.edit_text(text,
        reply_markup=provider_menu(provider.id))

async def show_plan(callback: CallbackQuery, provider, plan, **kwargs):
    plan = Plan.find(plan)
    logger.info(plan.name)
    text = "<b>{}</b>\n\n{}".format(plan.name,plan.description)
    await callback.answer(cache_time=1)
    await callback.message.edit_text(text,reply_markup=plan_menu(plan.id))

async def checkout_first(callback: CallbackQuery, provider, plan, **kwargs):
    plan = Plan.find(plan)
    logger.info(plan.name)
    text = "И тут мы начинаем заполнять анкету.."
    await callback.answer(cache_time=1)
    await callback.message.edit_text(text)

@dp.callback_query_handler(shop_cd.filter())
async def shop_navigate(call: CallbackQuery, callback_data: dict):
    logger.info(callback_data)
    current_level = callback_data.get("level")
    provider = callback_data.get("provider")
    plan = callback_data.get("plan")
    levels = {
        "0": show_menu,
        "1": show_provider,
        "2": show_plan,
        "3": checkout_first
    }
    current_level_function = levels[current_level]
    await current_level_function(
        call,
        provider=provider,
        plan=plan
    )


