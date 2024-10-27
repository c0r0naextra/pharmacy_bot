import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardRemove
from aiogram import Router
from kb import KeyboardManager
from config import API_TOKEN





bot = Bot(token=API_TOKEN)
router = Router()
dp = Dispatcher()

manufacturers = ["Омепразол, 20 мг, капс. №30 (Озон, ООО (Россия)) 💊", "Омепразол, 20 мг, капс. №30 (Синтез, ОАО (Россия)) 💊", "Омепразол, 40 мг, флак. №1 (Красфарма, ПАО (Россия)) 💊", "Омез, 40 мг, флак. №1 (Dr.Reddy's Laboratories Ltd (Индия)) 💊"]
start_buttons = ["🔍 Поиск лекарств", "Как пользоваться❓"]
pharmacy_info = (
        "🔺🔻🔺🔻🔺🔻🔺🔻🔺🔻\n\n"
        "Аптека № 1\n"
        "Лекарство: Омепразол, 20 мг, капс. №30\n"
        "Производитель: Озон, ООО (Россия)\n\n"
        "Аптека: Вита Экспресс\n"
        "Адрес: г. Самара, ул. Водников, 28/30\n"
        "Цена: 308 руб.\n"
        "Телефон: +78007550003\n"
        "🗺 [На карте](https://yandex.ru/maps/org/vita_ekspress/30350056438/?ll=50.250316%2C53.242025&mode=search .)"
        "\n\n"
        "🔺🔻🔺🔻🔺🔻🔺🔻🔺🔻\n\n"
        "Аптека № 2\n"
        "Лекарство: Омепразол, 20 мг, капс. №30\n"
        "Производитель: Синтез, ОАО (Россия)\n\n"
        "Аптека: Здравсити\n"
        "Адрес: г. Самара, ул. Ново-Садовая, 6\n"
        "Цена: 43 руб.\n"
        "Телефон: +78005009262\n"
        "🗺 [На карте](https://yandex.ru/maps/org/zdravsiti/19005758164/?ll=50.125822%2C53.206564&z=17)\n\n"
        "🔺🔻🔺🔻🔺🔻🔺🔻🔺🔻\n\n"
        "Аптека № 3\n"
        "Лекарство: Омез, 40 мг, флак. №1\n"
        "Производитель: Dr.Reddy's Laboratories Ltd (Индия)\n\n"
        "Аптека: Фармленд\n"
        "Адрес: г. Самара, ул. Демократическая, 23\n"
        "Цена: 295,59 руб.\n"
        "Телефон: +78462010019\n"
        "🗺 [На карте](https://yandex.ru/profile/76360490854?ysclid=m1404fvhn846190607 .)"
        "\n\n"
        "🔺🔻🔺🔻🔺🔻🔺🔻🔺🔻\n\n"
        "Аптека № 4\n"
        "Лекарство: Омепразол, 40 мг, флак. №1\n"
        "Производитель: Красфарма, ПАО (Россия)\n\n"
        "Аптека: Аптека Плюс\n"
        "Адрес: г. Самара, ул. Владимирская, 35А \n"
        "Цена: 179 руб.\n"
        "Телефон: +78462770982\n"
        "🗺 [На карте](https://yandex.ru/profile/13381887019?no-distribution=1&view-state=mini&source=wizbiz_new_map_single .)"
        "\n\n"
        "🔺🔻🔺🔻🔺🔻🔺🔻🔺🔻\n\n"
    )



kb_manager = KeyboardManager(start_buttons=start_buttons, manufacturers=manufacturers)

@router.message(Command("start"))
async def start_command(message: types.Message):
    await message.answer(f"Добро пожаловать! Выберете раздел",
                         reply_markup=kb_manager.get_start_keboard())


@router.message(lambda message: message.text == "🔍 Поиск лекарств")
async def drug_search(message: types.Message):
    await message.answer("Введите название препарата", reply_markup=ReplyKeyboardRemove())


@router.message(lambda message: message.text == "Как пользоваться❓")
async def help(message: types.Message):
    await message.answer("Нажмите 🔍 Поиск лекарств и введите нужный вам препарат")


@router.message(lambda message: message.text == "Назад")
async def back_to_start(message: types.Message):
    await message.answer("Вы вернулись в главное меню", reply_markup=kb_manager.get_start_keboard())



@router.message(lambda message: message.text.lower() == "омепразол")
async def the_drug(message: types.Message):
    await message.answer("Пожалуйста, выберите лекарство из списка", reply_markup=kb_manager.get_manufacturer_keyboard())


@router.message()
async def send_pharmacy(message: types.Message):
    for manufacturer in manufacturers:
        if message.text == manufacturer:
            await message.answer(pharmacy_info, parse_mode="Markdown", disable_web_page_preview=True)  


async def main():
    dp.include_router(router)

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())




