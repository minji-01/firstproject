import streamlit as st

# MBTI 리스트
mbti_list = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

gender_list = ["남성", "여성"]

mbti_love = {
    "INTJ": {"남성": "🔍 계획형 INTJ! 당신은 '말보단 뇌파로 통하는 사람'에게 끌려요!",
             "여성": "🧠 분석 여왕 INTJ! 조용하고 지적인 사람에게 마음이 움직이죠!"},
    "INFP": {"남성": "🌸 감성 INFP! 마음을 따뜻하게 어루만져주는 사람에게 약해요~",
             "여성": "🧚‍♀️ 꿈 많은 INFP! 동화 같은 연애를 꿈꾸는 로맨티스트에요!"}
}

mbti_jobs = {
    "INTJ": "📊 전략가! 기획자, 데이터 분석가, 과학자 타입이에요.",
    "INFP": "✒️ 창작러! 작가, 디자이너, 상담가가 어울려요."
}

mbti_movies = {
    "INTJ": (
        "Interstellar",
        "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
        "https://www.youtube.com/watch?v=zSWdZVtXT7E"
    ),
    "INFP": (
        "The Secret Life of Walter Mitty",
        "https://upload.wikimedia.org/wikipedia/en/e/e7/The_Secret_Life_of_Walter_Mitty_2013_poster.jpg",
        "https://www.youtube.com/watch?v=QD6cy4PBQPI"
    )
}

mbti_travel = {
    "INTJ": "📚 빈 (오스트리아) - 고요하게 사색하기 딱 좋은 클래식 도시!",
    "INFP": "🌈 프라하 - 감성과 낭만이 흐르는 동화 같은 도시!"
}

mbti_books = {
    "INTJ": "🧠 『사피엔스』 - 냉철한 지적 탐험을 좋아하는 당신에게!",
    "INFP": "📖 『어린 왕자』 - 마음 깊은 곳을 건드리는 따뜻한 이야기!"
}

# 페이지 세팅
st.set_page_config(page_title="MBTI 성별 맞춤 큐레이션", layout="centered")
st.title("🧬 MBTI로 나의 취향 알아보기")

# MBTI 선택
selected_mbti = st.selectbox("👉 당신의 MBTI는?", [""] + mbti_list)

if selected_mbti:
    # 성별 선택
    selected_gender = st.radio("🚻 성별을 선택해주세요!", gender_list, horizontal=True)

    if selected_gender:
        st.balloons()
        st.markdown("### 😎 무엇이 궁금한가요?")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("💘 이상형"):
                if selected_mbti in mbti_love and selected_gender in mbti_love[selected_mbti]:
                    st.subheader("✨ 당신의 이상형 스타일은...")
                    st.info(mbti_love[selected_mbti][selected_gender])
                else:
                    st.warning("🙈 해당 MBTI의 성별 데이터가 아직 부족해요... 다음에 추가할게요!")

            if st.button("💼 어울리는 직업"):
                st.subheader("✨ 추천 직업은...")
                st.success(mbti_jobs.get(selected_mbti, "아직 데이터가 부족해요! 조금만 기다려줘요 🙏"))

            if st.button("📚 추천 도서"):
                st.subheader("✨ 이 책 어때요?")
                st.info(mbti_books.get(selected_mbti, "독서취향 분석 중이에요~ 기다려줘요! 📖"))

        with col2:
            if st.button("🎥 인생 영화"):
                movie = mbti_movies.get(selected_mbti)
                if movie:
                    title, img_url, trailer_url = movie
                    st.subheader(f"✨ {title}")
                    st.image(img_url, width=250, caption="🎬 당신에게 찰떡인 인생 영화!")
                    st.link_button("🎞️ 예고편 보러가기", trailer_url)
                else:
                    st.warning("🎥 영화 데이터가 준비 중이에요!")

            if st.button("✈️ 여행지 추천"):
                st.subheader("✨ 떠나볼까요?")
                st.warning(mbti_travel.get(selected_mbti, "지금 당신의 여행지 정렬 중이에요 ✈️"))
