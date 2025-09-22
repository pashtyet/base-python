from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.pretty import pprint
from rich import box
'''import pprint'''
console = Console()
import os, json, requests
TOKEN = '8092607759:AAEgLwt8CephXgF6XGKz5Oi2yBXyy3UPSYU'
API = f"https://api.telegram.org/bot{TOKEN}"
ADMINID = "5082258749"
def print_help():
    console.print(Panel.fit(
        """[bold]Команды:[/bold]
token            — показать текущий токен
set-token        — ввести новый токен (сменит API базу)
chat             — показать текущий chat_id
set-chat         — ввести chat_id администрации вручную
send-menu        — отправить inline-панель администратору
fetch            — единоразово получить апдейты (getUpdates)
list             — показать последние апдейты в виде таблицы
offset           — показать текущий offset
offset next      — сдвинуть offset = last_update_id + 1
offset reset     — сбросить offset = None
handle <i>       — обработать апдейт № i (например, callback_query)
quit             — выйти
bot-info         — информация о боте
send-test-message— отправить тестовое сообщение
""",
        title="Console Inline Keyboard Trainer", border_style="cyan"))

def send_test_message():
    recipient=input('Кому отправить — ToAll, AdminID, CustomID')
    test_message_text=input('Что отправить?')
    if recipient == 'AdminID':
        requests.get(f'{API}/sendMessage?chat_id={ADMINID}&text={test_message_text}')
    elif recipient == 'CustomID':
        recipientID=input('ID получателя')
        requests.get(f'{API}/sendMessage?chat_id={recipientID}&text={test_message_text}')
    elif recipient == 'ToAll':
        print('In process')
def show_token():
    console.print(f"[bold]TOKEN:[/bold] {TOKEN}")
def get_updates():
    response = requests.get(f'{API}/getUpdates')
    pprint(response.json())
def show_bot_info():
    response = requests.get(f'{API}/getMe')
    pprint(response.json())
# === Главный REPL (без фонового опроса) ===
def show_chat():
    pass
def main():
    console.print(Panel.fit(
        "Inline Keyboards — ручной тренажёр на чистом Bot API\n"
        "Получаем апдейты [bold]по запросу[/bold], обрабатываем их вручную.",
        border_style="cyan"
    ))
    print_help()
    while True:
        cmd = input("\n> ").strip()
        if not cmd:
            continue
        if cmd == "help":
            print_help()
        elif cmd == "quit":
            break
        elif cmd == "token":
            show_token()
        elif cmd == "chat":
            show_chat()
        elif cmd == "bot-info":
            show_bot_info()
        elif cmd == "fetch":
            get_updates()
        elif cmd == "send_test_message":
            send_test_message()




if __name__ == "__main__":
    main()
