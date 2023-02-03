import pynecone as pc


config = pc.Config(
    app_name="Blade_Web",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)
