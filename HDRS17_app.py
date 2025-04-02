import streamlit as st
import re

# HAM-D 항목 및 선택지 정의
questions = {
    1: ("우울한 기분", [
        "0 없다",
        "1 물어보았을 때만 우울한 기분이라고 말한다",
        "2 자발적으로 우울한 기분이라고 말한다",
        "3 얼굴 표정, 자세, 목소리, 쉽게 우는 경향과 같은 비언어적인 표현을 통해 우울한 기분을 나타낸다",
        "4 오로지 우울한 기분만을 언어적/비언어적 표현을 통해 나타낸다"
    ]),
    2: ("죄책감", [
        "0 없다",
        "1 자책하거나 자신이 사람들을 실망시킨다고 느낀다",
        "2 죄를 지었다고 생각하거나 과거의 실수에 대해 반복적으로 생각한다",
        "3 현재의 병을 벌로 여긴다. 죄책망상이 있다",
        "4 비난 또는 탄핵하는 목소리를 듣거나 위협적인 환시를 경험한다"
    ]),
    3: ("자살", [
        "0 없다",
        "1 인생이 살 가치가 없다고 느껴진다",
        "2 죽고 싶거나 죽는 상상을 한다",
        "3 자살 사고가 있거나 자살 기도를 시도한 행동을 한다",
        "4 심각한 자살 시도를 한다"
    ]),
    4: ("초기 불면증", [
        "0 잠드는 데 어려움이 없다",
        "1 가끔 잠들기 어렵다 (30분 이상)",
        "2 매일 잠들기 어렵다"
    ]),
    5: ("중기 불면증", [
        "0 없음",
        "1 편하고 깊게 자지 못한다",
        "2 자주 깬다, 뒤척인다 (소변 제외)"
    ]),
    6: ("말기 불면증", [
        "0 없음",
        "1 새벽에 깬다, 다시 잠든다",
        "2 깬 뒤 다시 잠들지 못한다"
    ]),
    7: ("일과 활동", [
        "0 어려움 없음",
        "1 피로하거나 기력 저하",
        "2 흥미 상실 또는 무관심",
        "3 활동 시간 감소 또는 생산성 저하",
        "4 활동 중단 또는 거의 불가능"
    ]),
    8: ("지체", [
        "0 정상",
        "1 면담 시 약간 지체됨",
        "2 뚜렷한 지체",
        "3 면담이 어려울 정도로 지체됨",
        "4 혼미 상태"
    ]),
    9: ("초조", [
        "0 없음",
        "1 약간 초조",
        "2 손/머리카락을 만지작거림",
        "3 가만히 못 있음",
        "4 손을 비비거나 입술 깨무는 행동 등"
    ]),
    10: ("정신적 불안", [
        "0 없음",
        "1 긴장, 과민",
        "2 사소한 일에 대해 걱정",
        "3 염려가 말/표정에 명백함",
        "4 묻지 않아도 심한 공포 표현"
    ]),
    11: ("신체적 불안", [
        "0 없음",
        "1 경도 (입마름 등)",
        "2 중등도 (심계항진, 두통)",
        "3 고도 (호흡곤란 등)",
        "4 최고도 (기능 거의 없음)"
    ]),
    12: ("위장관계 증상", [
        "0 없음",
        "1 입맛 저하, 속 더부룩",
        "2 강요 없이는 식사 못함, 약물 요구"
    ]),
    13: ("전반적 신체 증상", [
        "0 없음",
        "1 무거움, 통증, 피로",
        "2 매우 뚜렷한 신체증상"
    ]),
    14: ("성적 증상", [
        "0 없음",
        "1 경도",
        "2 고도"
    ]),
    15: ("건강염려증", [
        "0 없음",
        "1 몸에 대해 많이 생각함",
        "2 건강에 집착함",
        "3 자주 건강 이상 호소",
        "4 건강염려 망상"
    ]),
    16: ("체중감소 (하나 선택)", [
        "0 없음",
        "1 병으로 인한 감소 추정",
        "2 환자가 체중감소 인지함",
        "0 주당 0.5kg 미만 감소",
        "1 주당 0.5~1kg 미만 감소",
        "2 주당 1kg 이상 감소"
    ]),
    17: ("병식", [
        "0 병식 있음",
        "1 부분적으로 인정",
        "2 완전히 부인"
    ])
}

st.title("Hamilton Depression Rating Scale, HDRS-17")

responses = {}

with st.form("hdrs_form"):
    for i in range(1, 18):
        st.markdown(f"**{i}. {questions[i][0]}**")
        responses[i] = st.selectbox("선택하세요", questions[i][1], key=f"q{i}")
        st.markdown("---")
    submitted = st.form_submit_button("총점 계산 및 결과 보기")

if submitted:
    def extract_score(text):
        match = re.search(r"\((\d+)\)", text)
        return int(match.group(1)) if match else 0

    scores = []
    for i in range(1, 18):
        score = extract_score(responses[i])
        if i == 16:
            # 체중감소 중 높은 점수 사용
            alternatives = [int(n) for n in re.findall(r"\((\d+)\)", responses[i])]
            score = max(alternatives) if alternatives else 0
        scores.append(score)

    total = sum(scores)

    if total <= 7:
        interpretation = "정상"
    elif total <= 13:
        interpretation = "경도 우울"
    elif total <= 18:
        interpretation = "중등도 우울"
    elif total <= 22:
        interpretation = "고도 우울"
    else:
        interpretation = "최고도 우울"

    # 결과 출력
    result_lines = ["Hamilton Depression Rating Scale, HDRS", ""]
    for i in range(1, 18):
        result_lines.append(f"{i}. {questions[i][0]}: {responses[i]}")
    result_lines.append("")
    result_lines.append(f"총점: {total}")
    result_lines.append(f"임상적 해석: {interpretation}")
    final_output = "\n".join(result_lines)

    st.markdown("### 📝 결과 복사용")
    st.code(final_output, language="text")
