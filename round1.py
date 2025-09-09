import flet as ft

def main(page: ft.Page):
    page.title = "ICI 2025 SF PAUTAKAN"

    page.window_full_screen = False
    page.window_resizable = False
    page.window_maximized = True

    # Define refs for dynamic text updates
    time_label_ref = ft.Ref[ft.Text]()
    time_value_ref = ft.Ref[ft.Text]()
    round_label_ref = ft.Ref[ft.Text]()
    round_value_ref = ft.Ref[ft.Text]()
    score_label_ref = ft.Ref[ft.Text]()
    score_value_ref = ft.Ref[ft.Text]()
    question_value_ref = ft.Ref[ft.Text]()
    ans_value_ref = ft.Ref[ft.Text]()

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
                    src="bg_2.png",
                    expand=True,
                    fit=ft.ImageFit.CONTAIN,
                ),

                # Scoreboard section
                ft.Container(
                    content=ft.Stack(
                        controls=[
                            ft.Container(
                                content=ft.Text("TIME", style=ft.TextStyle(font_family="digital-7", size=30), ref=time_label_ref),
                                alignment=ft.alignment.top_left,
                                left=60,
                                top=200,
                            ),
                            ft.Container(
                                content=ft.Text("100", style=ft.TextStyle(font_family="digital-7", size=60), ref=time_value_ref),
                                alignment=ft.alignment.top_left,
                                left=60,
                                top=250,
                            ),
                            ft.Container(
                                content=ft.Text("ROUND", style=ft.TextStyle(font_family="digital-7", size=30), ref=round_label_ref),
                                alignment=ft.alignment.top_left,
                                left=60,
                                top=350,
                            ),
                            ft.Container(
                                content=ft.Text("01", style=ft.TextStyle(font_family="digital-7", size=60), ref=round_value_ref),
                                alignment=ft.alignment.top_left,
                                left=80,
                                top=400,
                            ),
                            ft.Container(
                                content=ft.Text("SCORE", style=ft.TextStyle(font_family="digital-7", size=30), ref=score_label_ref),
                                alignment=ft.alignment.top_left,
                                left=60,
                                top=500,
                            ),
                            ft.Container(
                                content=ft.Text("000", style=ft.TextStyle(font_family="digital-7", size=60), ref=score_value_ref),
                                alignment=ft.alignment.top_left,
                                left=60,
                                top=550,
                            ),
                        ]
                    ),
                ),

                # Manually positioned Card panel (x = 100, y = 100)
                ft.Container(
                    content=ft.Card(
                        content=ft.Container(
                            content=ft.Column(
                                controls=[
                                    ft.Text("SPORTS FESTIVAL 2025 PAUTAKAN", size=20, weight=ft.FontWeight.BOLD, ref=question_value_ref),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER
                            ),
                            width=930,
                            height=400,
                            padding=20,
                            #bgcolor=ft.Colors.WHITE,
                            bgcolor="#ca0046",
                            opacity=1,
                            border_radius=20
                        ),
                        elevation=6
                    ),
                    left=195,  # X-axis position
                    top=160    # Y-axis position
                ),
                ft.Container(
                    content=ft.Card(
                        content=ft.Container(
                            content=ft.Column(
                                controls=[
                                    ft.Text("ANSWER HERE", size=20, weight=ft.FontWeight.BOLD, ref=ans_value_ref),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER
                            ),
                            width=930,
                            height=62,
                            padding=20,
                            #bgcolor=ft.Colors.WHITE,
                            bgcolor="#ca0046",
                            opacity=1,
                            border_radius=20
                        ),
                        elevation=6
                    ),
                    left=195,  # X-axis position
                    top=570    # Y-axis position
                )

            ]
        )
    )

ft.app(target=main)