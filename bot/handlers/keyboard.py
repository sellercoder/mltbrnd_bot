# IMPORTS ##################################################
# aiogram packages
from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import KeyboardButton
from aiogram.types import InlineKeyboardButton
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData
from api import *
# END IMPORTS ######################################

shop_cd = CallbackData('shop','level','provider','plan')
def make_shop_nav(level, provider="0", plan="0"):
    return shop_cd.new(level=level, provider=provider, plan=plan)


def catalog_menu():
    markup = InlineKeyboardMarkup(row_width=1)

    providers = getProviders()

    for provider in providers:
        btn = InlineKeyboardButton(
            text=provider.name,
            callback_data=make_shop_nav(
                level=1,
                provider=provider.id)
            )
        markup.insert(btn)

    return markup


def provider_menu(provider_id):

    CURRENT_LEVEL = 1

    provider = getProvider(provider_id)
    plans = provider.plans

    markup = InlineKeyboardMarkup(row_width=1)

    back_clb = make_shop_nav(level=CURRENT_LEVEL - 1)
    back_btn = InlineKeyboardButton(
        text="⬅️ Операторы",callback_data=back_clb)

    for plan in plans:
        plan_cb = make_shop_nav(
            level=CURRENT_LEVEL + 1,
            provider=provider.id,
            plan=plan.id)
        plan_btn = InlineKeyboardButton(
            text=f"{plan.name}",
            callback_data=plan_cb)
        markup.insert(plan_btn)

    markup.row(back_btn)
    return markup

def plan_menu(plan_id):

    CURRENT_LEVEL = 2

    plan = Plan.find(plan_id)
    provider = plan.provider

    markup = InlineKeyboardMarkup(row_width=1)

    back_clb = make_shop_nav(
        level=CURRENT_LEVEL - 1,
        provider=provider.id)
    back_btn = InlineKeyboardButton(
        text="⬅️ К тарифам",callback_data=back_clb)

    get_clb = make_shop_nav(
        level=CURRENT_LEVEL + 1,
        provider=provider.id,
        plan=plan.id)
    get_btn = InlineKeyboardButton(
        text="Оформить тариф",callback_data=get_clb)

    url_btn = InlineKeyboardButton(
        text="Подробная информация",url="https://ya.ru")

    markup.row(get_btn)
    markup.row(url_btn)
    markup.row(back_btn)
    return markup











