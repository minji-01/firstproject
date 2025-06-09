import streamlit as st

# MBTI 리스트
mbti_list = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

gender_list = ["남성", "여성"]

# Create structured data for all MBTI types

mbti_data = {
    "INTJ": {
        "love": {
            "남성": "🧠 똑똑한 INTJ! 논리적인 대화로 두근거림을 느끼는 타입이에요!",
            "여성": "🎯 계획력 만렙 INTJ! 조용히 챙겨주는 지적인 사람이 좋아요~"
        },
        "job": "📊 전략가형! 기획자, 데이터 분석가, 과학자 스타일!",
        "movie": {
            "title": "Interstellar",
            "poster": "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
            "trailer": "https://www.youtube.com/watch?v=zSWdZVtXT7E"
        },
        "travel": "🇦🇹 빈 - 클래식 음악과 고요한 풍경, 사색을 즐기기에 완벽해요!",
        "book": "『사피엔스』 - 역사와 인간을 파헤치는 깊이 있는 책이에요."
    },
    "INTP": {
        "love": {
            "남성": "🔍 호기심 많은 INTP! 엉뚱한 농담에 잘 웃어주는 사람이 딱!",
            "여성": "🧪 실험정신 강한 INTP! 내 세계를 존중해주는 사람에게 끌려요!"
        },
        "job": "💡 발명가형! 개발자, 이론물리학자, 철학자 스타일!",
        "movie": {
            "title": "The Imitation Game",
            "poster": "https://upload.wikimedia.org/wikipedia/en/5/5e/The_Imitation_Game_poster.jpg",
            "trailer": "https://www.youtube.com/watch?v=S5CjKEFb-sM"
        },
        "travel": "🇯🇵 교토 - 전통과 현대가 어우러진 도시에 마음이 편해져요.",
        "book": "『이기적 유전자』 - 논리적이고 과학적인 당신에게 찰떡!"
    },
    "ENTJ": {
        "love": {
            "남성": "📈 리더 ENTJ! 야망 있고 똑부러지는 사람에게 매력을 느껴요!",
            "여성": "🔥 추진력 만렙 ENTJ! 목표를 향해 같이 달려갈 사람을 좋아해요!"
        },
        "job": "🏢 CEO형! 관리자, 변호사, 기업 전략가에 잘 어울려요.",
        "movie": {
            "title": "Steve Jobs",
            "poster": "https://upload.wikimedia.org/wikipedia/en/b/b9/Steve_Jobs_film_poster.jpg",
            "trailer": "https://www.youtube.com/watch?v=aEr6K1bwIVs"
        },
        "travel": "🇺🇸 뉴욕 - 역동적인 도시에서 에너지 뿜뿜!",
        "book": "『그릿』 - 끝까지 해내는 열정과 끈기에 대해 배우는 책!"
    },
    "ENTP": {
        "love": {
            "남성": "🎤 토론가 ENTP! 아이디어를 자유롭게 나눌 수 있는 사람에게 끌려요!",
            "여성": "🎈 장난기 많은 ENTP! 지루할 틈이 없는 대화 상대를 좋아해요!"
        },
        "job": "🚀 혁신가형! 스타트업 창업자, 크리에이티브 디렉터!",
        "movie": {
            "title": "Catch Me If You Can",
            "poster": "https://upload.wikimedia.org/wikipedia/en/4/4d/Catch_Me_If_You_Can_2002_movie.jpg",
            "trailer": "https://www.youtube.com/watch?v=s-7pyIxz8Qg"
        },
        "travel": "🇪🇸 바르셀로나 - 자유로운 예술과 즉흥 여행이 잘 어울려요.",
        "book": "『넛지』 - 창의적인 발상으로 세상을 보는 법을 알려줘요."
    },

    "INFJ": {
        "love": {
            "남성": "🧘‍♂️ 조용하지만 깊은 INFJ! 나만의 진심을 알아봐주는 사람에게 약해요.",
            "여성": "🌌 이상주의자 INFJ! 말없이 함께 있어도 마음이 통하는 사람을 원해요."
        },
        "job": "🌱 조력자형! 심리상담가, 작가, 인권운동가에 잘 어울려요.",
        "movie": {
            "title": "A Beautiful Mind",
            "poster": "https://upload.wikimedia.org/wikipedia/en/b/b8/A_Beautiful_Mind_Poster.jpg",
            "trailer": "https://www.youtube.com/watch?v=aS_d0Ayjw4o"
        },
        "travel": "🇨🇿 프라하 - 고요한 분위기와 감성적인 거리가 잘 어울려요.",
        "book": "『데미안』 - 자아를 찾아가는 여정이 당신과 닮았어요."
    },
    "INFP": {
        "love": {
            "남성": "🌷 감성 INFP! 따뜻하고 배려심 깊은 사람에게 끌려요~",
            "여성": "🧚‍♀️ 몽환적인 INFP! 공감력 넘치는 연인을 꿈꿔요!"
        },
        "job": "🎨 예술가형! 작가, 일러스트레이터, 심리상담가가 잘 맞아요.",
        "movie": {
            "title": "The Secret Life of Walter Mitty",
            "poster": "https://upload.wikimedia.org/wikipedia/en/e/e7/The_Secret_Life_of_Walter_Mitty_2013_poster.jpg",
            "trailer": "https://www.youtube.com/watch?v=QD6cy4PBQPI"
        },
        "travel": "🇮🇸 아이슬란드 - 꿈같은 풍경 속에서 내면의 평화를 찾아요.",
        "book": "『어린 왕자』 - 마음속 깊은 이야기를 함께 나눠요."
    },
    "ENFJ": {
        "love": {
            "남성": "🌟 카리스마 ENFJ! 진심을 알아주고 응원해주는 사람이 좋아요!",
            "여성": "💖 사교 여왕 ENFJ! 감정을 잘 나눌 수 있는 사람에게 끌려요!"
        },
        "job": "🎤 지도자형! 교사, 리더, 커뮤니케이터 스타일!",
        "movie": {
            "title": "Dead Poets Society",
            "poster": "https://upload.wikimedia.org/wikipedia/en/4/49/Dead_Poets_Society.jpg",
            "trailer": "https://www.youtube.com/watch?v=WrO9PTpuSSs"
        },
        "travel": "🇫🇷 파리 - 낭만과 영감을 주는 도시에서 인생샷 찰칵!",
        "book": "『모든 순간이 너였다』 - 마음을 따뜻하게 해주는 글귀들!"
    },
    "ENFP": {
        "love": {
            "남성": "🎉 자유로운 ENFP! 함께 놀고 웃을 수 있는 사람이 좋아요!",
            "여성": "🌈 감성 폭발 ENFP! 나의 꿈을 응원해주는 사람이 찐이에요!"
        },
        "job": "🎭 아이디어 뱅크! 콘텐츠 기획자, 마케터, 상담가가 잘 어울려요.",
        "movie": {
            "title": "The Truman Show",
            "poster": "https://upload.wikimedia.org/wikipedia/en/2/22/Truman_Show_Poster.jpg",
            "trailer": "https://www.youtube.com/watch?v=dlnmQbPGuls"
        },
        "travel": "🇮🇹 피렌체 - 예술과 낭만이 살아 숨 쉬는 골목 여행!",
        "book": "『미움받을 용기』 - 자유롭고 진정한 나를 위한 철학서!"
    }

    "ISTJ": {
        "love": {
            "남성": "🛡️ 신중한 ISTJ! 믿음직하고 성실한 사람에게 끌려요.",
            "여성": "📋 계획파 ISTJ! 신뢰감 있고 약속을 잘 지키는 사람에게 약해요!"
        },
        "job": "🏛️ 관리자형! 회계사, 공무원, 군인에 잘 어울려요.",
        "movie": {
            "title": "The King's Speech",
            "poster": "https://upload.wikimedia.org/wikipedia/en/0/0e/The_Kings_Speech_poster.jpg",
            "trailer": "https://www.youtube.com/watch?v=pzI4D6dyp_o"
        },
        "travel": "🇩🇪 베를린 - 질서 있고 효율적인 도시 여행이 딱!",
        "book": "『7가지 성공 습관』 - 현실적이고 실용적인 책 좋아하죠!"
    },
    "ISFJ": {
        "love": {
            "남성": "🍵 다정한 ISFJ! 배려심 넘치고 자상한 사람에게 설레요.",
            "여성": "🧺 챙겨주는 ISFJ! 말없이 도와주는 사람에게 끌려요~"
        },
        "job": "👩‍⚕️ 수호자형! 간호사, 교사, 행정직에 잘 어울려요.",
        "movie": {
            "title": "The Help",
            "poster": "https://upload.wikimedia.org/wikipedia/en/0/00/The_Help_Poster.jpg",
            "trailer": "https://www.youtube.com/watch?v=WbuKgzgeUIU"
        },
        "travel": "🇳🇱 암스테르담 - 따뜻한 분위기와 평화로운 풍경이 좋아요.",
        "book": "『책 먹는 여우』 - 정 많고 귀여운 감성의 당신에게!"
    },
    "ESTJ": {
        "love": {
            "남성": "🏗️ 현실주의 ESTJ! 똑부러지고 목표가 분명한 사람에게 끌려요!",
            "여성": "🗂️ 책임감 강한 ESTJ! 신뢰감 있게 이끄는 사람이 좋아요!"
        },
        "job": "📈 경영자형! 관리자, 판사, 군 간부 등 리더 직군에 어울려요.",
        "movie": {
            "title": "Moneyball",
            "poster": "https://upload.wikimedia.org/wikipedia/en/2/2e/Moneyball_Poster.jpg",
            "trailer": "https://www.youtube.com/watch?v=-4QPVo0UIzc"
        },
        "travel": "🇸🇬 싱가포르 - 깔끔하고 정돈된 도시가 잘 맞아요.",
        "book": "『원씽』 - 집중과 효율을 중시하는 당신을 위한 책!"
    },
    "ESFJ": {
        "love": {
            "남성": "🎀 친절한 ESFJ! 감정을 표현해주고 잘 챙겨주는 사람이 좋아요.",
            "여성": "🍰 정 많은 ESFJ! 다정한 말투와 애정표현에 심쿵!"
        },
        "job": "🎓 협력자형! 상담가, 교사, 간호사에 찰떡이에요.",
        "movie": {
            "title": "The Intern",
            "poster": "https://upload.wikimedia.org/wikipedia/en/b/b9/The_Intern_Poster.jpg",
            "trailer": "https://www.youtube.com/watch?v=ZU3Xban0Y6A"
        },
        "travel": "🇦🇺 시드니 - 활기차고 친절한 분위기의 도시가 어울려요!",
        "book": "『엄마를 부탁해』 - 가족애 넘치는 이야기 좋아하죠?"
    },
    "ISTP": {
        "love": {
            "남성": "🔧 기술자 ISTP! 쿨하고 자유로운 사람에게 매력을 느껴요!",
            "여성": "🛠️ 관찰자 ISTP! 집착 없이 서로를 존중하는 사람이 좋아요!"
        },
        "job": "🕹️ 장인형! 엔지니어, 정비사, 파일럿에 딱 어울려요.",
        "movie": {
            "title": "Ford v Ferrari",
            "poster": "https://upload.wikimedia.org/wikipedia/en/5/5f/Ford_v_Ferrari_poster.jpg",
            "trailer": "https://www.youtube.com/watch?v=zyYgDtY2AMY"
        },
        "travel": "🇳🇿 뉴질랜드 - 대자연 속에서의 모험 여행 좋아하죠!",
        "book": "『셜록 홈즈 전집』 - 분석적이고 논리적인 이야기 취향!"
    },
    "ISFP": {
        "love": {
            "남성": "🍃 감성 ISFP! 말보다 행동으로 표현해주는 사람에게 끌려요.",
            "여성": "🎨 예술혼 ISFP! 섬세하고 부드러운 사람에게 심쿵!"
        },
        "job": "🧵 예술가형! 플로리스트, 포토그래퍼, 일러스트레이터에 적합해요.",
        "movie": {
            "title": "Her",
            "poster": "https://upload.wikimedia.org/wikipedia/en/4/44/Her2013Poster.jpg",
            "trailer": "https://www.youtube.com/watch?v=WzV6mXIOVl4"
        },
        "travel": "🇬🇷 산토리니 - 예쁜 풍경과 감성 넘치는 골목이 어울려요.",
        "book": "『연을 쫓는 아이』 - 마음을 울리는 감성 서사에 약한 당신에게!"
    },
    "ESTP": {
        "love": {
            "남성": "🏄 활발한 ESTP! 모험심 강하고 유쾌한 사람에게 끌려요!",
            "여성": "🎢 에너지 폭발 ESTP! 같이 놀고 웃을 수 있는 사람이 찐이에요!"
        },
        "job": "🚓 활동가형! 소방관, 스포츠 선수, 세일즈 전문가에 적합!",
        "movie": {
            "title": "The Dark Knight",
            "poster": "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
            "trailer": "https://www.youtube.com/watch?v=EXeTwQWrcwY"
        },
        "travel": "🇧🇷 리우데자네이루 - 활기찬 페스티벌과 뜨거운 에너지!",
        "book": "『파워 오브 해빗』 - 실용적이고 즉각 적용 가능한 책 좋아하죠!"
    },
    "ESFP": {
        "love": {
            "남성": "🎉 파티왕 ESFP! 즐겁고 분위기 띄우는 사람에게 끌려요!",
            "여성": "💃 무대 체질 ESFP! 애정 표현 잘하고 리액션 좋은 사람이 찐이에요!"
        },
        "job": "🎬 연예인형! 배우, 가수, 이벤트 플래너 스타일!",
        "movie": {
            "title": "La La Land",
            "poster": "https://upload.wikimedia.org/wikipedia/en/a/ab/La_La_Land_%28film%29.png",
            "trailer": "https://www.youtube.com/watch?v=0pdqf4P9MB8"
        },
        "travel": "🇹🇭 방콕 - 먹고 즐기고 쇼핑까지! 딱 당신 스타일!",
        "book": "『미생』 - 현실적인 공감과 감동이 있는 이야기 좋아해요!"
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
