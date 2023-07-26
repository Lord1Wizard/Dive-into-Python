import time
import pywinauto
from pywinauto.application import Application
from PIL import ImageGrab
# import telebot
import pywinauto.findwindows as findwindows

# Укажите заголовок окна NovaLCT
APP_TITLE = "NovaLCT V5.4.4.6(No Hardware)"

# Путь для сохранения скриншотов
# SCREENSHOTS_SAVE_PATH = "C:/temp/"
SCREENSHOTS_SAVE_PATH = "C:/MyProjects/Python/rabota/Screens/"

# Укажите путь для сохранения значения яркости
# BRIGHTNESS_FILE_PATH = "C:/temp/brightness.txt"
BRIGHTNESS_FILE_PATH = "C:/MyProjects/Python/rabota/Brightness/brightness.txt"

def print_available_windows():
    windows = findwindows.find_windows()
    for window in windows:
        window_title = window
        # findwindows.GetWindowText(window)
        print(window_title)
        
def find_and_activate_window(window_title):
    try:
        app = Application(backend="uia").connect(title=window_title)
        app_dialog = app.window(title=window_title)
        app_dialog.set_focus()
        print(app.process)
        return True
    # except pywinauto.findbestmatch.MatchError:
    except pywinauto.findwindows.ElementNotFoundError:
        return False

def refresh_and_take_screenshot(SCREENSHOTS_SAVE_PATH):
    # Нажимаем на кнопку Refresh
    pywinauto.keyboard.send_keys('{TAB}')
    pywinauto.keyboard.send_keys('{ENTER}')

    # Добавим небольшую задержку перед снятием скриншота после обновления
    time.sleep(1)

    # Делаем скриншот
    screenshot = ImageGrab.grab()

    # Сохраняем скриншот
    screenshot_file_path = SCREENSHOTS_SAVE_PATH + "brightness_screenshot.png"
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

def open_novalct_if_not_running(APP_TITLE):
    try:
        # Попробуем найти окно NovaLCT, если окно не найдено, то запустим NovaLCT
        if not(find_and_activate_window(APP_TITLE)) :
            try:
                # Если NovaLCT не запущен, то запускаем его
                app_path = r"C:\\Users\\Wizard\\AppData\\Roaming\\Nova Star\\NovaLCT\\Bin\\NovaLCT.exe"
                app = Application().start(app_path)  # Замените на путь к исполняемому файлу NovaLCT
                app.wait_cpu_usage_lower(threshold=0.5, timeout=60)  # Ждем, пока NovaLCT полностью загрузится
            except Exception as e:
                print(f"Произошла ошибка при запуске NovaLCT: {e}")

    except pywinauto.application.ProcessNotFoundError:
        pass

def main():
    


    # Запускаем NovaLCT, если он не запущен
    open_novalct_if_not_running(APP_TITLE)

    # Выведем список всех доступных окон (для отладки)
    # print_available_windows()

    # Попробуем найти и активировать окно NovaLCT
    if find_and_activate_window(APP_TITLE):
        # pass
        # Проверим, есть ли уже открытое окно Brightness Adjustment(No Hardware)
        if not find_and_activate_window("Brightness Adjustment(No Hardware)"):
            # Найдем кнопку Brightness и кликнем на нее
            try:
                app = Application(backend="uia").connect(title=APP_TITLE)
                app_dialog = app.window(title=APP_TITLE)

                # Входим во вкладку Brightness
                app_dialog.child_window(title="Brightness", control_type="Button").click()

                # Добавим небольшую задержку перед сохранением значения яркости
                time.sleep(1)

                # Найдем элемент, содержащий значение яркости
                brightness_element = app_dialog.child_window(title="Current Brightness", control_type="Text")
                brightness_value = brightness_element.get_value()
                with open(BRIGHTNESS_FILE_PATH, 'w') as file:
                    file.write(brightness_value)
                print(f"Значение яркости сохранено в '{BRIGHTNESS_FILE_PATH}'")

                # Вызываем функцию для обновления и снятия скриншота в окне Brightness Adjustment(No Hardware)
                refresh_and_take_screenshot(SCREENSHOTS_SAVE_PATH)

            except Exception as e:
                print(f"Произошла ошибка при сохранении значения яркости: {e}")
        else:
            # Если окно Brightness Adjustment(No Hardware) уже открыто, просто выполняем обновление и снимаем скриншот
            refresh_and_take_screenshot(SCREENSHOTS_SAVE_PATH)
    else:
        print("Окно NovaLCT не найдено.")

if __name__ == "__main__":
    main()
