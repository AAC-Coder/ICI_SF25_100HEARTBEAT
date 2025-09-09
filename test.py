import flet as ft

def main(page: ft.Page):
    def on_keyboard(e: ft.KeyboardEvent):
        key_display.value = f"Key: {e.key}"
        modifiers_display.value = f"Shift: {e.shift}, Ctrl: {e.ctrl}, Alt: {e.alt}, Meta: {e.meta}"
        page.update()

    page.on_keyboard_event = on_keyboard

    key_display = ft.Text("Key: ")
    modifiers_display = ft.Text("Modifiers: ")

    page.add(
        ft.Text("Press any key..."),
        key_display,
        modifiers_display
    )

ft.app(target=main)
