
from pywinauto.application import Application


app = Application(backend="uia").start('C://Windows//System32//calc.exe')

# Опишем окно, которое хотим найти в процессе Notepad.exe
dlg_spec = app.window(best_match='Калькулятор')
# ждем пока окно реально появится
actionable_dlg = dlg_spec.wait('visible')
print('222')