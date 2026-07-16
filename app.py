

import streamlit as st
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
import seaborn as sns


# 차트 시각화 소개
st.title("📊 튜토리얼 5: 차트 시각화")

# 예시용 숫자 데이터 생성
data = pd.DataFrame({
    "x": [1,2,3,4,5],
    "y": [-0.5, 1, -1, 2 , 0]
})

# matplotlib로 선 그래프를 생성
fig, ax = plt.subplots()
ax.plot(data["x"], data["y"], marker='o')

# Streamlit 차트 렌더링
st.pyplot(fig)

chart_data = pd.DataFrame(np.random.randn(10, 2), columns=["KOSPI", "S&P500"])
st.line_chart(chart_data, width=0, height=300, use_container_width=True)

data = {
        "Year": [2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026],
        "S&P500": [100, 150, 200, 180, 150, 130, 200, 250, 270],
        "KOSPI": [50, 80, 120, 90, 100, 80, 150, 200, 220]
        }

df = pd.DataFrame(data)
sns.set_palette("Set2")             # 그래프의 기본 색상 테마를 'Set2'로 설정
fig = plt.figure(figsize=(10, 6))   # 다중라인 그래프 그리기

plt.title("S&P500 and KOSPI Trend")
plt.xlabel("Year")
plt.ylabel("Index")
plt.legend()    # 범례
sns.lineplot(x="Year", y="S&P500", data=df, marker="o", label="S&P500")
sns.lineplot(x="Year", y="KOSPI", data=df, marker="o", label="KOSPI")
st.pyplot(fig)


labels = ["A", "B", "C", "D"]
sizes = [random.randint(1,10) for _ in range(len(labels))]

#그래프
fig, ax = plt.subplots()
ax.pie(sizes, labels = ["A", "B", "C", "D"], colors = ["lightsteelblue","thistle","bisque","lightsalmon"], autopct = "%1.1f%%", explode = [0 if s != min(sizes) else 0.1 for s in sizes])

st.pyplot(fig)
