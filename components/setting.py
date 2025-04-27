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
                        DashIconify(icon="clarity:download-line"), color="black", variant="transparent", style={"width": "30px", "height": "30px"},
                        id="download-button",
                        n_clicks=0,
                    ),
                    dmc.ActionIcon(
                        DashIconify(icon="clarity:settings-line"), color="black", variant="transparent", style={"width": "30px", "height": "30px"},
                        id="interest-button",
                        n_clicks=0,
                    ),
                ],
                gap="lg",
            )
        ]
    )

