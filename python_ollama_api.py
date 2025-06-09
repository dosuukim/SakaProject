import requests
import json

# Ollama 서버 URL (기본값)
OLLAMA_URL = "http://localhost:11434/api/chat"

def chat_with_ollama(model_name, prompt):
    headers = {"Content-Type": "application/json"}
    data = {
        "model": model_name,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "stream": False # 스트리밍 응답을 받지 않음
    }

    try:
        response = requests.post(OLLAMA_URL, headers=headers, data=json.dumps(data))
        response.raise_for_status() # HTTP 오류 발생 시 예외 발생

        result = response.json()
        if "message" in result and "content" in result["message"]:
            return result["message"]["content"]
        else:
            return "응답에서 메시지 내용을 찾을 수 없습니다."

    except requests.exceptions.RequestException as e:
        return f"API 호출 중 오류 발생: {e}"

if __name__ == "__main__":
    model = "llama3" # 사용할 모델 이름
    user_prompt = "대한민국의 수도는 어디야?"
    print(f"질문: {user_prompt}")
    
    response_content = chat_with_ollama(model, user_prompt)
    print(f"응답: {response_content}")

    print("-" * 30)

    user_prompt_2 = "인공지능의 미래에 대해 간략하게 설명해줘."
    print(f"질문: {user_prompt_2}")
    response_content_2 = chat_with_ollama(model, user_prompt_2)
    print(f"응답: {response_content_2}")