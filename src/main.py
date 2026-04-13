import flet as ft
from controllers.UserController import AuthController
from controllers.TareaController import TareaController
from views.LoginView import LoginView
from views.Dashboard import DashboardView

def main(page: ft.Page):
    # Instanciamos los controladores una sola vez
    auth_ctrl = AuthController()
    task_ctrl = TareaController()

    def route_change(route):
        page.views.clear()
        if page.route == "/":
            page.views.append(LoginView(page, auth_ctrl))
        elif page.route == "/dashboard":
            page.views.append(DashboardView(page, task_ctrl))
        # Agregas aqui el registro_view de la misma forma
        page.update()

    page.on_route_change = route_change
    page.go("/")

if __name__ == "_main_":
    ft.app(main)