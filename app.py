import random
import streamlit as st

# 1. 웹앱 기본 설정 및 상단 제목, 안내 문구
st.set_page_config(page_title="가위바위보 게임", page_icon="🎮")

st.title("🎮 컴퓨터와 대결하는 가위바위보 게임")
st.write(
    "아래 세 가지 버튼 중 하나를 눌러 컴퓨터와 승부를 겨뤄보세요! 행운을 빕니다."
)
st.divider()

# 선택지 목록 및 사용자 선택 초기화
choices = ["✌️ 가위", "✊ 바위", "✋ 보"]
user_choice = None

# 2. 버튼 3개를 가로로 나란히 배치
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("✌️ 가위", use_container_width=True):
        user_choice = "✌️ 가위"

with col2:
    if st.button("✊ 바위", use_container_width=True):
        user_choice = "✊ 바위"

with col3:
    if st.button("✋ 보", use_container_width=True):
        user_choice = "✋ 보"

# 3. 사용자가 버튼을 눌렀을 때 컴퓨터 선택 및 승패 판정
if user_choice is not None:
    computer_choice = random.choice(choices)

    st.subheader("결과 확인")
    view_col1, view_col2 = st.columns(2)
    view_col1.info(f"**나의 선택:** {user_choice}")
    view_col2.info(f"**컴퓨터의 선택:** {computer_choice}")

    # 4. 승/패/무승부에 따른 결과 메시지 및 축하 효과 출력
    if user_choice == computer_choice:
        st.warning("🤝 **무승부입니다!** 마음이 통했네요. 다시 한 번 도전해 보세요!")
    elif (
        (user_choice == "✌️ 가위" and computer_choice == "✋ 보")
        or (user_choice == "✊ 바위" and computer_choice == "✌️ 가위")
        or (user_choice == "✋ 보" and computer_choice == "✊ 바위")
    ):
        st.success("🎉 **축하합니다! 승리하셨습니다!**")
        st.balloons()
    else:
        st.error("😭 **아쉽지만 패배했습니다...** 다시 도전해 보세요!")
