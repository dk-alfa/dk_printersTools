"""Точка входа в скрипт dk_pt
Написана Дмитрием Кораблевым инженером отдела IT ООО Альфа-Сервис
Дата первого коммита 2024-07-26
"""
import sys
from controller.app import App

if __name__ == '__main__':
    """
    Создать экземпляр класса App
    запустить экземпляр класса
    """
    printers_tools_app = App
    printers_tools_app.run(printers_tools_app, sys.argv)
