import pynecone as pc

# openai.api_key = "YOUR_API_KEY"

class State(pc.State):
    pass

def index():
    return pc.center(
        pc.vstack(
            pc.heading("Blade", font_size="1.5em"),
            pc.input(placeholder="Sample Input"),
            pc.button(
                pc.icon(tag="MoonIcon"),
                on_click=pc.toggle_color_mode,
            ),
            pc.divider(),
            padding="2em",
            shadow="lg",
            border_radius="lg",
        ),
        width="100%",
        height="100vh",
        font_family="Inter",
        bg="radial-gradient(circle at 22% 11%,rgba(62, 180, 137,.20),hsla(0,0%,100%,0) 19%)",
    )

# Add state and page to the app.
app = pc.App(state=State)
app.add_page(index, title="Pynecone:Blade")
app.compile()