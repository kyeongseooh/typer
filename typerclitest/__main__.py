import typer


from typer.models import Default
id_dict = {"root" : "dd98969321"}


app = typer.Typer()

# int = 0과 같이 default값을 주면 option이 된다. --age로 사용해야하며 option은 입력 순서 상관 없이 적용 가능
# default값이 없으면 필수임
@app.command()
def test(name : str, age : int = 0):
    print(f"{name} {age}")

# typer.Option에서 ...은 필수 입력 옵션이라는 뜻(즉 반드시 --pw로 사용해야함을 의미), 기본값이 없음을 의미
@app.command()
def login(id : str, pw : str = typer.Option(...,prompt=True, hide_input=True)):


    if id in id_dict and pw == id_dict[id]:
        print("login completed")
    else:
        print("id and pw not matched")

@app.command()
def hello(name:str):
    #--help text
    """
    help text
    """
    print(f"hello {name}")

if __name__ == "__main__":
    app()