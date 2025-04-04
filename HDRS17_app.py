# 설치 안내
# pip install streamlit

import streamlit as st

# 문항 및 선택지 데이터 정의
questions_ko = [
    "1. 우울한 기분 (슬픔, 절망감, 무력감, 무가치감)",
    "2. 죄책감",
    "3. 자살",
    "4. 초기 불면증",
    "5. 중기 불면증",
    "6. 말기 불면증",
    "7. 일과 활동",
    "8. 지체",
    "9. 초조",
    "10. 정신적 불안",
    "11. 신체적 불안",
    "12. 위장관계 신체증상",
    "13. 전반적인 신체증상",
    "14. 성적인 증상",
    "15. 건강염려증",
    "16. 체중감소",
    "17. 병식"
]

questions_en = [
    "Depressed mood",
    "Feelings of guilt",
    "Suicide",
    "Early insomnia",
    "Middle insomnia",
    "Late insomnia",
    "Work and activities",
    "Psychomotor retardation",
    "Psychomotor agitation",
    "Psychological anxiety",
    "Somatic anxiety",
    "Gastrointestinal symptoms",
    "General somatic symptoms",
    "Genital symptoms",
    "Hypochondriasis",
    "Weight loss",
    "Insight"
]

answers_ko = [
    ["없다", "물어보았을 때만 우울한 기분이라고 말한다", "자발적으로 우울한 기분이라고 말한다", "비언어적 표현으로 우울한 기분을 나타낸다", "언어적, 비언어적으로 우울한 기분만 나타낸다"],
    ["없다", "자책하거나 자신이 사람들을 실망시켰다고 느낀다", "죄를 지었다고 생각하거나 반복적으로 생각한다", "현재 병을 벌로 여김. 죄책망상 있음", "비난/탄핵 목소리나 위협적 환시 경험"],
    ["없다", "인생이 살 가치 없다고 느낌", "죽었으면 하거나 죽음 상상", "자살 사고나 시도 행동 있음", "심각한 자살 시도"],
    ["어려움 없음", "간간이 잠들기 어려움 (30분 이상)", "매일 밤 잠들기 어려움"],
    ["어려움 없음", "편하게 자지 못함", "한밤중에 깨거나 뒤척임 (소변 제외)"],
    ["어려움 없음", "새벽에 깨지만 다시 잠", "깨고 나면 다시 잠들지 못함"],
    ["어려움 없음", "활동에 피로/무기력 느낌", "흥미 상실 (직접 보고 또는 간접 표현)", "활동 시간 감소 또는 생산성 저하", "일 중단 또는 일상생활 불가능"],
    ["정상적", "면담 시 약간 지체", "면담 시 뚜렷한 지체", "면담이 어려움", "완전한 혼미 상태"],
    ["없다", "조금 초조", "손/머리카락 만지작", "가만히 못 있고 움직임", "손 비비기, 손톱 물어뜯기 등"],
    ["없다", "긴장감과 과민함", "사소한 일들 걱정", "염려 태도가 얼굴/말에서 뚜렷", "묻지 않아도 공포 표현"],
    ["없다", "경도", "중등도", "고도", "기능 수행 불가"],
    ["없다", "입맛 저하 있으나 격려 없이 섭취", "격려 없이는 섭취 어려움, 약 요구"],
    ["없다", "팔다리 무거움, 기운 없음", "뚜렷한 신체 증상 있음"],
    ["없다", "경도", "고도"],
    ["없다", "몸에 대해 많이 생각함", "건강에 집착", "건강 나쁨 자주 호소/도움 요청", "건강염려 망상"],
    ["체중 감소 없음", "체중 감소 있음", "확실한 체중감소 있음"],
    ["우울함과 질병을 인식", "병을 인정하나 외부 요인 탓", "병을 전적으로 부인"]
]

answers_en = [
    ["Absent", "Indicated only on questioning", "Spontaneously reported", "Non-verbal expression", "Only depressed state expressed"],
    ["Absent", "Self-reproach", "Ideas of guilt / rumination", "Illness seen as punishment", "Accusatory voices / hallucinations"],
    ["Absent", "Feels life not worth living", "Wishes dead or thoughts of death", "Suicidal ideas or gestures", "Serious suicide attempts"],
    ["No difficulty", "Occasional difficulty >30min", "Difficulty every night"],
    ["No difficulty", "Restless/disturbed", "Wakes and gets out of bed"],
    ["No difficulty", "Wakes early but sleeps again", "Cannot fall asleep again"],
    ["No difficulty", "Fatigue or weakness in activities", "Loss of interest", "Less activity or productivity", "Stopped working or no activities"],
    ["Normal", "Slight retardation", "Obvious retardation", "Interview difficult", "Complete stupor"],
    ["None", "Fidgetiness", "Plays with hands/hair", "Moves about", "Hand-wringing etc."],
    ["No difficulty", "Tension and irritability", "Worry over minor matters", "Apprehensive appearance", "Fears expressed without questioning"],
    ["Absent", "Mild", "Moderate", "Severe", "Incapacitating"],
    ["None", "Appetite loss without urging", "Needs urging or medication"],
    ["None", "Heaviness or fatigue", "Definite somatic symptoms"],
    ["Absent", "Mild", "Severe"],
    ["Not present", "Self-absorption", "Preoccupation with health", "Frequent complaints", "Hypochondriacal delusions"],
    ["No weight loss", "Probable weight loss", "Definite weight loss"],
    ["Acknowledges illness", "Attributes cause to external", "Denies illness"]
]

# 상태 초기화
if 'responses' not in st.session_state:
    st.session_state.responses = [None] * len(questions_ko)

st.title("Hamilton Depression Rating Scale (HDRS-17)")

# 문항별 선택 (드롭다운 형식으로 수정)
for i, question in enumerate(questions_ko):
    st.session_state.responses[i] = st.selectbox(
        label=question,
        options=list(range(len(answers_ko[i]))),
        format_func=lambda x: answers_ko[i][x],
        key=f"q_{i}"
    )

# 결과 계산 및 출력
if st.button("결과 보기"):
    results = []
    total_score = 0
    for i, score in enumerate(st.session_state.responses):
        en_question = questions_en[i]
        en_answer = answers_en[i][score]
        results.append(f"{i+1}. {en_question}\n   ({score}) {en_answer} (Score: {score})")
        total_score += score

    if total_score <= 7:
        interpretation = "WNL"
    elif total_score <= 13:
        interpretation = "Mild depression"
    elif total_score <= 18:
        interpretation = "Moderate depression"
    elif total_score <= 22:
        interpretation = "Severe depression"
    else:
        interpretation = "Very severe depression"

    output = "Hamilton Depression Rating Scale (HDRS-17) Results\n" + "\n".join(results) + f"\nTotal Score: {total_score}\nInterpretation: {interpretation}"
    st.code(output)

