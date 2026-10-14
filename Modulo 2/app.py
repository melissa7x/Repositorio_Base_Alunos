from flask import Flask

app = Flask(__name__)


@app.route("/")
def inicio():
    return """
    <html>
    <head>
        <title>Meus Filmes</title>

        <style>
            body {
                background-color: black;
                color: white;
                font-family: Arial;
                text-align: center;
            }

            h1 {
                font-size: 40px;
                margin-top: 30px;
            }

            .filmes {
                display: flex;
                justify-content: center;
                gap: 25px;
                flex-wrap: wrap;
                margin-top: 30px;
            }

            .filme {
                background-color: #1c1c1c;
                padding: 15px;
                border-radius: 15px;
                width: 220px;
            }

            .filme img {
                width: 220px;
                height: 300px;
                object-fit: cover;
                border-radius: 10px;
            }

            .filme a {
                color: white;
                text-decoration: none;
            }

            .filme h2 {
                font-size: 20px;
            }
        </style>
    </head>

    <body>

        <h1>🎬 Meus Filmes</h1>

        <div class="filmes">

            <div class="filme">
                <a href="/homem-aranha">
                    <img src="/static/Homem_Aranha.png">
                    <h2>🕷️ Homem-Aranha</h2>
                </a>
            </div>

            <div class="filme">
                <a href="/dragao">
                    <img src="/static/Como_treinar_seu_dragão.png">
                    <h2>🐉 Como Treinar o Seu Dragão</h2>
                </a>
            </div>

            <div class="filme">
                <a href="/divertidamente">
                    <img src="/static/Divertida_Mente.png">
                    <h2>🧠 Divertida Mente</h2>
                </a>
            </div>

            <div class="filme">
                <a href="/vingadores">
                    <img src="/static/Vingadores.png">
                    <h2>🦸 Vingadores</h2>
                </a>
            </div>

        </div>

    </body>
    </html>
    """


@app.route("/homem-aranha")
def homem_aranha():
    return """
    <body style="background-color: black; color: white; text-align: center; font-family: Arial;">

        <h1>🕷️ Homem-Aranha</h1>

        <img src="/static/Homem_Aranha.png" width="300">

        <h2>Sobre o filme</h2>

        <p>
        Homem-Aranha é um filme de super-herói sobre Peter Parker,
        um jovem que ganha poderes especiais e decide usar seus
        poderes para ajudar as pessoas.
        </p>

    </body>
    """


@app.route("/dragao")
def dragao():
    return """
    <body style="background-color: black; color: white; text-align: center; font-family: Arial;">

        <h1>🐉 Como Treinar o Seu Dragão</h1>

        <img src="/static/Como_treinar_seu_dragão.png" width="300">

        <h2>Sobre o filme</h2>

        <p>
        Como Treinar o Seu Dragão conta a história de Soluço,
        um jovem viking que faz amizade com um dragão chamado Banguela.
        </p>

    </body>
    """


@app.route("/divertidamente")
def divertidamente():
    return """
    <body style="background-color: black; color: white; text-align: center; font-family: Arial;">

        <h1>🧠 Divertida Mente</h1>

        <img src="/static/Divertida_Mente.png" width="300">

        <h2>Sobre o filme</h2>

        <p>
        Divertida Mente conta a história de Riley e das emoções
        que vivem dentro da sua mente.
        </p>

    </body>
    """


@app.route("/vingadores")
def vingadores():
    return """
    <body style="background-color: black; color: white; text-align: center; font-family: Arial;">

        <h1>🦸 Vingadores</h1>

        <img src="/static/Vingadores.png" width="300">

        <h2>Sobre o filme</h2>

        <p>
        Vingadores reúne vários heróis que precisam trabalhar
        juntos para enfrentar uma grande ameaça e proteger o mundo.
        </p>

    </body>
    """


app.run(debug=True)
