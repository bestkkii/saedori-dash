import dash_mantine_components as dmc

def render_setting_buttons():
    return dmc.Flex(
        justify="flex-end",
        align="center",
        style={"height": "100%"},
        children=[
            dmc.Group(
                [
                    dmc.Button("다운로드", id="download-button", color="blue", n_clicks=0),
                    dmc.Button("관심사 설정", id="interest-button", color="gray", n_clicks=0),
                ],
                gap="lg",
            )
        ]
    )

