from flask import Flask, jsonify, render_template, request
from openai import OpenAI
from config import config

app = Flask(__name__)


## 在此處替換為你的 OpenAI API Key
client = OpenAI(api_key=config['openai'])




# 首頁路由
@app.route('/')
def home():
    return render_template('home.html')


# 關於頁面路由
@app.route('/about')
def about():
    return render_template('about.html')




# 回傳錯誤頁面
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


# 關於頁面路由
@app.route('/chat_window')
def chat_window():
    return render_template('chat_window.html')






# 新增一個 /send_message 路由，用於處理 AJAX 請求
@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.json
    user_message = data.get('message')
    print(f"Received message: {user_message}")


    # 呼叫 OpenAI API 生成回應
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # 或 "gpt-4" 根據你的 API 訂閱情況
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message}
            ]
        )
        bot_response = response.choices[0].message.content
    except Exception as e:
        print(f"Error communicating with OpenAI API: {e}")
        bot_response = "抱歉，我無法處理您的請求。請稍後再試。"


    return jsonify({'response': bot_response})


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)

