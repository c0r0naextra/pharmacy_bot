from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


class KeyboardManager:
    def __init__(self, start_buttons, manufacturers):
        self.start_buttons = start_buttons
        self.manufacturers = manufacturers

    def get_start_keboard(self):
        keyboard = [
            [KeyboardButton(text=start_button)] for start_button in self.start_buttons
            ]
        return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)
    
    def get_manufacturer_keyboard(self):
        keyboard = [[KeyboardButton(text=manufacturer)] for manufacturer in self.manufacturers]
        keyboard.append([KeyboardButton(text="Назад")]) 
        return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)