# TODO for Modifying recall.round6.py

- [ ] Change Countdown class to inherit from ft.Text instead of ft.TextField
- [ ] Add style parameter to Countdown.__init__ and pass to super()
- [ ] Update round_value_ref and score_value_ref to ft.Ref[ft.Text]()
- [ ] Add style=ft.TextStyle(font_family="digital-7", size=60) to round_value_ref UI element
- [ ] Add style=ft.TextStyle(font_family="digital-7", size=60) to score_value_ref UI element
- [ ] Add style=ft.TextStyle(font_family="digital-7", size=60) to Countdown component
- [ ] Assign time_value_ref to Countdown component's ref
- [ ] Remove read_only logic from Countdown class since it's now ft.Text
- [ ] Update any code that assumes TextField behavior to work with Text
