# 使用python映像
FROM python:3.10-slim


# 設置工作目錄
WORKDIR /app


# 複製 requirements.txt 並安裝依賴
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt


# 複製當前目錄下的所有文件到容器的工作目錄
COPY . /app


# 定義容器啟動時執行的指令
CMD ["python", "app.py"]