### main.py 다국어 번역기 백엔드 코드

from flask import Flask, request, render_template
import openai

# OpenAI API 키 설정
openai.api_key = "KEY"

# Flask application 생성
app = Flask(__name__) 

@app.route("/translater", methods=["post"])
def translater():
    # 주고받는 데이터 형식을 json으로 지정
    data = request.json # 파싱된 json 데이터(request 객체에는 요청한 데이터를 파싱한 값이 들어있음)
    
    language = data["language"] # ai가 번역한 글
    text = data["inputText"] # 사용자가 입력한 text

    prompt = f"{text}\n\nTranslate this sentence into {language}"

    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',  # ChatGPT 엔진 선택
        messages=[
            {
                "role": "system",
                "content": "You are a translater"
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=1.5,  # 0 ~ 2 사이(디폴트:1), 낮은 값은 보수적인 응답, 높은 값은 더 다양한 응답을 생성합니다.
        max_tokens=100,  # 모델이 생성하는 최대 토큰 수
        # n=1,  # 생성할 응답 수(디폴트:1)
        stop=None,  # 응답 중지 시퀀스
        timeout=None  # 요청 시간 초과 (옵션)
    )
    return response["choices"][0]["message"]["content"]
    # if response.choices:
    #     return response.choices[0].text.strip()

@app.route("/web")
def web():
    return render_template("index.html") # templates 아래의 index.html 파일 리턴함

app.run() # host, port 직접 지정도 가능 host="0.0.0.0", port=80