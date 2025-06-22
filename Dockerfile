# Pythonイメージをベースにする
FROM python:3.11

# 作業フォルダを作成
WORKDIR /app

# ファイルをコンテナにコピー
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .

# Flaskアプリを実行
CMD ["python", "app.py"]
