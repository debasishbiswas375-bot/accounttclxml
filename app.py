import solara
import os
from supabase import create_client

# 1. Connect to Supabase
supabase = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))

# 2. State Management
user_id = solara.reactive(None)
user_role = solara.reactive("user")

@solara.component
def AdminInterface():
    with solara.Sidebar():
        solara.Markdown("### Admin Panel")
        solara.Button("Manage Users")
        solara.Button("Global Settings")
        
    with solara.Column():
        solara.Header("Control Center")
        solara.Success("Status: Operational")
        # Here you can add the "Plan Manager" we discussed!

@solara.component
def UserInterface():
    with solara.Column(align="center"):
        solara.Header("User Dashboard")
        solara.Info("Welcome! You have successfully claimed your Signup Reward.")

@solara.component
def Page():
    # Simple check: If not logged in, show login buttons
    if not user_id.value:
        with solara.Column(align="center"):
            solara.Markdown("# Professional Portal")
            solara.Button("Login as Admin", on_click=lambda: (user_role.set("admin"), user_id.set("123")))
            solara.Button("Login as User", on_click=lambda: (user_role.set("user"), user_id.set("456")))
    else:
        # The Switch: Show different UI based on role
        if user_role.value == "admin":
            AdminInterface()
        else:
            UserInterface()

Page()
