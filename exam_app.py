import streamlit as st
import random
import datetime

# ==========================================
# 1. 題庫資料 (與之前相同)
# ==========================================
QUESTION_DB = {
    "(114上)服務業經營管理": [
        {"q": "在服務行銷的7P組合中，除了傳統的4P之外，增加了哪三項？", "options": ["人員(People)、實體環境(Physical Evidence)、服務過程(Process)", "價格(Price)、推廣(Promotion)、通路(Place)", "政治(Politics)、公共關係(Public)、權力(Power)", "規劃(Plan)、執行(Practice)、考核(Performance)"], "ans": 0, "diff": "中等", "type": "單選"},
        {"q": "服務具有哪四大特性，使其管理不同於實體產品？(多選)", "options": ["無形性", "不可分割性", "異質性", "易逝性/不可儲存性"], "ans": [0, 1, 2, 3], "diff": "困難", "type": "多選"},
        {"q": "PZB服務品質缺口模型中，『顧客期望的服務』與『顧客認知的服務』之間的落差，稱為？", "options": ["缺口1 (知識缺口)", "缺口3 (傳遞缺口)", "缺口5 (服務缺口)", "缺口2 (標準缺口)"], "ans": 2, "diff": "困難", "type": "單選"},
        {"q": "關於『服務三角』(Service Triangle) 的敘述，何者正確？", "options": ["公司與顧客之間是互動行銷", "員工與顧客之間是外部行銷", "公司與員工之間是內部行銷", "以上皆非"], "ans": 2, "diff": "簡單", "type": "單選"},
        {"q": "服務藍圖(Service Blueprint)中的『互動線』(Line of Interaction)是用來區隔？", "options": ["前台員工與後台員工", "顧客與前台接觸員工", "後台員工與支援系統", "管理層與基層"], "ans": 1, "diff": "中等", "type": "單選"}
    ],
    "(114上)家庭、社區與環境": [
        {"q": "Bronfenbrenner 的生態系統理論中，個人直接參與且互動最頻繁的環境（如家庭、學校）稱為？", "options": ["微系統 (Microsystem)", "中系統 (Mesosystem)", "外系統 (Exosystem)", "巨系統 (Macrosystem)"], "ans": 0, "diff": "簡單", "type": "單選"},
        {"q": "下列何者屬於社區的『生產-分配-消費』功能？", "options": ["鄰居互相幫忙照顧小孩", "社區舉辦中秋晚會", "社區內的便利商店提供生活物資販售", "制定社區公約"], "ans": 2, "diff": "中等", "type": "單選"},
        {"q": "關於『永續社區』的特徵，下列何者正確？(多選)", "options": ["強調生態環境的保護", "追求經濟發展但不犧牲環境", "重視社會公平與居民參與", "完全禁止任何商業活動"], "ans": [0, 1, 2], "diff": "中等", "type": "多選"},
        {"q": "家庭生命週期中，『空巢期』是指哪個階段？", "options": ["子女出生到就學", "子女全部離家到家長退休", "退休到死亡", "新婚到子女出生"], "ans": 1, "diff": "簡單", "type": "單選"},
        {"q": "『鄰避效應』(NIMBY) 通常是指社區居民對於哪類設施的抗拒？", "options": ["公園綠地", "嫌惡設施（如垃圾場、變電所）", "圖書館", "便利商店"], "ans": 1, "diff": "簡單", "type": "單選"}
    ],
    "(114上)生態旅遊": [
        {"q": "根據國際生態旅遊協會(TIES)定義，生態旅遊的核心精神包含哪些？(多選)", "options": ["對自然環境負責任", "保障當地居民福祉", "具有解說與教育意義", "以獲取最大商業利潤為首要目標"], "ans": 0, "diff": "中等", "type": "多選"},
        {"q": "『環境承載量』(Carrying Capacity) 是指？", "options": ["遊覽車的最大載客數", "環境能承受人類活動干擾而不發生不可逆破壞的最大限度", "遊客願意支付的最高金額", "飯店的最大容納人數"], "ans": 1, "diff": "簡單", "type": "單選"},
        {"q": "無痕山林 (Leave No Trace, LNT) 的七大準則中，不包含下列哪一項？", "options": ["適當處理垃圾", "保持環境原有的風貌", "盡量餵食野生動物以表示友善", "降低用火對環境的衝擊"], "ans": 2, "diff": "簡單", "type": "單選"},
        {"q": "下列何者是『大眾旅遊』與『生態旅遊』的主要區別？", "options": ["大眾旅遊強調量，生態旅遊強調質與體驗", "大眾旅遊費用較高", "生態旅遊不需導覽解說", "大眾旅遊地點通常在偏遠山區"], "ans": 0, "diff": "簡單", "type": "單選"},
        {"q": "關於生態旅遊中的『解說』(Interpretation)，其目的為何？", "options": ["單純背誦學名", "連結遊客與資源的情感，啟發保育意識", "強迫遊客購買紀念品", "只是為了打發時間"], "ans": 1, "diff": "中等", "type": "單選"}
    ],
    "(114上)婚姻與家人關係": [
        {"q": "Sternberg 的『愛情三角理論』包含哪三個元素？", "options": ["金錢、時間、體力", "親密(Intimacy)、激情(Passion)、承諾(Commitment)", "溝通、妥協、接納", "外貌、個性、背景"], "ans": 1, "diff": "簡單", "type": "單選"},
        {"q": "Satir (薩提爾) 提出的溝通姿態中，『指責型』的人通常忽略了什麼？", "options": ["自我", "他人", "情境", "所有一切"], "ans": 1, "diff": "中等", "type": "單選"},
        {"q": "『三明治世代』(Sandwich Generation) 是指哪一群人？", "options": ["喜歡吃三明治的人", "同時要照顧年邁父母與未成年子女的中年人", "夾在兩位主管之間的員工", "在學校與補習班之間奔波的學生"], "ans": 1, "diff": "簡單", "type": "單選"},
        {"q": "下列關於『家庭壓力ABC-X模型』的敘述，何者正確？", "options": ["A代表壓力事件", "B代表家庭擁有的資源", "C代表家庭對事件的認知/界定", "以上皆是"], "ans": 3, "diff": "困難", "type": "單選"},
        {"q": "Baumrind 提出的教養風格中，何者被認為最能培養出負責且有自信的孩子？", "options": ["專制型", "放任型", "威信型/開明型", "忽視型"], "ans": 2, "diff": "中等", "type": "單選"}
    ],
    "(114上)個人行銷與形象管理": [
        {"q": "根據 Albert Mehrabian 的法則，在第一印象中，視覺外表(非語言)佔了多少比例？", "options": ["7%", "38%", "55%", "90%"], "ans": 2, "diff": "中等", "type": "單選"},
        {"q": "進行個人行銷時，SWOT分析中的『O』代表什麼？", "options": ["優勢 (Strengths)", "劣勢 (Weaknesses)", "機會 (Opportunities)", "威脅 (Threats)"], "ans": 2, "diff": "簡單", "type": "單選"},
        {"q": "關於『電梯簡報』(Elevator Pitch)，下列特徵何者錯誤？", "options": ["時間短促，約30-60秒", "重點在於引發對方興趣", "需要詳細說明所有人生經歷", "精準傳達個人價值"], "ans": 2, "diff": "簡單", "type": "單選"},
        {"q": "形象管理的『T.P.O.』原則是指穿著要考慮哪三點？(多選)", "options": ["時間 (Time)", "地點 (Place)", "場合/目的 (Occasion)", "價格 (Price)"], "ans": [0, 1, 2], "diff": "中等", "type": "多選"},
        {"q": "在口語溝通中，除了內容本身，『副語言』(Paralanguage) 包含哪些要素？", "options": ["音量大小", "語速快慢", "語調起伏", "以上皆是"], "ans": 3, "diff": "中等", "type": "單選"}
    ]
}

# ==========================================
# 2. APP 邏輯
# ==========================================
def main():
    st.set_page_config(page_title="空大期末考衝刺", page_icon="📝")
    
    # 側邊欄：設定考試參數
    st.sidebar.title("⚙️ 考試設定")
    selected_subject = st.sidebar.selectbox("1. 選擇科目", list(QUESTION_DB.keys()))
    difficulty = st.sidebar.radio("2. 選擇難度", ["簡單", "中等", "困難"], index=1)
    
    # 初始化 Session State (紀錄考試狀態)
    if 'exam_started' not in st.session_state:
        st.session_state.exam_started = False
    if 'current_questions' not in st.session_state:
        st.session_state.current_questions = []

    # 倒數計時顯示
    exam_date = datetime.date(2026, 1, 10)
    today = datetime.date.today()
    days_left = (exam_date - today).days
    
    st.title("🚀 空大期末考衝刺系統 (114上)")
    if days_left > 0:
        st.error(f"⚠️ 距離 1/10 考試只剩 {days_left} 天！")
    else:
        st.success("就是這週末了！加油！")

    # === 主頁面：尚未開始考試 ===
    if not st.session_state.exam_started:
        st.info(f"準備進行科目：**{selected_subject}**")
        st.write("點擊下方按鈕生成試卷...")
        
        if st.button("🔥 開始測驗", use_container_width=True):
            # 篩選題目邏輯
            raw_questions = QUESTION_DB.get(selected_subject, [])
            filtered_q = []
            for q in raw_questions:
                # 簡單模式包含簡單；中等包含簡單+中等；困難包含所有
                if difficulty == "簡單" and q['diff'] != "簡單": continue
                if difficulty == "中等" and q['diff'] == "困難": continue
                filtered_q.append(q)
            
            if not filtered_q:
                st.warning("該設定下沒有題目，請放寬條件！")
            else:
                random.shuffle(filtered_q)
                st.session_state.current_questions = filtered_q
                st.session_state.user_answers = {}  # 重置答案
                st.session_state.exam_started = True
                st.rerun()

    # === 考試頁面 ===
    else:
        st.subheader(f"📖 科目：{selected_subject}")
        
        with st.form("exam_form"):
            questions = st.session_state.current_questions
            
            for idx, q in enumerate(questions):
                st.markdown(f"**第 {idx+1} 題：{q['q']}**")
                
                # 生成唯一 key，避免衝突
                q_key = f"q_{idx}"
                
                if q['type'] == "單選":
                    # 單選題
                    st.radio(
                        "請選擇：", 
                        q['options'], 
                        key=q_key, 
                        index=None, 
                        label_visibility="collapsed"
                    )
                else:
                    # 多選題
                    st.write("(複選)")
                    for opt_idx, opt in enumerate(q['options']):
                        st.checkbox(opt, key=f"{q_key}_{opt_idx}")
                
                st.divider()

            # 交卷按鈕
            submitted = st.form_submit_button("📝 交卷計分", use_container_width=True)
            
            if submitted:
                score = 0
                results = []
                
                for idx, q in enumerate(questions):
                    q_key = f"q_{idx}"
                    is_correct = False
                    user_ans_display = ""
                    
                    if q['type'] == "單選":
                        user_selection = st.session_state.get(q_key)
                        if user_selection:
                            # 找出選項 index
                            try:
                                ans_idx = q['options'].index(user_selection)
                                if ans_idx == q['ans']:
                                    is_correct = True
                                user_ans_display = user_selection
                            except:
                                pass
                        else:
                            user_ans_display = "未作答"
                            
                    else: # 多選
                        user_indices = []
                        user_ans_text = []
                        for opt_idx, opt in enumerate(q['options']):
                            if st.session_state.get(f"{q_key}_{opt_idx}"):
                                user_indices.append(opt_idx)
                                user_ans_text.append(opt)
                        
                        if sorted(user_indices) == sorted(q['ans']):
                            is_correct = True
                        user_ans_display = "、".join(user_ans_text) if user_ans_text else "未作答"

                    if is_correct:
                        score += 1
                        results.append(f"✅ 第 {idx+1} 題答對")
                    else:
                        # 顯示正確答案
                        if q['type'] == "單選":
                            correct_ans = q['options'][q['ans']]
                        else:
                            correct_ans = "、".join([q['options'][i] for i in q['ans']])
                        results.append(f"❌ 第 {idx+1} 題答錯 (你的答案：{user_ans_display} | 正解：{correct_ans})")

                # 顯示結果
                st.session_state.exam_results = {
                    "score": score,
                    "total": len(questions),
                    "details": results
                }
                st.session_state.exam_finished = True

        # === 顯示成績結果 ===
        if st.session_state.get("exam_finished"):
            res = st.session_state.exam_results
            final_score = int((res['score'] / res['total']) * 100)
            
            st.markdown("### 📊 測驗結果")
            if final_score >= 90:
                st.success(f"太強了！得分：{final_score} 分")
            elif final_score >= 60:
                st.warning(f"及格過關！得分：{final_score} 分")
            else:
                st.error(f"需要加強喔！得分：{final_score} 分")
            
            with st.expander("查看詳細答題狀況"):
                for line in res['details']:
                    st.write(line)
            
            if st.button("🔄 再考一次"):
                st.session_state.exam_started = False
                st.session_state.exam_finished = False
                st.rerun()

if __name__ == "__main__":
    main()
