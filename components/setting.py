import dash_mantine_components as dmc
from dash_iconify import DashIconify

def render_setting_buttons():
    return dmc.Flex(
        justify="flex-end",
        align="center",
        style={"height": "100%"},
        children=[
            dmc.Group(
                [
                    dmc.ActionIcon(
                        DashIconify(icon="material-symbols:download-rounded", width=35, height=35), 
                        color="black", 
                        variant="transparent", 
                        style={"width": "25px", "height": "25px"},
                        id="download-button",
                        n_clicks=0,
                    ),
                    dmc.ActionIcon(
                        DashIconify(icon="material-symbols:settings-rounded", width=35, height=35), 
                        color="black", 
                        variant="transparent", 
                        style={"width": "25px", "height": "25px"},
                        id="interest-button",
                        n_clicks=0,
                    ),
                ],
                gap="lg",
            )
        ]
    )

