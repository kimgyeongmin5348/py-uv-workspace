
import streamlit as st

# MBTI Quiz: 스트림릿 앱 (5문제씩 순차 진행)
st.set_page_config(page_title="MBTI 테스트", layout="centered")
st.title("🔮 간단한 MBTI 테스트")
st.write("각 문항에 대해 자신과 얼마나 일치하는지 선택한 후 '다음'을 눌러주세요.")

# MBTI 질문 리스트: (질문, 해당 지표, 동의할 때 가산점을 얻는 유형)
# 5척도 점수 계산용: "매우 비동의"(1점) ~ "매우 동의"(5점)
# 동의(4, 5점) 시 해당 유형(예: E)에 점수 부여, 비동의(1, 2점) 시 반대 유형(예: I)에 점수 부여
questions = [
    # 1. E vs I (외향 vs 내향)
    ("모르는 사람들과 대화를 시작하는 것이 어렵지 않다.", "EI", "E"),
    ("주목받는 것을 즐기며 사람들 앞에 서는 것을 좋아하는 편이다.", "EI", "E"),
    ("주말에는 집에 있기보다 밖에서 사람들을 만나며 에너지를 얻는다.", "EI", "E"),
    ("말하기 전에 생각하기보다, 말하면서 생각을 정리하는 편이다.", "EI", "E"),
    ("모임이나 파티 등 활기찬 분위기에서 살아있음을 느낀다.", "EI", "E"),

    # 2. S vs N (감각 vs 직관)
    ("상상이나 이론적인 아이디어보다는 현실적인 실현 가능성이 더 중요하다.", "SN", "S"),
    ("구체적이고 명확한 사실과 경험을 바탕으로 판단하는 편이다.", "SN", "S"),
    ("비유적이거나 함축적인 표현보다 직설적이고 단순 명료한 표현이 좋다.", "SN", "S"),
    ("미래의 계획이나 가능성보다는 현재 직면한 세부 사항에 집중한다.", "SN", "S"),
    ("새롭고 독창적인 방법보다는 기존에 검증된 일 처리 방식을 선호한다.", "SN", "S"),

    # 3. T vs F (사고 vs 감정)
    ("타인의 감정에 깊이 공감하기보다, 논리적인 해결책을 제시하는 편이다.", "TF", "T"),
    ("토론이나 논쟁이 발생했을 때, 상대방의 기분보다 진실(사실) 규명이 더 중요하다.", "TF", "T"),
    ("결정을 내릴 때 감정적인 요소는 배제하고 객관적인 원칙을 우선시한다.", "TF", "T"),
    ("감정 기복이 적고, 상황을 냉정하고 이성적으로 판단한다는 말을 자주 듣는다.", "TF", "T"),
    ("친구의 힘든 고민을 들으면 슬픔을 나누기보다 '왜 그런 일이 생겼는지' 원인을 찾고 싶다.", "TF", "T"),

    # 4. J vs P (판단 vs 인식)
    ("여행을 갈 때 시간대별로 세부적인 계획과 일정을 미리 짜두는 편이다.", "JP", "J"),
    ("주변 환경(방, 책상 등)이 항상 체계적으로 정리되어 있어야 마음이 편하다.", "JP", "J"),
    ("예기치 못한 돌발 상황이 발생하면 스트레스를 크게 받는 편이다.", "JP", "J"),
    ("일이나 과제를 할 때 마감일에 임박해서 하기보다 미리 계획을 세워 끝낸다.", "JP", "J"),
    ("목표를 명확히 정해두고 계획대로 차근차근 실행하는 것을 좋아한다.", "JP", "J"),
]

block_size = 5
options = {
    1: "매우 비동의",
    2: "비동의",
    3: "보통 (중립)",
    4: "동의",
    5: "매우 동의"
}

# 퀴즈 초기화 함수
def reset_quiz():
    st.session_state.current_idx = 0
    st.session_state.scores = {k: 0 for k in ["E", "I", "S", "N", "T", "F", "J", "P"]}

# 세션 상태 초기화
if "scores" not in st.session_state or "current_idx" not in st.session_state:
    reset_quiz()

start = st.session_state.current_idx
end = min(start + block_size, len(questions))

# 진행 상황 표시 바
progress = start / len(questions)
st.progress(progress)
st.write(f"진행도: {start} / {len(questions)} 문항 완료")

# 블록별 질문 표시
if start < len(questions):
    # Form을 활용해 한 페이지에 5개씩 렌더링
    with st.form(key=f"form_{start}"):
        for i in range(start, end):
            q_text, _, _ = questions[i]
            st.write(f"**Q{i+1}. {q_text}**")
            # 라디오 버튼 가로 정렬을 위해 horizontal=True 사용
            st.radio(
                label=f"Q{i+1} 선택",
                options=list(options.keys()),
                format_func=lambda x: options[x],
                index=2,  # 기본값: 보통 (중립)
                key=f"choice_{i}",
                label_visibility="collapsed"
            )
            st.markdown("---")

        submit = st.form_submit_button("다음 단계로")

        if submit:
            # 점수 계산 루프
            for i in range(start, end):
                score = st.session_state.get(f"choice_{i}", 3)
                _, dimension, target_type = questions[i]

                # 반대 유형 정의
                opposing_type = dimension.replace(target_type, "")

                # 척도에 따른 점수 부여 (3점 기준)
                if score > 3:  # 동의 경향 (4, 5점)
                    st.session_state.scores[target_type] += (score - 3)
                elif score < 3:  # 비동의 경향 (1, 2점)
                    st.session_state.scores[opposing_type] += (3 - score)
                # 3점(보통)일 때는 양쪽에 점수를 가산하지 않음

            # 다음 블록으로 이동 후 리런
            st.session_state.current_idx += block_size
            st.rerun()

# 모든 질문 완료 후 결과 표시
else:
    sc = st.session_state.scores

    # 각 지표별 점수 비교로 MBTI 도출 (동점일 경우 앞 글자 디폴트)
    mbti = (
        "E" if sc["E"] >= sc["I"] else "I"
    ) + (
        "S" if sc["S"] >= sc["N"] else "N"
    ) + (
        "T" if sc["T"] >= sc["F"] else "F"
    ) + (
        "J" if sc["J"] >= sc["P"] else "P"
    )

    st.subheader("🧩 분석 결과")
    st.markdown(f"당신의 MBTI 유형은 단연 **{mbti}** 입니다!")

    descriptions = {
        "ISTJ": "논리적이고 신중한 관리자 유형. 사실에 입각해 철저하게 일 처리를 해냅니다.",
        "ISFJ": "책임감 있고 세심한 수호자 유형. 소중한 사람들을 지키고 헌신하는 조력자입니다.",
        "INFJ": "통찰력 있고 창의적인 이상주의자 유형. 깊이 있는 생각과 강한 신념을 지닙니다.",
        "INTJ": "전략적이고 독립적인 설계자 유형. 모든 일에 논리적인 계획을 세우는 전략가입니다.",
        "ISTP": "유연하고 분석적인 해결사 유형. 도구와 상황을 다루는 데 능숙한 실천가입니다.",
        "ISFP": "따뜻하고 예술적인 탐험가 유형. 현재를 즐기며 감수성이 풍부하고 온화합니다.",
        "INFP": "이상주의적이고 충실한 중재자 유형. 신념과 자신만의 가치관을 깊이 소중히 여깁니다.",
        "INTP": "호기심 많고 논리적인 사색가 유형. 지적 탐구와 문제 해결에 늘 목말라 있습니다.",
        "ESTP": "에너지 넘치고 현실적인 활동가 유형. 행동력이 강하며 스릴과 도전을 즐깁니다.",
        "ESFP": "친근하고 낙천적인 연예인 유형. 삶을 즐길 줄 알고 주변을 유쾌하게 만듭니다.",
        "ENFP": "열정적이고 창의적인 활동가 유형. 무한한 긍정 에너지로 새로운 가능성을 찾습니다.",
        "ENTP": "영리하고 독창적인 발명가 유형. 고정관념에 도전하고 열띤 지적 토론을 좋아합니다.",
        "ESTJ": "현실적이고 조직적인 지도자 유형. 체계를 세우고 사람들을 확실하게 이끕니다.",
        "ESFJ": "친절하고 협력적인 제공자 유형. 관계를 소중히 여기며 타인에게 배려가 넘칩니다.",
        "ENFJ": "이해심 많고 카리스마 있는 리더 유형. 타인의 성장을 돕고 이끌어주는 등불 같은 존재입니다.",
        "ENTJ": "결단력 있고 대담한 지휘관 유형. 목표 달성을 위해 확고한 비전과 카리스마로 돌파합니다."
    }

    st.info(descriptions.get(mbti, "유형 설명이 없습니다."))

    # 스코어 세부 시각화
    with st.expander("나의 상세 지표 확인하기"):
        st.write(f"**외향성(E) {sc['E']}점** vs **내향성(I) {sc['I']}점**")
        st.write(f"**감각(S) {sc['S']}점** vs **직관(N) {sc['N']}점**")
        st.write(f"**사고(T) {sc['T']}점** vs **감정(F) {sc['F']}점**")
        st.write(f"**판단(J) {sc['J']}점** vs **인식(P) {sc['P']}점**")

    if st.button("다시 테스트하기"):
        reset_quiz()
        st.rerun()
