import flet as ft
from app.components.banners.generic_banner import GenericBanner


class DangerousBanner(GenericBanner):
    def __init__(self, page: ft.Page, message: str) -> None:
        super().__init__(page, message)
        self.bgcolor = ft.colors.RED_500
        self.leading.name = ft.icons.DANGEROUS
