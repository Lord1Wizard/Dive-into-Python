import time
import pywinauto
from pywinauto.application import Application
from PIL import ImageGrab
# import telebot

def find_and_activate_window(window_title):
    try:
        app = Application(backend="uia").connect(best_match=window_title)
        app_dialog = app.window(best_match=window_title)
        app_dialog.set_focus()
        return True
    except pywinauto.application.ProcessNotFoundError:
        return False

def refresh_and_take_screenshot(screenshots_save_path):
    # Нажимаем на кнопку Refresh
    pywinauto.keyboard.send_keys('{TAB}')
    pywinauto.keyboard.send_keys('{ENTER}')

    # Добавим небольшую задержку перед снятием скриншота после обновления
    time.sleep(1)

    # Делаем скриншот
    screenshot = ImageGrab.grab()

    # Сохраняем скриншот
    screenshot_file_path = screenshots_save_path + "brightness_screenshot.png"
    screenshot.save(screenshot_file_path)
    print(f"Скриншот окна 'Brightness Adjustment(No Hardware)' сохранен в '{screenshot_file_path}'")

    # Отправляем скриншот вам в телеграме
    send_telegram_message(screenshot_file_path)

def send_telegram_message(file_path):
    bot_token = "6622992261:AAHVQymwfkKtO6jr8suVpIBGVDV979g7WUI"  # Замените на свой токен бота
    chat_id = "1368687157"  # Замените на свой chat_id

    try:
        bot = telebot.TeleBot(bot_token)
        with open(file_path, "rb") as file:
            bot.send_photo(chat_id, file)
        print("Скриншот отправлен вам в телеграме.")
    except Exception as e:
        print(f"Произошла ошибка при отправке скриншота в телеграме: {e}")

def main():
    # Укажите заголовок окна NovaLCT
    app_title = "NovaLCT"

    # Путь для сохранения скриншотов
    screenshots_save_path = "C:/MyProjects/Python/rabota/Screens/"

    # Укажите путь для сохранения значения яркости
    brightness_file_path = "C:/MyProjects/Python/rabota/Brightness/brightness.txt"

    # Попробуем найти и активировать окно NovaLCT
    if find_and_activate_window(app_title):
        # Проверим, есть ли уже открытое окно Brightness Adjustment(No Hardware)
        if not find_and_activate_window("Brightness Adjustment(No Hardware)"):
            # Найдем кнопку Brightness и кликнем на нее
            try:
                app = Application(backend="uia").connect(title=app_title)
                app_dialog = app.window(title=app_title)

                # Входим во вкладку Brightness
                app_dialog.child_window(title="Brightness", control_type="TabPage").click_input()

                # Добавим небольшую задержку перед сохранением значения яркости
                time.sleep(1)

                # Найдем элемент, содержащий значение яркости
                brightness_element = app_dialog.child_window(title="Current Brightness", control_type="Text")
                brightness_value = brightness_element.get_value()
                with open(brightness_file_path, 'w') as file:
                    file.write(brightness_value)
                print(f"Значение яркости сохранено в '{brightness_file_path}'")

                # Вызываем функцию для обновления и снятия скриншота в окне Brightness Adjustment(No Hardware)
                refresh_and_take_screenshot(screenshots_save_path)

            except Exception as e:
                print(f"Произошла ошибка при сохранении значения яркости: {e}")
        else:
            # Если окно Brightness Adjustment(No Hardware) уже открыто, просто выполняем обновление и снимаем скриншот
            refresh_and_take_screenshot(screenshots_save_path)
    else:
        print("Окно NovaLCT не найдено.")

if __name__ == "__main__":
    main()
