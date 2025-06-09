import requests
import json

# Ollama 서버 URL (기본값)
OLLAMA_GENERATE_URL = "http://localhost:11434/api/generate"

def generate_with_ollama(model_name, prompt):
    headers = {"Content-Type": "application/json"}
    data = {
        "model": model_name,
        "prompt": prompt,
        "stream": False # 스트리밍 응답을 받지 않음
    }

    try:
        response = requests.post(OLLAMA_GENERATE_URL, headers=headers, data=json.dumps(data))
        response.raise_for_status()

        result = response.json()
        if "response" in result:
            return result["response"]
        else:
            return "응답에서 내용을 찾을 수 없습니다."

    except requests.exceptions.RequestException as e:
        return f"API 호출 중 오류 발생: {e}"

# if __name__ == "__main__":
#     model = "llama2" 
#     user_prompt = "간단한 농담 하나 해줘."
#     print(f"질문: {user_prompt}")
    
#     response_content = generate_with_ollama(model, user_prompt)
#     print(f"응답: {response_content}")

if __name__ == "__main__":
    model = "llama2" 
    # user_prompt = "간단한 농담 하나 해줘."
    user_prompt = input("Ollama에 질문을 해보세요 : ")
    # print(f"질문: {user_prompt}")
    
    response_content = generate_with_ollama(model, user_prompt)
    print(f"응답: {response_content}")
