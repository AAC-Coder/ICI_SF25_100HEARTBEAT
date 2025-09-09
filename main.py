import flet as ft

def main(page: ft.Page):
    page.title = "ICI 2025 SF PAUTAKAN"
    
    page.window_full_screen = False
    page.window_resizable = False  # Optional: prevent resizing
    page.window_maximized = True

    def on_click(e):
        page.snack_bar = ft.SnackBar(ft.Text("Button clicked!"))
        page.snack_bar.open = True
        page.update()

    page.add(
        ft.Stack(
            expand=True,
            controls=[
                # Background image centered and scaled to fit
                ft.Image(
                    src="bg_1.png",
                    expand=True,
                    fit=ft.ImageFit.CONTAIN,

                ),

                # Button anchored to bottom center
                ft.Container(
                    content=ft.ElevatedButton("START", on_click=on_click),
                    opacity=0,
                    bottom=60,
                    left=0,
                    right=0,
                    alignment=ft.alignment.bottom_center
                )
            ]
        )
    )

ft.app(target=main)
