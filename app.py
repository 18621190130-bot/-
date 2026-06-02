import streamlit as st
from recommend import recommend

st.title("📚 图书推荐系统")

st.write("请输入你的阅读偏好，比如：喜欢科幻、宇宙、未来科技")

user_input = st.text_area("你的兴趣：")

if st.button("开始推荐"):
    if user_input:
        results = recommend(user_input)

        st.subheader("推荐结果：")
        for r in results:
            st.write(f"📖 {r['书名']}（{r['作者']}）")
            st.write(f"📂 类别：{r['类别']}")
            st.write(f"📝 简介：{r['简介']}")
            st.write(f"⭐ 相似度：{r['相似度']:.4f}")
            st.write("---")
    else:
        st.warning("请输入你的兴趣！")