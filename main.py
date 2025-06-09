import streamlit as st

# 📌 MBTI별 추천 영화 데이터
mbti_movies = {
    "INTJ": ["🎬 Interstellar", "🧠 A Beautiful Mind"],
    "INTP": ["🔍 The Imitation Game", "💡 Primer"],
    "ENTJ": ["🚀 The Martian", "📈 Moneyball"],
    "ENTP": ["🧪 Back to the Future", "🧬 Jurassic Park"],
    "INFJ": ["🌌 Contact", "🔮 Arrival"],
    "INFP": ["🎥 Donnie Darko", "🌱 The Man from Earth"],
    "ENFJ": ["🎓 Good Will Hunting", "🧬 Gattaca"],
    "ENFP": ["🌀 Cloud Atlas", "🔭 October Sky"],
    "ISTJ": ["📐 Hidden Figures", "💾 The Theory of Everything"],
    "ISFJ": ["🔬 Awakenings", "🧬 Lorenzo's Oil"],
    "ESTJ": ["🧮 Apollo 13", "📊 The Big Short"],
    "ESFJ": ["🧑‍🏫 Stand and Deliver", "🎓 Dead Poets Society"],
    "ISTP": ["🧲 Tenet", "🔍 Pi"],
    "ISFP": ["📸 The Secret Life of Walter Mitty", "💡 Koyaanisqatsi"],
    "ESTP": ["🎢 Limitless", "🌌 Gravity"],
    "ESFP": ["🎡 The Prestige", "🧠 Lucy"],
}

# 🎉 앱 타이틀
st.title("🎭 MBTI 맞춤 🎥 과학 & 수학 영화 추천기")
st.markdown("당신의 성격에 어울리는 명작 과학/수학 영화를 추천해드려요! 💡")

# 📋 MBTI 선택
mbti_options = list(mbti_movies.keys())
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요", [""] + mbti_options)

# 🎬 추천 결과
if selected_mbti:
    st.balloons()  # 🎈 풍선 효과
    st.success(f"🎉 {selected_mbti}에게 딱 어울리는 영화들입니다!")
    for movie in mbti_movies[selected_mbti]:
        st.markdown(f"- {movie}")
