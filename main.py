import openai

# OpenAI API 키 설정
openai.api_key = 'KEY'

# ChatGPT에 대한 대화 시작
def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',  # ChatGPT 엔진 선택(2023년에 새롭게 출시된 모델)
        # prompt=prompt, (문법이 바뀌어서 아래와 같이 입력해야 함)
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.7,  # 0 ~ 2 사이, 낮은 값은 보수적인 응답, 높은 값은 더 다양한 응답을 생성합니다.
        max_tokens=100,  # 모델이 생성하는 최대 토큰 수
        n=1,  # 생성할 응답 수
        stop=None,  # 응답 중지 시퀀스
        timeout=None  # 요청 시간 초과 (옵션)
    )
    if response.choices:
        return response.choices[0].message.content
    return ''

# ChatGPT와 상호 작용
while True:
    user_input = input("사용자: ")
    prompt = f"사용자: {user_input}\nAI: "
    output = chat_with_gpt(prompt)
    print("AI:", output)