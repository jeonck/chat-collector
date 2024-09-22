import streamlit as st
import json

def prompt_dialogue():
    def parse_text_to_json(input_text):
        lines = input_text.strip().split('\n')
        comments = []
        i = 0

        while i < len(lines):
            if i + 4 < len(lines):
                username = lines[i].strip()
                timestamp = lines[i + 1].strip()
                comment = lines[i + 2].strip()
                try:
                    replies = int(lines[i + 3].strip())
                except ValueError:
                    replies = 0  # If conversion fails, set replies to 0
                reply_indicator = lines[i + 4].strip()

                if reply_indicator.lower() == "reply":
                    comments.append({
                        "username": username,
                        "timestamp": timestamp,
                        "comment": comment,
                        "replies": replies
                    })
                    i += 6  # Move to the next block, skipping the blank line
                else:
                    i += 1
            else:
                break

        return comments

    st.title('🗨️ 감성 대화 수집기')
    """
    이 감성 대화 수집기는 melonn에서 대화한 데이터를 JSON 형식으로 수집할 수 있도록 도와줍니다.   
    "Convert to JSON" 버튼을 사용하여 입력된 대화를 JSON 형식으로 변환할 수 있고, JSON 파일로 다운로드도 가능합니다. 
    """

    sample_data = """_hazelll_
now
아침부터 개발이라니 대단하다! 어떤 툴 만들고 있어? 어렵진 않아?
0
Reply

silva__break
now
툴 개발은 어렵지! 언제나 너를 지지해! 이거 끝내고 나서 우리 다 같이 상대 회사 박살내자!
0
Reply
"""

    # 레이아웃 설정
    col1, col2 = st.columns([1, 1])

    with col1:
        convert_button = st.button("Convert to JSON")

    with col2:
        download_button_placeholder = st.empty()

    input_text = st.text_area("https://www.melonn.xyz/ 의 대화 데이터를 입력하세요.(대화 copy&paste)", sample_data, height=300)

    if convert_button:
        if input_text:
            try:
                comments = parse_text_to_json(input_text)
                json_output = json.dumps(comments, ensure_ascii=False, indent=4)
                st.json(json_output)
                download_button_placeholder.download_button(label="Download JSON", data=json_output, file_name="collect.json", mime="application/json")
            except Exception as e:
                st.error(f"An error occurred: {e}")
        else:
            st.warning("Please enter some text data.")

if __name__ == "__main__":
    prompt_dialogue()
