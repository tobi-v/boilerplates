apt install -y build-essential curl libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev libffi-dev libncursesw5-dev liblzma-dev python3-tk


curl https://pyenv.run | bash
export PATH="$HOME/.pyenv:$PATH"

pyenv install 3.12.13
pyenv shell 3.12.13

python -m venv venv
source venv/bin/activate

pip install -r requirements.txt