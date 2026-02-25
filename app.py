import solara
import os
from supabase import create_client

# Connect using the private secrets we set up
supabase = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))

@solara.component
def Page():
    # Let's check who is logged in (Simulated for this step)
    current_email = "admin@example.com" 
    
    # Check the database for the role
    user_data = supabase.table("profiles").select("role").eq("email", current_email).single().execute()
    role = user_data.data.get("role") if user_data.data else "user"

    with solara.Column(align="center"):
        solara.Header("Expert Accounting System")
        
        if role == "admin":
            with solara.Card("ADMIN CONTROL PANEL", style={"background-color": "#f0f8ff"}):
                solara.Markdown("### Change Global Signup Bonus")
                solara.Success("Status: Database Connected")
                solara.Button("Set Bonus to 500 Credits", color="primary")
        else:
            with solara.Card("USER DASHBOARD"):
                solara.Info(f"Welcome, {current_email}!")
                solara.Markdown("Your current balance: **100 Credits**")

Page()
