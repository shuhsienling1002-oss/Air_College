import streamlit as st
import random

# ==========================================
# 終極完整題庫 (單一檔案版，無須拼接)
# 包含：所有歷屆考題 + 課本精華
# ==========================================
QUESTION_DB = {
    "(114上)服務業經營管理": [
        # --- 113學年度 期末考題 (正參/副參) ---
        {"q": "(113期末) 行銷4P包含哪些內容？", "options": ["產品 (Product)", "價格 (Price)", "以上皆是"], "ans": 2, "diff": "簡單", "type": "單選", "expl": "行銷4P：產品、價格、通路、推廣。"},
        {"q": "(113期末) 下列何者不屬於廠商廣設通路的行銷行為？", "options": ["便利商店於全國各地增設分店", "星巴克咖啡採取第二杯由星巴克請客", "台灣高鐵與郵局合作以利乘客取票"], "ans": 1, "diff": "中等", "type": "單選", "expl": "星巴克買一送一屬於『推廣/促銷』，而非通路。"},
        {"q": "(113期末) 行銷人員將整體消費市場區分為若干消費族群的分類過程，是指STP策略中的哪一項？", "options": ["市場區隔 (Segmentation)", "目標市場 (Targeting)", "產品定位 (Positioning)"], "ans": 0, "diff": "中等", "type": "單選"},
        {"q": "(113期末) 針對現今市場上已有的產品，增加公司的服務項目，讓顧客感到新穎、有價值，此為？", "options": ["服務延伸", "全新服務", "服務改善"], "ans": 0, "diff": "中等", "type": "單選"},
        {"q": "(113期末) 運用軟硬體技術，針對銷售、行銷、顧客服務與支援等範疇進行自動化並改善企業流程，此為？", "options": ["品質管理", "服務管理", "顧客關係管理 (CRM)"], "ans": 2, "diff": "中等", "type": "單選"},
        {"q": "(113期末) 影響顧客滿意度之決定因素為何？", "options": ["期望", "失驗", "以上皆是"], "ans": 2, "diff": "簡單", "type": "單選"},
        {"q": "(113期末) 2021年7月1日我國實施房地合一稅2.0，規定兩年內房屋交易所得課稅稅率提升至多少？", "options": ["20%", "35%", "45%"], "ans": 2, "diff": "困難", "type": "單選"},
        {"q": "(113期末) ESG政策中的『G』指的是什麼？", "options": ["環境保護", "社會責任", "公司治理 (Governance)"], "ans": 2, "diff": "簡單", "type": "單選"},
        {"q": "(113期末) 給予顧客信賴感、正確執行服務的能力，是SERVQUAL量表中的哪一構面？", "options": ["反應性", "可靠性", "關懷性"], "ans": 1, "diff": "中等", "type": "單選"},
        {"q": "(113期末) 航空運輸業中，『航班平均載客人數 / 座位數』稱為？", "options": ["積載因子 (Load Factor)", "能量因子", "速度因子"], "ans": 0, "diff": "困難", "type": "單選"},
        # --- 歷屆精選 ---
        {"q": "顧客忠誠度可藉由哪三個指標來衡量？(多選)", "options": ["再次購買的意願", "向他人推薦的意願", "對價格的容忍度", "顧客的年齡"], "ans": [0, 1, 2], "diff": "困難", "type": "多選"},
        {"q": "服務具有哪四大特性？(多選)", "options": ["無形性", "不可分割性", "異質性", "易逝性"], "ans": [0, 1, 2, 3], "diff": "困難", "type": "多選"},
        {"q": "在服務行銷的7P組合中，除了傳統的4P之外，增加了哪三項？", "options": ["人員、實體環境、服務過程", "價格、推廣、通路", "政治、公共關係、權力", "規劃、執行、考核"], "ans": 0, "diff": "中等", "type": "單選"},
        {"q": "服務藍圖中的『互動線』是用來區隔？", "options": ["前台員工與後台員工", "顧客與前台接觸員工", "後台員工與支援系統", "管理層與基層"], "ans": 1, "diff": "中等", "type": "單選"},
        {"q": "PZB服務品質缺口模型中，『顧客期望的服務』與『顧客認知的服務』之間的落差，稱為？", "options": ["缺口1 (知識缺口)", "缺口5 (服務缺口)", "缺口3 (傳遞缺口)"], "ans": 1, "diff": "困難", "type": "單選", "expl": "缺口5是最終結果，即顧客滿意度缺口。"}
    ],

    "(114上)家庭、社區與環境": [
        # --- 歷屆試題與課本重點 ---
        {"q": "Bronfenbrenner 的生態系統理論中，個人直接參與且互動最頻繁的環境（如家庭、學校）稱為？", "options": ["微系統", "中系統", "外系統", "巨系統"], "ans": 0, "diff": "簡單", "type": "單選"},
        {"q": "下列何者屬於社區的『生產-分配-消費』功能？", "options": ["鄰居互相幫忙", "社區中秋晚會", "便利商店/菜市場交易", "社區公約"], "ans": 2, "diff": "中等", "type": "單選"},
        {"q": "關於『永續社區』的特徵，下列何者正確？(多選)", "options": ["強調生態環境保護", "追求經濟發展但不犧牲環境", "重視社會公平與居民參與", "完全禁止商業活動"], "ans": [0, 1, 2], "diff": "中等", "type": "多選"},
        {"q": "家庭生命週期中，『空巢期』是指哪個階段？", "options": ["子女出生到就學", "子女全部離家到家長退休", "退休到死亡", "新婚"], "ans": 1, "diff": "簡單", "type": "單選"},
        {"q": "『鄰避效應』(NIMBY) 通常是指社區居民對於哪類設施的抗拒？", "options": ["公園綠地", "嫌惡設施（如垃圾場、變電所）", "圖書館", "學校"], "ans": 1, "diff": "簡單", "type": "單選"},
        {"q": "家事分工的不平等，導致職業婦女下班後需進行第二份工作，此現象被社會學家稱為？", "options": ["玻璃天花板", "第二輪班 (The Second Shift)", "異化勞動", "邊際效應"], "ans": 1, "diff": "中等", "type": "單選"},
        {"q": "根據 Maslow 的需求層次理論，參與社區巡守隊或志工服務，最主要能滿足個人的何種需求？", "options": ["生理需求", "安全需求", "愛與隸屬 / 尊榮感", "自我放棄"], "ans": 2, "diff": "中等", "type": "單選"},
        {"q": "『仕紳化』(Gentrification) 對社區的影響通常為何？", "options": ["房價下跌", "中產階級遷入，導致原低收入居民被迫遷離", "社區變髒亂", "無影響"], "ans": 1, "diff": "困難", "type": "單選"},
        {"q": "關於『社會資本』(Social Capital) 的衡量，不包含下列哪一項？", "options": ["信任", "互惠規範", "社會網絡", "個人銀行存款"], "ans": 3, "diff": "簡單", "type": "單選"},
        {"q": "家庭資源管理中，『邊際效用遞減』是指？", "options": ["資源越多越好", "隨著消費量增加，每多一單位帶來的滿足感逐漸下降", "錢越用越少"], "ans": 1, "diff": "困難", "type": "單選"}
    ],

    "(114上)生態旅遊": [
        # --- 102/105學年度 期末考題改編 (大量補充) ---
        {"q": "(102期末) 把旅遊業當作純粹經濟產業，大力規劃以實現利益最大化，這符合生態旅遊的規劃精神嗎？", "options": ["符合", "不符合 (應以保育為優先)"], "ans": 1, "diff": "簡單", "type": "單選", "expl": "生態旅遊首重保育與永續，而非單純獲利。"},
        {"q": "(102期末) 晚間賞螢時，為了看清楚螢火蟲，應該拿手電筒直接照射嗎？", "options": ["應該，越亮越好", "不應該，強光會干擾求偶，應包紅色玻璃紙"], "ans": 1, "diff": "簡單", "type": "單選"},
        {"q": "(102期末) 下列何者是正確的『綠色旅遊』觀念？", "options": ["強調對環境友善，降低負擔", "為了省錢所以不買門票", "只去綠色的森林玩", "盡量使用一次性餐具"], "ans": 0, "diff": "簡單", "type": "單選"},
        {"q": "(102期末) 關於果皮處理，下列觀念何者正確？", "options": ["果皮會腐爛變成養分，所以可以隨地丟棄", "果皮仍屬於垃圾，應帶下山，不可隨意丟棄"], "ans": 1, "diff": "中等", "type": "單選", "expl": "高山分解緩慢，且可能改變野生動物食性，應遵守LNT原則。"},
        {"q": "(102期末) 『生產導向』的定義是先調查消費者需求再設計商品嗎？", "options": ["是", "否 (這是行銷導向)"], "ans": 1, "diff": "中等", "type": "單選"},
        {"q": "(102期末) 在遊憩機會序列(ROS)中，機動車輛最『少』出現在哪種環境？", "options": ["現代化環境", "原始環境", "半現代化環境"], "ans": 1, "diff": "簡單", "type": "單選"},
        {"q": "(102期末) 規劃遊樂區時，坡度大於幾度即不適合開車？", "options": ["50度", "60度", "70度", "80度"], "ans": 1, "diff": "困難", "type": "單選"},
        {"q": "(102期末) 遊客抵達後覺得活動已飽和、無法獲得滿意體驗的容許人數，稱為？", "options": ["生態承載量", "實質承載量", "社會承載量", "設施承載量"], "ans": 2, "diff": "中等", "type": "單選"},
        {"q": "(102期末) 遊客違反行為規範被發現時，內心產生的難為情感受屬於哪種道德情緒？", "options": ["無力感", "羞恥感", "罪惡感", "尷尬感"], "ans": 3, "diff": "中等", "type": "單選"},
        {"q": "(102期末) 哪種環境中，公廁、涼亭及販賣機等設施愈多愈好？", "options": ["現代化環境", "半現代化環境", "原始環境"], "ans": 0, "diff": "簡單", "type": "單選"},
        {"q": "(102期末) 哪種旅遊不但環保無汙染，還可深度探訪，是近年新風潮？", "options": ["摩托車旅遊", "汽車旅遊", "單車旅遊"], "ans": 2, "diff": "簡單", "type": "單選"},
        {"q": "(102期末) 澎湖居民用玄武岩、咾咕石砌築成圍牆以抵擋東北季風，稱為？", "options": ["花宅", "石宅", "菜宅", "砂宅"], "ans": 2, "diff": "困難", "type": "單選", "expl": "菜宅又稱『蜂巢田』。"},
        {"q": "(102期末) 停車場與露營區的容許使用量，屬於何種承載量？", "options": ["生態承載量", "實質/設施承載量", "社會承載量"], "ans": 1, "diff": "簡單", "type": "單選"},
        {"q": "(105期末) 生態旅遊的『承載量』包含哪四種類型？(多選)", "options": ["生態承載量", "實質/設施承載量", "社會/心理承載量", "經濟承載量 (通常不列入核心四類)", "管理承載量"], "ans": [0, 1, 2], "diff": "困難", "type": "多選"},
        {"q": "『里山倡議』(Satoyama Initiative) 的核心願景是？", "options": ["與自然和諧共生", "人定勝天", "全面都市化", "完全封山育林"], "ans": 0, "diff": "中等", "type": "單選"},
        {"q": "無痕山林 (LNT) 的七大準則中，不包含下列哪一項？", "options": ["適當處理垃圾", "保持環境原有的風貌", "盡量餵食野生動物", "降低用火對環境的衝擊"], "ans": 2, "diff": "簡單", "type": "單選"},
        {"q": "『漂綠』(Greenwashing) 是指？", "options": ["企業誇大其環保作為，誤導消費者", "在牆壁漆上綠色", "多種樹", "使用綠能"], "ans": 0, "diff": "中等", "type": "單選"},
        {"q": "根據國際生態旅遊協會(TIES)定義，生態旅遊的核心精神包含哪些？(多選)", "options": ["對自然環境負責任", "保障當地居民福祉", "具有解說與教育意義", "以獲取最大商業利潤為首要目標"], "ans": [0, 1, 2], "diff": "中等", "type": "多選"},
        {"q": "『環境承載量』是指？", "options": ["遊覽車的最大載客數", "環境能承受人類活動干擾而不發生不可逆破壞的最大限度", "遊客願意支付的最高金額"], "ans": 1, "diff": "簡單", "type": "單選"},
        {"q": "下列何者是『大眾旅遊』與『生態旅遊』的主要區別？", "options": ["大眾旅遊強調量，生態旅遊強調質與體驗", "大眾旅遊費用較高", "生態旅遊不需導覽解說"], "ans": 0, "diff": "簡單", "type": "單選"}
    ],

    "(114上)婚姻與家人關係": [
        # --- 102學年度 期末考題改編 (大量補充) ---
        {"q": "(102期末) 職業婦女與家庭主婦在家務時間安排上，最大的不同在於『購物』的時間，對嗎？", "options": ["正確", "錯誤"], "ans": 1, "diff": "中等", "type": "單選", "expl": "最大差異通常在於平日白天的家務處理時間。"},
        {"q": "(102期末) 在臺灣，子女『一定』得從父姓嗎？", "options": ["是", "否 (可由父母約定)"], "ans": 1, "diff": "簡單", "type": "單選", "expl": "法律已修，可約定從母姓。"},
        {"q": "(102期末) 子女出生後，夫妻的角色分工通常會更趨向傳統（男主外女主內），對嗎？", "options": ["正確", "錯誤"], "ans": 0, "diff": "中等", "type": "單選", "expl": "這稱為『親職化導致的傳統化』。"},
        {"q": "(102期末) 影響老年夫妻與成年子女關係的主要因素，只是居住距離與互動次數，跟父母身體/財務無關？", "options": ["正確", "錯誤"], "ans": 1, "diff": "中等", "type": "單選"},
        {"q": "(102期末) 關於單親家庭，『單親家長必然會教養出問題子女』的說法是否正確？", "options": ["正確", "錯誤"], "ans": 1, "diff": "簡單", "type": "單選", "expl": "這是刻板印象。"},
        {"q": "(102期末) 家庭暴力事件中，受害者都有被虐的傾向，此說法正確嗎？", "options": ["正確", "錯誤"], "ans": 1, "diff": "簡單", "type": "單選", "expl": "這是『責怪受害者』的迷思。"},
        {"q": "(102期末) 婚姻關係強調在某一特定時間中，達到怎樣『好』(Good)的程度，其所指的是？", "options": ["婚姻的品質", "婚姻的成功", "婚姻的穩定"], "ans": 0, "diff": "中等", "type": "單選"},
        {"q": "(102期末) 哪類型的父母強調服從，並認為子女應無異議遵守其規則？", "options": ["主權型", "獨裁型/專制型", "放任型"], "ans": 1, "diff": "簡單", "type": "單選"},
        {"q": "(102期末) 手足互動中，何種行為是屬於社會所給予的規範及期望？", "options": ["衝突競爭", "扮演父母角色", "合作支持"], "ans": 2, "diff": "中等", "type": "單選"},
        {"q": "(102期末) 哪個階段對夫妻感情而言，是由谷底上升的重要轉折點？", "options": ["子女小學階段", "子女青少年階段", "子女離家階段 (空巢期)"], "ans": 2, "diff": "中等", "type": "單選", "expl": "育兒壓力減輕，夫妻滿意度回升 (U型曲線)。"},
        {"q": "(102期末) 手足間互動最『少』的年齡階段為？", "options": ["20~30歲", "30~40歲", "40~50歲"], "ans": 0, "diff": "困難", "type": "單選", "expl": "年輕成人期忙於建立自己的事業與家庭，手足互動減少。"},
        {"q": "(102期末) 哪種類型的祖父母期望與孫子女互動，且將角色視為一種休閒活動？", "options": ["趣味尋找型", "正規型", "家庭智慧儲藏庫型"], "ans": 0, "diff": "困難", "type": "單選"},
        {"q": "(102期末) 單親家長將注意力集中在孩子身上，形成過度保護，這屬於哪種親子關係？", "options": ["世代聯盟", "代罪羔羊式", "情緒緊密結合"], "ans": 1, "diff": "困難", "type": "單選"},
        {"q": "(102期末) 關於再婚的社會因素，下列敘述何者『不正確』？", "options": ["年輕離婚者比年長者易再婚", "男性比女性易再婚", "女性社會階層愈高，再婚可能性愈高"], "ans": 2, "diff": "困難", "type": "單選", "expl": "事實上，高社經地位女性再婚率反而較低 (婚姻梯度理論)。"},
        {"q": "(102期末) 繼親家庭需經歷哪四個階段的調適？(請選出正確組合)", "options": ["猜測、體諒、互動、進入行動", "幻想、現實、進入行動、加強關係", "干涉、不諒解、懷疑、現實"], "ans": 1, "diff": "困難", "type": "單選"},
        {"q": "(102期末) 下列何者『不是』單親家庭形成的主要原因？", "options": ["離婚", "喪偶", "未婚生子", "中彩券"], "ans": 3, "diff": "簡單", "type": "單選"},
        {"q": "Sternberg 的『愛情三角理論』包含哪三個元素？", "options": ["金錢、時間、體力", "親密、激情、承諾", "溝通、妥協、接納"], "ans": 1, "diff": "簡單", "type": "單選"},
        {"q": "『三明治世代』(Sandwich Generation) 是指？", "options": ["喜歡吃三明治的人", "同時照顧年邁父母與未成年子女的中年人", "奔波的學生"], "ans": 1, "diff": "簡單", "type": "單選"},
        {"q": "下列關於『家庭壓力ABC-X模型』的敘述，何者正確？", "options": ["A代表壓力事件", "B代表家庭擁有的資源", "C代表家庭對事件的認知/界定", "以上皆是"], "ans": 3, "diff": "困難", "type": "單選"},
        {"q": "Satir (薩提爾) 提出的溝通姿態中，『指責型』的人通常忽略了什麼？", "options": ["自我", "他人", "情境", "所有一切"], "ans": 1, "diff": "中等", "type": "單選"}
    ],

    "(114上)個人行銷與形象管理": [
        # --- 課本精華 ---
        {"q": "(Ch10) 關於歸因理論，當我們看到林專員每天上班都遲到(低一致性)，而他對其他事情也都遲到(低區辨性)，我們傾向將林專員的遲到歸因於？", "options": ["外在環境因素", "內在個人特質 (如懶惰)", "運氣不好"], "ans": 1, "diff": "困難", "type": "單選"},
        {"q": "(Ch12) 在非語言溝通中，下列哪一項通常被認為是最能洩漏真實情緒的線索，難以偽裝？", "options": ["說出的話語", "微表情 (Micro-expressions) 與肢體動作", "服裝品牌"], "ans": 1, "diff": "中等", "type": "單選"},
        {"q": "(Ch14) 個人行銷規劃流程的第一步通常是？", "options": ["直接開始推銷", "自我分析與定位 (SWOT)", "印名片"], "ans": 1, "diff": "中等", "type": "單選"},
        {"q": "(Ch15) 關於個人品牌的『定位』(Positioning)，核心概念為何？", "options": ["在目標受眾腦海中佔有一個獨特的位置", "模仿競爭對手", "價格越低越好"], "ans": 0, "diff": "困難", "type": "單選"},
        {"q": "(Ch16) 『喬哈里窗』(Johari Window) 中，『自己不知道，但別人看得很清楚』的區域稱為？", "options": ["開放區", "盲目區 (Blind Spot)", "隱藏區", "未知區"], "ans": 1, "diff": "困難", "type": "單選"},
        {"q": "根據 Albert Mehrabian 的法則，在第一印象中，視覺外表(非語言)佔了多少比例？", "options": ["7%", "38%", "55%", "90%"], "ans": 2, "diff": "中等", "type": "單選"},
        {"q": "進行個人行銷時，SWOT分析中的『O』代表什麼？", "options": ["優勢", "劣勢", "機會 (Opportunities)", "威脅"], "ans": 2, "diff": "簡單", "type": "單選"},
        {"q": "關於『電梯簡報』(Elevator Pitch)，下列特徵何者錯誤？", "options": ["時間短促", "重點在於引發興趣", "需詳細說明人生經歷", "精準傳達價值"], "ans": 2, "diff": "簡單", "type": "單選"},
        {"q": "形象管理的『T.P.O.』原則是指？(多選)", "options": ["時間 (Time)", "地點 (Place)", "場合/目的 (Occasion)", "價格"], "ans": [0, 1, 2], "diff": "中等", "type": "多選"}
    ]
}

# ==========================================
# APP 核心邏輯 (強制抽出最多 50 題)
# ==========================================
st.set_page_config(page_title="空大期末考衝刺", page_icon="🎓")
st.title("🎓 空大期末考衝刺系統 (v9.0 單一檔案終極版)")

# 初始化
if 'exam_finished' not in st.session_state: st.session_state.exam_finished = False
if 'exam_results' not in st.session_state: st.session_state.exam_results = []
if 'quiz_score' not in st.session_state: st.session_state.quiz_score = 0
if 'quiz' not in st.session_state: st.session_state.quiz = []

# 側邊欄
with st.sidebar:
    st.header("⚙️ 考試設定")
    subject = st.selectbox("選擇科目", list(QUESTION_DB.keys()))
    difficulty = st.radio("選擇難度", ["全部", "簡單", "中等", "困難"], index=0)
    
    # 顯示該科目總題數
    total_q_count = len(QUESTION_DB[subject])
    st.info(f"📚 題庫總數：{total_q_count} 題")
    
    if st.button("🔄 重置/開始新測驗", use_container_width=True):
        st.session_state.exam_finished = False
        st.session_state.quiz = []
        st.session_state.exam_results = []
        st.rerun()

# 篩選題目
def get_questions(subj, diff):
    all_q = QUESTION_DB[subj]
    if diff == "全部":
        return all_q
    return [q for q in all_q if q['diff'] == diff]

# 主畫面
if not st.session_state.exam_finished:
    if not st.session_state.quiz:
        questions = get_questions(subject, difficulty)
        if not questions:
            st.warning("⚠️ 此難度下沒有題目，請選擇其他難度。")
        else:
            # --- 關鍵修正：強制抽出最多 50 題 (或全部) ---
            sample_size = min(len(questions), 50)
            st.session_state.quiz = random.sample(questions, sample_size)

    if st.session_state.quiz:
        with st.form("exam_form"):
            user_ans_container = {}
            for i, q in enumerate(st.session_state.quiz):
                st.markdown(f"#### 第 {i+1} 題：{q['q']}")
                st.caption(f"難度：{q['diff']} | 題型：{q.get('type', '單選')}")
                
                if q.get('type') == "多選":
                    user_ans_container[i] = st.multiselect("請選擇答案 (可複選):", q['options'], key=f"q_{i}")
                else:
                    user_ans_container[i] = st.radio("請選擇一個答案:", q['options'], index=None, key=f"q_{i}")
                st.divider()
            
            if st.form_submit_button("📝 交卷計分", use_container_width=True):
                score = 0
                results = []
                for i, q in enumerate(st.session_state.quiz):
                    u_ans = user_ans_container[i]
                    is_corr = False
                    corr_idx = q['ans']
                    
                    if q.get('type') == "多選":
                        if not isinstance(corr_idx, list): corr_idx = [corr_idx]
                        corr_txt = [q['options'][x] for x in corr_idx]
                        if set(u_ans) == set(corr_txt):
                            score += 1
                            is_corr = True
                        results.append({"q": q['q'], "u": "、".join(u_ans), "c": "、".join(corr_txt), "ok": is_corr, "exp": q.get("expl", "")})
                    else:
                        corr_txt = q['options'][corr_idx]
                        if u_ans == corr_txt:
                            score += 1
                            is_corr = True
                        results.append({"q": q['q'], "u": u_ans, "c": corr_txt, "ok": is_corr, "exp": q.get("expl", "")})
                
                st.session_state.quiz_score = score
                st.session_state.exam_results = results
                st.session_state.exam_finished = True
                st.rerun()

else:
    # 結果頁面
    final_score = st.session_state.quiz_score
    total_q = len(st.session_state.quiz)
    st.metric("本次得分", f"{final_score} / {total_q}", delta=f"答對率 {final_score/total_q:.0%}")
    
    for i, res in enumerate(st.session_state.exam_results):
        with st.expander(f"第 {i+1} 題：{'✅' if res['ok'] else '❌'}"):
            st.markdown(f"**題目：** {res['q']}")
            if res['ok']: st.success(f"**您的答案：** {res['u']}")
            else:
                st.error(f"**您的答案：** {res['u']}")
                st.info(f"**正確答案：** {res['c']}")
            if res['exp']: st.caption(f"解析：{res['exp']}")
            
    if st.button("↩️ 返回首頁 (再測一次)", use_container_width=True):
        st.session_state.exam_finished = False
        st.session_state.quiz = []
        st.session_state.exam_results = []
        st.rerun()
