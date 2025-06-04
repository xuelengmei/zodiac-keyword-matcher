import streamlit as st

st.set_page_config(page_title="性格关键词匹配器", page_icon="🧠")

st.title("🧠 星座关键词匹配小助手")

st.markdown("从下方选择符合你性格的词，我来帮你“猜”你可能属于哪个星座~")

# 性格关键词库
traits = [
    "内向", "外向", "感性", "理性", "爱自由", "粘人", "热情", "敏感",
    "幽默", "冷静", "社恐", "浪漫", "固执", "开朗", "细腻", "神秘"
]

# 星座性格映射表（简化示例）
zodiac_traits = {
    "白羊座": ["热情", "外向", "冲动", "幽默"],
    "金牛座": ["理性", "固执", "冷静", "细腻"],
    "双子座": ["幽默", "外向", "开朗", "爱自由"],
    "巨蟹座": ["敏感", "粘人", "内向", "浪漫"],
    "狮子座": ["外向", "热情", "自信", "固执"],
    "处女座": ["理性", "细腻", "冷静", "神秘"],
    "天秤座": ["开朗", "优雅", "爱自由", "理性"],
    "天蝎座": ["神秘", "敏感", "冷静", "感性"],
    "射手座": ["爱自由", "外向", "幽默", "热情"],
    "摩羯座": ["冷静", "理性", "固执", "内向"],
    "水瓶座": ["爱自由", "神秘", "理性", "幽默"],
    "双鱼座": ["感性", "浪漫", "粘人", "内向"]
}

# 多选性格
selected_traits = st.multiselect("🧩 请选择你的性格关键词", traits)

if st.button("🔍 开始匹配"):
    if not selected_traits:
        st.warning("请先选择至少一个关键词噢～")
    else:
        match_scores = {}
        for zodiac, t_list in zodiac_traits.items():
            score = len(set(selected_traits) & set(t_list))
            if score > 0:
                match_scores[zodiac] = score

        if match_scores:
            sorted_matches = sorted(match_scores.items(), key=lambda x: x[1], reverse=True)
            top_matches = [f"{z}（匹配度：{s}）" for z, s in sorted_matches[:3]]
            st.success("你可能是这些星座之一：")
            st.write("、".join(top_matches))
        else:
            st.info("没有明显的匹配结果，可能你的性格太独特啦！🌟")

st.markdown("---")
st.caption("🔮 结果仅供参考，星座只是性格的一个切面～")
