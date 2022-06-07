Previamente tener instalado:
    sudo apt install python3-pip
    sudo apt install python3-venv


Ejecutar los siguientes comandos:
    rm -rf .venv/
    python3 -m virtualenv .venv
    source .venv/bin/activate
    pip3 install -r requirements
    python run.py

<!-- pipenv --python `which python3` install -->

Para ejecutar las migraciones:
    flask db upgrade
