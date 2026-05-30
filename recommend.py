import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# =========================
# 1. 读取数据
# =========================
df = pd.read_excel("books_dataset.xlsx")

# =========================
# 2. 构造文本信息（很关键！）
# 把多列拼成“语义描述”
# =========================
df["text"] = df["书名"] + " " + df["所属类别"] + " " + df["书本简介（小于20字）"]

# =========================
# 3. 加载模型（第一次会稍慢）
# =========================
model = SentenceTransformer('all-MiniLM-L6-v2')

# =========================
# 4. 预计算图书向量（只做一次）
# =========================
book_embeddings = model.encode(df["text"].tolist())

# =========================
# 5. 推荐函数（给 Streamlit 用）
# =========================
def recommend(user_input, top_n=5):
    # 用户输入向量化
    user_embedding = model.encode([user_input])
    
    # 计算余弦相似度
    similarities = cosine_similarity(user_embedding, book_embeddings)[0]
    
    # 取前 top_n 个
    top_indices = similarities.argsort()[-top_n:][::-1]
    
    results = []
    for idx in top_indices:
        results.append({
            "书名": df.iloc[idx]["书名"],
            "作者": df.iloc[idx]["作者"],
            "类别": df.iloc[idx]["所属类别"],
            "简介": df.iloc[idx]["书本简介（小于20字）"],
            "相似度": float(similarities[idx])
        })
    
    return results


# =========================
# 6. 本地测试
# =========================
if __name__ == "__main__":
    user_input = input("请输入你的阅读偏好：")
    recs = recommend(user_input)
    
    print("\n推荐结果：")
    for r in recs:
        print(f"{r['书名']}（{r['作者']}）- 相似度: {r['相似度']:.4f}")