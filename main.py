import openai
import config
import typer
from rich import print
from rich.table import Table

def main():

    openai.api_key = config.api_key

    print("[bold green]ChatGPT API en Python[/bold green]")

    table = Table("Comando", "Descripcion")
    table.add_row("exit", "Salir de la aplicacion")
    table.add_row("new", "Crear una nueva Conversación")

    print(table)

    #contexto del asistente
    context = {"role": "system",
                "content": '''Eres un asistente de programación Full Stack. 
                            y entre tu base de conocimiento debes considerar la programacion de videojuegos
                            a nivel de codigo en python'''}
    messages = [context]

    while True:
        content = __prompt()

        if content == "new":
            print("¡Nueva Conversacion Creada!")
            messages = [context]
            content = __prompt()

        messages.append({"role": "user", "content": content})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages = messages)

        response_content = response.choices[0].message.content
        
        messages.append({"role": "assistant", "content": response_content})

        print(f"[bold green]> [/bold green][green]{response_content}[/green]")

def __prompt() -> str:
    prompt = typer.prompt("\nHola, como puedo ayudarte el día de hoy? ")

    if prompt == "exit":
        exit = typer.confirm("¿Estas seguro?")
        if exit:
            print("¡Hasta Luego!")
            raise typer.Abort()
        
        return __prompt()

    return prompt

if __name__ == "__main__":
    typer.run(main)