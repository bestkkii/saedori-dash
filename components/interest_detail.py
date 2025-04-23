import dash_mantine_components as dmc

def render_interest_detail(title="관심사", description="관심사 세부 내용"):
    return dmc.Card(
        [
            dmc.Text(title, weight=700, size="lg", mb="xs"),
            dmc.Text(description, size="sm", color="dimmed"),
        ],
        shadow="sm",
        radius="md",
        withBorder=True,
        h="100%"  # height: 100%
    )
