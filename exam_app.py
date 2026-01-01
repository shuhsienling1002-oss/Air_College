import streamlit as st
import random
import datetime

# ==========================================
# 1. 終極救亡圖存版題庫 (Full Survival Pack)
# ==========================================
QUESTION_DB = {
    "(114上)服務業經營管理": [
        # --- 基礎概念 ---
        {"q": "在服務行銷的7P組合中，除了傳統的4P(產品/價格/推廣/通路)外，增加了哪三項？", "options": ["人員(People)、實體環境(Physical Evidence)、服務過程(Process)", "政治(Politics)、公共關係(Public)、權力(Power)", "規劃(Plan)、執行(Practice)、考核(Performance)", "利潤(Profit)、夥伴(Partner)、定位(Position)"], "ans": 0, "diff": "簡單", "type": "單選"},
        {"q": "服務具有哪四大特性(IHIP)？(多選)", "options": ["無形性 (Intangibility)", "不可分割性 (Inseparability)", "異質性 (Heterogeneity)", "易逝性/不可儲存性 (Perishability)"], "ans": [0, 1, 2, 3], "diff": "簡單", "type": "多選"},
        {"q": "PZB服務品質缺口模型中，『顧客期望的服務』與『顧客認知的服務』之間的落差，稱為？", "options": ["缺口5 (服務缺口)", "缺口1 (知識缺口)", "缺口3 (傳遞缺口)", "缺口2 (標準缺口)"], "ans": 0, "diff": "困難", "type": "單選"},
        {"q": "『關鍵時刻』(Moments of Truth) 的概念是由哪位學者或企業家發揚光大？", "options": ["北歐航空總裁 Jan Carlzon", "現代管理學之父 Peter Drucker", "行銷大師 Philip Kotler", "蘋果創辦人 Steve Jobs"], "ans": 0, "diff": "中等", "type": "單選"},
        {"q": "下列何者不屬於『內部行銷』的工作範疇？", "options": ["員工教育訓練", "建立服務文化", "針對終端消費者打廣告", "獎勵優秀員工"], "ans": 2, "diff": "簡單", "type": "單選"},
        {"q": "關於服務藍圖(Service Blueprint)的三條界線，下列排序何者正確（由上而下）？", "options": ["互動線 → 可視線 → 內部互動線", "可視線 → 互動線 → 內部互動線", "內部互動線 → 可視線 → 互動線", "互動線 → 內部互動線 → 可視線"], "ans": 0, "diff": "困難", "type": "單選"},
        {"q": "服務補救悖論 (Service Recovery Paradox) 是指什麼現象？", "options": ["服務失敗後經過成功的補救，顧客滿意度反而比未發生失敗前更高", "服務補救越做越糟", "顧客永遠不會原諒服務失誤", "補救成本高於服務利潤"], "ans": 0, "diff": "中等", "type": "單選"},
        {"q": "在排隊心理學中，下列何者會讓顧客覺得等待時間比較『短』？(多選)", "options": ["有事做的時候", "焦慮的時候", "這是一個公平的等待時", "不知還要等多久的時候"], "ans": [0, 2], "diff": "中等", "type": "多選"},
        {"q": "CRM 系統的核心目的是？", "options": ["降低生產成本", "最大化股東權益", "建立與顧客的長期獲利關係", "單純收集名單"], "ans": 2, "diff": "簡單", "type": "單選"},
        {"q": "『情感勞務』(Emotional Labor) 的定義為何？", "options": ["工作需要付出大量體力", "員工需要管理自己的情緒以展現出組織要求的表情", "同事之間談戀愛", "顧客對員工產生感情"], "ans": 1, "diff": "中等", "type": "單選"},
        {"q": "PZB服務品質模型中，『缺口1』(知識缺口) 產生的主因為何？", "options": ["管理者不了解顧客的期望", "服務標準未落實", "過度誇大的廣告", "第一線員工態度不佳"], "ans": 0, "diff": "中等", "type": "單選"},
        {"q": "SERVQUAL 量表的五大構面(RATER)不包含下列何者？", "options": ["可靠性 (Reliability)", "回應性 (Responsiveness)", "保證性 (Assurance)", "價格低廉性 (Cheapness)"], "ans": 3, "diff": "中等", "type": "單選"},
        {"q": "在『服務三角』中，公司與員工之間的關係稱為？", "options": ["內部行銷", "外部行銷", "互動行銷", "關係行銷"], "ans": 0, "diff": "簡單", "type": "單選"},
        {"q": "CRM (顧客關係管理) 將顧客分為四類，其中『忠誠度低、貢獻度高』的顧客稱為？", "options": ["蝴蝶 (Butterflies)", "摯友 (True Friends)", "陌生人 (Strangers)", "藤壺 (Barnacles)"], "ans": 0, "diff": "困難", "type": "單選"},
        {"q": "『授權』(Empowerment) 給第一線員工的主要目的是？", "options": ["讓員工能快速回應顧客需求並解決問題", "讓主管可以偷懶", "減少薪資支出", "增加員工的工作量"], "ans": 0, "diff": "簡單", "type": "單選"}
    ],

    "(114上)家庭、社區與環境": [
        # --- 生態系統理論 ---
        {"q": "Bronfenbrenner 的生態系統理論中，個人直接參與且互動最頻繁的環境（如家庭、學校）稱為？", "options": ["微系統 (Microsystem)", "中系統 (Mesosystem)", "外系統 (Exosystem)", "巨系統 (Macrosystem)"], "ans": 0, "diff": "簡單", "type": "單選"},
        {"q": "下列何者屬於社區的『生產-分配-消費』功能？", "options": ["鄰居互相幫忙照顧小孩", "社區舉辦中秋晚會", "社區內的便利商店提供生活物資販售", "制定社區公約"], "ans": 2, "diff": "中等", "type": "單選"},
        {"q": "關於『永續社區』的特徵，下列何者正確？(多選)", "options": ["強調生態環境的保護", "追求經濟發展但不犧牲環境", "重視社會公平與居民參與", "完全禁止任何商業活動"], "ans": [0, 1, 2], "diff": "中等", "type": "多選"},
        {"q": "家庭生命週期中，『空巢期』是指哪個階段？", "options": ["子女出生到就學", "子女全部離家到家長退休", "退休到死亡", "新婚到子女出生"], "ans": 1, "diff": "簡單", "type": "單選"},
        {"q": "『鄰避效應』(NIMBY) 通常是指社區居民對於哪類設施的抗拒？", "options": ["公園綠地", "嫌惡設施（如垃圾場、變電所）", "圖書館", "便利商店"], "ans": 1, "diff": "簡單", "type": "單選"},
        {"q": "Bronfenbrenner 生態系統理論中，父母的工作場所、社區的醫療資源屬於哪一層？", "options": ["外系統 (Exosystem)", "微系統 (Microsystem)", "中系統 (Mesosystem)", "巨系統 (Macrosystem)"], "ans": 0, "diff": "困難", "type": "單選"},
        {"q": "文化價值觀、法律、習俗屬於生態系統的哪一層？", "options": ["巨系統 (Macrosystem)", "外系統", "中系統", "微系統"], "ans": 0, "diff": "中等", "type": "單選"},
        {"q": "社區的『社會化』功能是指？", "options": ["傳遞知識、社會價值與行為規範", "生產與消費商品", "維持社會秩序", "互相幫助"], "ans": 0, "diff": "中等", "type": "單選"},
        {"q": "『同質性高、人際關係緊密、重視傳統』是哪種社區的特徵？", "options": ["鄉村社區", "都市社區", "虛擬社區", "功能性社區"], "ans": 0, "diff": "簡單", "type": "單選"},
        {"q": "環境心理學中，當『個人空間』(Personal Space) 被侵犯時，人通常會產生什麼反應？", "options": ["壓力與防衛", "興奮", "放鬆", "無感"], "ans": 0, "diff": "簡單", "type": "單選"},
        {"q": "『擁擠』(Crowding) 與『密度』(Density) 的差別在於？", "options": ["密度是物理測量值，擁擠是心理主觀感受", "兩者完全一樣", "密度是心理感受，擁擠是物理值", "密度只計算車輛"], "ans": 0, "diff": "困難", "type": "單選"},
        {"q": "建立『高齡友善社區』的三大支柱是？(多選)", "options": ["健康", "參與", "安全", "高科技"], "ans": [0, 1, 2], "diff": "中等", "type": "多選"},
        {"q": "聯合國 SDGs (永續發展目標) 共有幾項？", "options": ["17項", "10項", "5項", "100項"], "ans": 0, "diff": "簡單", "type": "單選"},
        {"q": "『社區營造』的核心精神強調？", "options": ["由下而上 (Bottom-up) 的居民參與", "由政府全權主導", "以硬體建設為主", "引進財團開發"], "ans": 0, "diff": "簡單", "type": "單選"},
        {"q": "家庭生態系統中，『開放系統』的特徵是？", "options": ["與外界環境有能量與資訊的交換", "完全封閉不與外界往來", "拒絕改變", "以上皆非"], "ans": 0, "diff": "中等", "type": "單選"},
        {"q": "下列何者是『綠建築』(Green Building) 的指標？(多選)", "options": ["節能", "省水", "減廢", "使用昂貴建材"], "ans": [0, 1, 2], "diff": "中等", "type": "多選"}
    ],

    "(114上)生態旅遊": [
        # --- 定義與精神 ---
        {"q": "根據國際生態旅遊協會(TIES)定義，生態旅遊的核心精神包含哪些？(多選)", "options": ["對自然環境負責任", "保障當地居民福祉", "具有解說與教育意義", "以獲取最大商業利潤為首要目標"], "ans": 0, "diff": "中等", "type": "多選"},
        {"q": "『環境承載量』(Carrying Capacity) 是指？", "options": ["遊覽車的最大載客數", "環境能承受人類活動干擾而不發生不可逆破壞的最大限度", "遊客願意支付的最高金額", "飯店的最大容納人數"], "ans": 1, "diff": "簡單", "type": "單選"},
        {"q": "無痕山林 (Leave No Trace, LNT) 的七大準則中，不包含下列哪一項？", "options": ["適當處理垃圾", "保持環境原有的風貌", "盡量餵食野生動物以表示友善", "降低用火對環境的衝擊"], "ans": 2, "diff": "簡單", "type": "單選"},
        {"q": "下列何者是『大眾旅遊』與『生態旅遊』的主要區別？", "options": ["大眾旅遊強調量，生態旅遊強調質與體驗", "大眾旅遊費用較高", "生態旅遊不需導覽解說", "大眾旅遊地點通常在偏遠山區"], "ans": 0, "diff": "簡單", "type": "單選"},
        {"q": "關於生態旅遊中的『解說』(Interpretation)，其目的為何？", "options": ["單純背誦學名", "連結遊客與資源的情感，啟發保育意識", "強迫遊客購買紀念品", "只是為了打發時間"], "ans": 1, "diff": "中等", "type": "單選"},
        {"q": "『漂綠』(Greenwashing) 是指？", "options": ["企業誇大其環保作為，誤導消費者", "在牆壁漆上綠色", "多種樹", "使用綠能"], "ans": 0, "diff": "簡單", "type": "單選"},
        {"q": "『遊憩機會序列』(ROS) 的管理概念是為了？", "options": ["提供多樣化的遊憩體驗以滿足不同遊客", "限制所有遊客只能去同一區", "將所有區域開發成遊樂園", "完全禁止進入"], "ans": 0, "diff": "困難", "type": "單選"},
        {"q": "『可接受改變限度』(LAC) 取代了傳統的承載量概念，它更重視？", "options": ["環境品質與遊憩體驗的變化程度", "絕對的人數限制", "門票收入的增加", "停車場的大小"], "ans": 0, "diff": "困難", "type": "單選"},
        {"q": "在國家公園的分區管理中，通常哪一區嚴格禁止一般遊客進入？", "options": ["生態保護區", "遊憩區", "一般管制區", "史蹟保存區"], "ans": 0, "diff": "中等", "type": "單選"},
        {"q": "無痕山林 (LNT) 運動的七大準則包括？(多選)", "options": ["事前充分規劃與準備", "在可承受的地點行走與宿營", "適當處理垃圾維護環境", "保持環境原有的風貌", "減低用火對環境的衝擊", "尊重野生動植物", "考量其他使用者"], "ans": [0, 1, 2, 3, 4, 5, 6], "diff": "困難", "type": "多選"},
        {"q": "『碳足跡』是指產品或活動在生命週期中產生的？", "options": ["溫室氣體總排放量", "垃圾量", "廢水量", "噪音量"], "ans": 0, "diff": "簡單", "type": "單選"},
        {"q": "下列何者是『生態旅遊』的負面衝擊？", "options": ["過度開發導致棲地破碎化", "增加在地就業機會", "提升環境保育意識", "保存傳統文化"], "ans": 0, "diff": "簡單", "type": "單選"},
        {"q": "社區基礎生態旅遊 (CBET) 強調？", "options": ["社區居民擁有經營權與決策權", "外來財團全權管理", "居民只需負責表演", "政府強制徵收"], "ans": 0, "diff": "中等", "type": "單選"},
        {"q": "賞鯨豚活動若未遵守規範，最可能造成的生態衝擊是？", "options": ["干擾動物行為甚至造成傷害", "遊客暈船", "海水變鹹", "漁獲量增加"], "ans": 0, "diff": "簡單", "type": "單選"}
    ],

    "(114上)婚姻與家人關係": [
        # --- 愛情與擇偶 ---
        {"q": "Sternberg 的『愛情三角理論』包含哪三個元素？", "options": ["金錢、時間、體力", "親密(Intimacy)、激情(Passion)、承諾(Commitment)", "溝通、妥協、接納", "外貌、個性、背景"], "ans": 1, "diff": "簡單", "type": "單選"},
        {"q": "Satir (薩提爾) 提出的溝通姿態中，『指責型』的人通常忽略了什麼？", "options": ["自我", "他人", "情境", "所有一切"], "ans": 1, "diff": "中等", "type": "單選"},
        {"q": "『三明治世代』(Sandwich Generation) 是指哪一群人？", "options": ["喜歡吃三明治的人", "同時要照顧年邁父母與未成年子女的中年人", "夾在兩位主管之間的員工", "在學校與補習班之間奔波的學生"], "ans": 1, "diff": "簡單", "type": "單選"},
        {"q": "下列關於『家庭壓力ABC-X模型』的敘述，何者正確？", "options": ["A代表壓力事件", "B代表家庭擁有的資源", "C代表家庭對事件的認知/界定", "以上皆是"], "ans": 3, "diff": "困難", "type": "單選"},
        {"q": "Baumrind 提出的教養風格中，何者被認為最能培養出負責且有自信的孩子？", "options": ["專制型", "放任型", "威信型/開明型", "忽視型"], "ans": 2, "diff": "中等", "type": "單選"},
        {"q": "Sternberg 愛情三角理論中，只有『親密』與『激情』，缺乏承諾的愛稱為？", "options": ["浪漫之愛 (Romantic Love)", "迷戀之愛 (Infatuated Love)", "友伴之愛 (Companionate Love)", "愚昧之愛 (Fatuous Love)"], "ans": 0, "diff": "中等", "type": "單選"},
        {"q": "Murstein 的 SVR 擇偶理論，三個階段依序為？", "options": ["刺激(Stimulus) → 價值觀(Value) → 角色(Role)", "刺激 → 角色 → 價值觀", "價值觀 → 刺激 → 角色", "角色 → 刺激 → 價值觀"], "ans": 0, "diff": "困難", "type": "單選"},
        {"q": "依據家庭生命週期，婚姻滿意度通常呈現什麼形狀的變化？", "options": ["U型 (新婚高，育兒期降，空巢期回升)", "倒U型 (育兒期最高)", "直線上升", "直線下降"], "ans": 0, "diff": "中等", "type": "單選"},
        {"q": "在家庭溝通中，Satir 指出的『超理智型』(Computer) 特徵為？", "options": ["只講道理與邏輯，忽略情感", "總是討好別人", "總是責備別人", "轉移話題"], "ans": 0, "diff": "中等", "type": "單選"},
        {"q": "雙薪家庭常見的『角色衝突』是指？", "options": ["工作角色與家庭角色的需求互相牴觸", "夫妻爭奪戶長", "婆媳問題", "親子代溝"], "ans": 0, "diff": "簡單", "type": "單選"},
        {"q": "關於『繼親家庭』(Stepfamily) 的特徵，何者正確？", "options": ["界線模糊，角色定位需重新協商", "比初婚家庭更簡單", "親子關係通常比夫妻關係晚建立", "完全沒有法律問題"], "ans": 0, "diff": "中等", "type": "單選"},
        {"q": "處理夫妻衝突時，使用『我訊息』(I-message) 的結構通常是？", "options": ["敘述事實 + 表達感受 + 說明影響", "你總是... + 你應該...", "責備對方 + 翻舊帳", "沈默不語"], "ans": 0, "diff": "簡單", "type": "單選"},
        {"q": "下列何者屬於家庭暴力中的『精神暴力』？(多選)", "options": ["言語羞辱", "冷漠忽視", "限制行動自由", "經濟控制"], "ans": [0, 1, 2, 3], "diff": "簡單", "type": "多選"},
        {"q": "Reiss 的『車輪理論』描述的是什麼發展過程？", "options": ["職涯發展", "親密關係/愛情的發展", "兒童智力發展", "老年退休規劃"], "ans": 1, "diff": "困難", "type": "單選"}
    ],

    "(114上)個人行銷與形象管理": [
        # --- 形象基礎 ---
        {"q": "根據 Albert Mehrabian 的法則，在第一印象中，視覺外表(非語言)佔了多少比例？", "options": ["7%", "38%", "55%", "90%"], "ans": 2, "diff": "中等", "type": "單選"},
        {"q": "進行個人行銷時，SWOT分析中的『O』代表什麼？", "options": ["優勢 (Strengths)", "劣勢 (Weaknesses)", "機會 (Opportunities)", "威脅 (Threats)"], "ans": 2, "diff": "簡單", "type": "單選"},
        {"q": "關於『電梯簡報』(Elevator Pitch)，下列特徵何者錯誤？", "options": ["時間短促，約30-60秒", "重點在於引發對方興趣", "需要詳細說明所有人生經歷", "精準傳達個人價值"], "ans": 2, "diff": "簡單", "type": "單選"},
        {"q": "形象管理的『T.P.O.』原則是指穿著要考慮哪三點？(多選)", "options": ["時間 (Time)", "地點 (Place)", "場合/目的 (Occasion)", "價格 (Price)"], "ans": [0, 1, 2], "diff": "中等", "type": "多選"},
        {"q": "在口語溝通中，除了內容本身，『副語言』(Paralanguage) 包含哪些要素？", "options": ["音量大小", "語速快慢", "語調起伏", "以上皆是"], "ans": 3, "diff": "中等", "type": "單選"},
        {"q": "Johari Window (喬哈里窗) 中，『自己不知道，別人卻知道』的區域是？", "options": ["盲目區 (Blind Spot)", "開放區 (Open Area)", "隱藏區 (Hidden Area)", "未知區 (Unknown Area)"], "ans": 0, "diff": "中等", "type": "單選"},
        {"q": "首因效應 (Primacy Effect) 告訴我們？", "options": ["第一印象非常重要且難以改變", "最後一眼最重要", "印象會隨時間平均", "外表不重要"], "ans": 0, "diff": "簡單", "type": "單選"},
        {"q": "USP (Unique Selling Proposition) 的中文意思是？", "options": ["獨特銷售主張 (核心競爭力)", "通用銷售計畫", "聯合服務平台", "使用者標準程序"], "ans": 0, "diff": "簡單", "type": "單選"},
        {"q": "在商務介紹禮儀中，下列順序何者正確？", "options": ["將職位低者介紹給職位高者", "將女性介紹給男性", "將長輩介紹給晚輩", "將客人介紹給自己公司的人"], "ans": 0, "diff": "困難", "type": "單選"},
        {"q": "握手禮儀中，通常應由誰先伸手？", "options": ["職位高者、長輩、女士", "職位低者", "男士", "晚輩"], "ans": 0, "diff": "中等", "type": "單選"},
        {"q": "非語言溝通中的『空間距離』，一般社交距離(Social Distance)大約是？", "options": ["1.2 ~ 3.6 公尺", "0 ~ 45 公分 (親密)", "45 ~ 120 公分 (個人)", "3.6 公尺以上 (公眾)"], "ans": 0, "diff": "困難", "type": "單選"},
        {"q": "網路形象管理(Digital Footprint)需要注意什麼？(多選)", "options": ["避免情緒性發言", "保護隱私設定", "展現專業與一致性", "定期檢視搜尋結果"], "ans": [0, 1, 2, 3], "diff": "中等", "type": "多選"},
        {"q": "色彩心理學中，藍色通常傳達什麼樣的形象感覺？", "options": ["專業、冷靜、信任", "熱情、危險", "自然、和平", "神秘、奢華"], "ans": 0, "diff": "簡單", "type": "單選"}
    ]
}

# ==========================================
# 2. APP 邏輯 (畫面控制中心)
# ==========================================
def reset_exam():
    """當使用者改變設定時，強制重置考試狀態"""
    st.session_state.exam_started = False
    st.session_state.current_questions = []
    st.session_state.exam_results = {}
    st.session_state.user_answers = {}

def main():
    st.set_page_config(page_title="空大期末考衝刺", page_icon="📝")
    
    # 初始化 Session State
    if 'exam_started' not in st.session_state:
        st.session_state.exam_started = False
    if 'current_questions' not in st.session_state:
        st.session_state.current_questions = []
    if 'exam_results' not in st.session_state:
        st.session_state.exam_results = {}

    # 側邊欄：設定考試參數 (加入 on_change 監聽)
    st.sidebar.title("⚙️ 考試設定")
    selected_subject = st.sidebar.selectbox(
        "1. 選擇科目", 
        list(QUESTION_DB.keys()),
        on_change=reset_exam  # <--- 關鍵修改：改變科目自動重置
    )
    
    difficulty = st.sidebar.radio(
        "2. 選擇難度", 
        ["簡單", "中等", "困難"], 
        index=1,
        on_change=reset_exam  # <--- 關鍵修改：改變難度自動重置
    )
    
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
        st.markdown(f"難度設定：**{difficulty}**")
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
        st.subheader(f"📖 科目：{selected_subject} ({difficulty}模式)")
        
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
