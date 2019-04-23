# ベースイメージの指定
FROM python:3.6-alpine

ENV PYTHONUNBUFFERED 1

# ソースを置くディレクトリを変数として格納                                                                                                                  
ARG project_dir=/web/socket/

# apkでインストールできるパッケージの更新後にgitをインストール
RUN apk update
RUN apk add git
RUN apk add gcc
RUN apk add libc-dev

# requirements.txtに記載されたパッケージをインストール
WORKDIR $project_dir
ADD requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt



# GitHubのリポジトリからFlask-SocketIOのソースコードを取得
# RUN git clone https://github.com/miguelgrinberg/Flask-SocketIO.git Flask-SocketIO
# WORKDIR $project_dir/Flask-SocketIO/example