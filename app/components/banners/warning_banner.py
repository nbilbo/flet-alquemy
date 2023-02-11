import flet as ft
from app.components.banners.generic_banner import GenericBanner


class WarningBanner(GenericBanner):
    def __init__(self, page: ft.Page, message: str) -> None:
        super().__init__(page, message)
        self.bgcolor = ft.colors.AMBER_500
        self.leading.name = ft.icons.WARNING