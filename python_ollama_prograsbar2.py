import requests
import json
import time
import sys
from tqdm import tqdm # pip install tqdm

# Ollama 서버 URL
OLLAMA_CHAT_URL = "http://localhost:11434/api/chat"

def get_streaming_response_with_tqdm_progress(model_name, prompt):
    headers = {"Content-Type": "application/json"}
    data = {
        "model": model_name,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "stream": True
    }

    full_response_content = ""
    # print(f"\n{model_name} 모델이 '{prompt}'에 대한 응답을 생성 중입니다:")
    print(f"\n{model_name}가 응답을 생성 중입니다:")

    try:
        response = requests.post(OLLAMA_CHAT_URL, headers=headers, data=json.dumps(data), stream=True)
        response.raise_for_status()

        # tqdm을 이용하여 무한 진행 바 표시 (실제 진행률은 알 수 없음)
        # 응답 청크가 올 때마다 tqdm을 업데이트
        with tqdm(unit=" chunk", desc="Generating response") as pbar:
            for chunk in response.iter_content(chunk_size=None):
                if chunk:
                    try:
                        for line in chunk.decode('utf-8').splitlines():
                            if line.strip():
                                json_data = json.loads(line)
                                if "message" in json_data and "content" in json_data["message"]:
                                    full_response_content += json_data["message"]["content"]
                                    pbar.update(1) # 청크가 올 때마다 진행 바 업데이트
                                elif "done" in json_data and json_data["done"]:
                                    break
                    except json.JSONDecodeError:
                        pass
        
        print("\n응답이 완료되었습니다.")

    except requests.exceptions.ConnectionError as e:
        print(f"\n[오류]: Ollama 서버에 연결할 수 없습니다. 서버가 실행 중인지 확인하세요. ({e})")
        return None
    except requests.exceptions.RequestException as e:
        print(f"\n[오류]: API 호출 중 오류 발생: {e}")
        return None
    
    return full_response_content

if __name__ == "__main__":
    model = "llama3"
    # question = "인공지능이 우리 삶에 미칠 영향에 대해 자세히 설명해줘."
    question = input("Ollama에 질문을 해보세요 : ")

    # print(f"질문: {question}")
    
    response_text = get_streaming_response_with_tqdm_progress(model, question)
    
    if response_text:
        print("---- 응답 내용 --->")
        print(response_text)
        print("<--- 응답 완료 ----")