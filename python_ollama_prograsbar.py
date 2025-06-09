import requests
import json
import sys
import time

# Ollama 서버 URL
OLLAMA_CHAT_URL = "http://localhost:11434/api/chat"

def get_streaming_response_with_progress(model_name, prompt):
    headers = {"Content-Type": "application/json"}
    data = {
        "model": model_name,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "stream": True # 스트리밍 응답 활성화
    }

    full_response_content = ""
    print(f"\n{model_name} 모델이 '{prompt}'에 대한 응답을 생성 중입니다...", end="", flush=True)

    try:
        # stream=True로 설정하여 응답을 스트리밍 방식으로 받음
        response = requests.post(OLLAMA_CHAT_URL, headers=headers, data=json.dumps(data), stream=True)
        response.raise_for_status()

        # 응답이 도착하는 동안 '.'을 출력하여 진행 상황을 표시
        for chunk in response.iter_content(chunk_size=None):
            if chunk:
                try:
                    # 각 청크는 여러 JSON 객체를 포함할 수 있음
                    for line in chunk.decode('utf-8').splitlines():
                        if line.strip():
                            json_data = json.loads(line)
                            if "message" in json_data and "content" in json_data["message"]:
                                content = json_data["message"]["content"]
                                full_response_content += content
                                # 응답이 도착할 때마다 '.' 출력 (너무 빠르면 생략 가능)
                                # print(".", end="", flush=True)
                                print(">", end="", flush=True)
                            elif "done" in json_data and json_data["done"]:
                                # 응답이 완료되면 루프 종료
                                break
                except json.JSONDecodeError:
                    # JSON 형식이 아닌 데이터는 무시
                    pass
        
        print("\n응답이 완료되었습니다.") # 진행 표시 후 완료 메시지

    except requests.exceptions.ConnectionError as e:
        print(f"\n[오류]: Ollama 서버에 연결할 수 없습니다. 서버가 실행 중인지 확인하세요. ({e})")
        return None
    except requests.exceptions.RequestException as e:
        print(f"\n[오류]: API 호출 중 오류 발생: {e}")
        return None
    
    return full_response_content

if __name__ == "__main__":
    model = "llama3" # 사용할 모델 이름
    # question = "서울의 랜드마크 3가지와 그 특징을 설명해줘."
    question = input("Ollama에 질문을 해보세요 : ")

    print(f"질문: {question}")
    
    response_text = get_streaming_response_with_progress(model, question)
    
    if response_text:
        print("---- 응답 내용 --->")
        print(response_text)
        print("<--- 응답 완료 ----")