import dash_mantine_components as dmc

def render_setting_buttons():
    return dmc.Flex(
        justify="flex-end",
        align="center",
        style={"height": "100%"},
        children=[
            dmc.Group(
                [
                    dmc.Button("다운로드", id="download-button", color="blue"),
                    dmc.Button("관심사 설정", id="interest-button", color="gray"),
                ],
                gap="lg",
            )
        ]
    )

