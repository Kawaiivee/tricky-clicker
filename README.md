# tricky-clicker
AI to classify yoyo tricks and score trick sequences
(Pivoted the project to make a neural network that "clicks" yoyo video perfomances. More like an AI judge)

# Install pyenv (Windows)
https://github.com/pyenv-win/pyenv-win
pyenv install 3.xx (3.12)

# Nav to python project directory
pyenv global 3.xx
pyenv local 3.xx

# Create Directory Structure
mkdir -p notebooks \
         src/video \
         src/pose \
         src/models \
         data/raw \
         data/processed \
         scripts

touch README.md requirements.in .gitignore
touch src/__init__.py
touch src/video/__init__.py
touch src/pose/__init__.py
touch src/models/__init__.py

# Create and activate the virtual environment
python -m venv .venv
source .venv/Scripts/activate

# Upgrade core tooling
pip install --upgrade pip setuptools wheel

# Add dependencies to requirements.in (cat runs all that)
cat > requirements.in << 'EOF'
jupyterlab
ipykernel

numpy
pandas
matplotlib

opencv-python
mediapipe

scikit-learn
tqdm
EOF

# Install dependencies
pip install pip-tools
pip-compile requirements.in
pip install -r requirements.txt

# Git hygiene (add to gitignore)
.venv/
__pycache__/
.ipynb_checkpoints/
data/raw/*
data/processed/*

# Pip install this package for cleaning up after jupyter (otherwise, git will check in a lot of menutia)
pip install nbstripout
nbstripout --install

# Verify it runs:
cd project-directory
source .venv/Scripts/activate
python --version
jupyter lab