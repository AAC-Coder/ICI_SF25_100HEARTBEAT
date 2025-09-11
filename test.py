import flet as ft
import openpyxl
import os
import sys
import asyncio
import time
import subprocess



class Countdown(ft.Text):
    def __init__(self, seconds: int, heartbeat_script: str = "heartbeat.py", style=None, ref=None):
        super().__init__(value=str(seconds), style=style, ref=ref)
        self.seconds = seconds
        self.heartbeat_script = heartbeat_script
        self.started = False

    def did_mount(self):
        # Don't start automatically - wait for manual start
        self.running = False

    def will_unmount(self):
        self.running = False

    def start(self):
        if not self.started:
            self.started = True
            self.running = True
            self.page.run_task(self._update_timer)

    async def _update_timer(self):
        # locate your heartbeat.py next to this script
        script_path = os.path.join(os.path.dirname(__file__), self.heartbeat_script)

        while self.running and self.seconds > 0:
            await asyncio.sleep(1)
            # 1. Decrement and update UI
            self.seconds -= 1
            self.value = str(self.seconds)
            self.update()

            # 2. Fire off heartbeat.py in a non-blocking way
            if os.path.isfile(script_path):
                # Use the same Python interpreter
                subprocess.Popen(
                    [sys.executable, script_path],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                )
            else:
                print(f"heartbeat script not found at: {script_path}")

        # When countdown ends
        if self.running:
            self.value = "⏰ Time's up!"
            self.update()

async def main(page: ft.Page):
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
    qnum_label_ref = ft.Ref[ft.Text]()
    qnum_value_ref = ft.Ref[ft.Text]()
    refdisqnumber_val_ref = ft.Ref[ft.Text]()

    # my variables
    logo_ref = ft.Ref[ft.Image]() # current logo
    current_logo = "nologo.png"
    timer_running = False
    countdown_ref = ft.Ref[Countdown]()  # Reference to countdown instance



    def selector():

        nonlocal current_logo
        print(f"Selector called with key: {key_display.value}")
        try:
            question_displayq = 0
            if refdisqnumber_val_ref.current is not None and refdisqnumber_val_ref.current.value.isdigit():
                question_displayq = int(refdisqnumber_val_ref.current.value)

            currentqnum = int(qnum_value_ref.current.value)
            if key_display.value == "Arrow Right":
                qnum_value_ref.current.value = str(currentqnum + 1)

            
            elif key_display.value == "Arrow Left":
                if currentqnum >= 1:
                    qnum_value_ref.current.value = str(currentqnum - 1)
    


            #Selecting specific cell
            if key_display.value == "Arrow Up":
                question_displayq = question_displayq + 1
                print(question_displayq)
                print("Hit: cell selector increment")
                print(refdisqnumber_val_ref.current.value)
                #return question_displayq
                refdisqnumber_val_ref.current.value = str(question_displayq)
            elif key_display.value == "Arrow Down":
                if question_displayq >= 1:
                    question_displayq = question_displayq - 1
                    print(question_displayq)
                    print("Hit: cell selector decrement")
                    print(refdisqnumber_val_ref.current.value)
                    refdisqnumber_val_ref.current.value = str(question_displayq)
                    #return question_displayq

           #selecting team  
            elif key_display.value =="0":
                current_logo = "nologo.png"
            elif key_display.value =="1":
                current_logo = "fire.png"
            elif key_display.value =="2":
                current_logo = "wind.png"
            elif key_display.value =="3":
                current_logo = "earth.png"
            elif key_display.value =="4":
                current_logo = "water.png"

            
            print(f"Question display cue number: ", question_displayq)



            logo_ref.current.src = current_logo
        except Exception as ex:
            current = int(qnum_value_ref.current.value)
            #qnum_value_ref.current.value = "Err"

        
        # CALLING THE CURRENNT QUESTION NUMBER
        current_question_number()



        

        page.update()

    def sheet_selector():
        print(current_logo)
        
        current_sheet=""
        if current_logo == "fire.png":
            current_sheet = f"R{qnum_value_ref.current.value}-FIRE"
        elif current_logo =="wind.png":
            current_sheet = f"R{qnum_value_ref.current.value}-WIND"
        elif current_logo == "earth.png":
            current_sheet = f"R{qnum_value_ref.current.value}-EARTH"
        elif current_logo == "water.png":
            current_sheet = f"R{qnum_value_ref.current.value}-WATER"

        return current_sheet


    def current_question_number():
        #os._exit(0)
        try:
            wb = openpyxl.load_workbook("SF2025_PAUTAKAN_100HEARTBEAT.xlsx")
            sheet_name = sheet_selector() # name of the current sheet
            print(current_logo)
            print("Current sheet Name: ", sheet_name)
            if sheet_name not in wb.sheetnames:
                question_value_ref.current.value = f"❌ Sheet '{sheet_name}' not found"
                print("Current sheet Name: ", sheet_name)
                return
            sheet = wb[sheet_name]
            # Select cell based on question number (e.g., row = question number, column = B)
            qnum = int(qnum_value_ref.current.value)
            #qnum = int(refdisqnumber_val_ref.current.value)
            #qnum = cell_selector()
            #cell_ref = f"A{qnum}"  # You can change column as needed
            #cell_ref = f"A{refddisqnumber_val_ref.current.value}"  # You can change column as needed
            cell_ref = f"A{refdisqnumber_val_ref.current.value}"  # You can change column as needed
            #cell_ref = f"A{cell_selector()}"  # You can change column as needed

            cell_value = sheet[cell_ref].value
            question_value_ref.current.value = f"Q{qnum}: {cell_value}" if cell_value else "⚠️ Cell is empty"
            print("Current sheet Name: ", sheet_name)

            #Answer Text
            cell_ref_ans = f"B{refdisqnumber_val_ref.current.value}"
            cell_value_ans = sheet[cell_ref_ans].value
            print(f"{cell_value_ans}")

            # Start countdown if selected cell is A2
            if refdisqnumber_val_ref.current.value == "2":
                if countdown_ref.current is not None:
                    countdown_ref.current.start()

        except Exception as e:
            print(f"⚠️ current question function Error: {type(e).__name__} - {e}")


    


    def on_keyboard(e: ft.KeyboardEvent):
        key_display.value = f"{e.key}"
        modifiers_display.value = f"Shift: {e.shift}, Ctrl: {e.ctrl}, Alt: {e.alt}, Meta: {e.meta}"
        print(f"Key pressed: {e.key}")
        selector()
        page.update()
    page.on_keyboard_event = on_keyboard
    key_display = ft.Text("", opacity=0.2,)
    
    modifiers_display = ft.Text("Modifiers: ")


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

                ft.Image(
                    src="nologo.png",
                    width=40,
                    height=40,
                    fit=ft.ImageFit.CONTAIN,
                    #left=580,
                    left=1070,
                    top=120,
                    ref=logo_ref
                ),
                
                #ft.Text("Press any key...", opacity=0.5),
                key_display,
                #modifiers_display,


                # Scoreboard section
                ft.Container(
                    content=ft.Stack(
                        controls=[
                            ft.Container(
                                content=ft.Text("Question Number: ", style=ft.TextStyle(font_family="digital-7",size=20), ref=qnum_label_ref),
                                alignment=ft.alignment.top_left,
                                left=210,
                                top=140,
                            ),
                            ft.Container(
                                content=ft.Text("0", style=ft.TextStyle(font_family="digital-7",size=20), ref=qnum_value_ref),
                                alignment=ft.alignment.top_left,
                                left=370,
                                top=140,
                            ),
                            ft.Container(
                                content=ft.Text("TIME", style=ft.TextStyle(font_family="digital-7", size=30), ref=time_label_ref),
                                alignment=ft.alignment.top_left,
                                left=60,
                                top=200,
                            ),
                            ft.Container(
                                #Countown timer
                                content=Countdown(seconds=100, heartbeat_script="heartbeat.py", style=ft.TextStyle(font_family="digital-7", size=60), ref=countdown_ref),
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
                                content=ft.Text("00", style=ft.TextStyle(font_family="digital-7", size=60), ref=round_value_ref),
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
                            ft.Container(
                                #######################
                                content=ft.Text("0", style=ft.TextStyle(font_family="digital-7", size=20), ref=refdisqnumber_val_ref),
                                alignment=ft.alignment.top_left,
                                left=20,
                                top=600,
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
                            #bgcolor=ft.Colors.WHITE
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
