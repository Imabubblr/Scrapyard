from cx_Freeze import setup, Executable

setup(
    name="Fun Scrapyards",
    version="1.0",
    description="My Python Application",
    executables=[Executable("Main.py")]
)