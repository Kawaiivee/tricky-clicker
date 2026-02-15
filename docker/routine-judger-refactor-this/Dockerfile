# Dockerfile
FROM python:3.12-slim

# Install system dependencies with CA certificates
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    git curl ca-certificates build-essential \
    libssl-dev zlib1g-dev libbz2-dev \
    libreadline-dev libsqlite3-dev \
    libncursesw5-dev xz-utils tk-dev \
    libxml2-dev libxmlsec1-dev libffi-dev && \
    update-ca-certificates --fresh

# Configure pyenv with SSL fix
RUN git clone https://github.com/pyenv/pyenv.git ~/.pyenv
ENV PYENV_ROOT="/root/.pyenv"
ENV PATH="$PYENV_ROOT/bin:$PATH"
ENV PYTHON_BUILD_CURL_OPTS="-k"
ENV PYTHON_BUILD_HTTP_CLIENT="curl"

# Install Python with retry logic
RUN pyenv install 3.9.12 || \
    (rm -rf /tmp/python-build* && pyenv install 3.9.12) && \
    pyenv global 3.9.12

# Install Python packages
RUN pip install --upgrade pip && \
    pip install jupyterlab numpy pandas matplotlib seaborn \
    scipy scikit-learn statsmodels notebook opencv-python

WORKDIR /home/jupyter
EXPOSE 9696
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token=password123"]