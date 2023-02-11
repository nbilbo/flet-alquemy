import flet as ft


class AppBar(ft.AppBar):
    def __init__(self) -> None:
        super().__init__()
        self.leading = ft.Icon()
        self.title = ft.Text()
        self.exit_button = ft.IconButton()
        self.about_button = ft.TextButton()

        self.leading.name = ft.icons.BOOK
        self.leading.size = 30

        self.about_button.text = 'About'
        self.about_button.icon = ft.icons.INFO

        self.title.value = 'Todo Application'
        self.title.font_family = 'Roboto-Medium'

        self.exit_button.icon = ft.icons.EXIT_TO_APP
        self.exit_button.tooltip = 'Exit'

        self.actions.append(self.about_button)
        self.actions.append(self.exit_button)