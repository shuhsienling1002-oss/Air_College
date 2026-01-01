import streamlit as st
import random
import datetime

# ==========================================
# 1. 核彈級・全考點覆蓋題庫 (The Ultimate Database)
# ==========================================
QUESTION_DB = {
    "(114上)服務業經營管理": [
        # --- 基礎概念 ---
        {"q": "在服務行銷的7P組合中，除了傳統的4P(產品/價格/推廣/通路)外，增加了哪三項？", "options": ["人員(People)、實體環境(Physical Evidence)、服務過程(Process)", "政治(Politics)、公共關係(Public)、權力(Power)", "規劃(Plan)、執行(Practice)、考核(Performance)", "利潤(Profit)、夥伴(Partner)、定位(Position)"], "ans": 0, "diff": "簡單", "type": "單選"},
        {"q": "服務具有哪四大特性(IHIP)？(多選)", "options": ["無形性 (Intangibility)", "不可分割性 (Inseparability)", "異質性 (Heterogeneity)", "易逝性/不可儲存性 (Perishability)"], "ans": [0, 1, 2, 3], "diff": "簡單", "type": "多選"},
        {"q": "服務的『易逝性』(Perishability) 導致的主要管理難題是？", "options": ["無法庫存，供需難以調節", "顧客不易評估品質", "服務品質難以標準化", "顧客必須參與生產"], "ans": 0, "diff": "簡單", "type": "單選"},
        {"q": "為了克服『不可分割性』(Inseparability)，服務業者常採取什麼策略？", "options": ["重視服務人員的選用與訓練", "使用專利權保護", "實施差別定價", "強調保固"], "ans": 0, "diff": "中等", "type": "單選"},
        {"q": "根據 Lovelock 的服務分類，『針對人的有形服務』(如理髮、醫療) 屬於？", "options": ["人體處理 (People Processing)", "物品處理 (Possession Processing)", "腦力刺激處理 (Mental Stimulus Processing)", "訊息處理 (Information Processing)"], "ans": 0, "diff": "困難", "type": "單選"},
        
        # --- 服務行銷 7P ---
        {"q": "服務行銷組合中，『實體環境』(Physical Evidence) 又稱為？", "options": ["服務場景 (Servicescape)", "服務藍圖", "服務劇本", "服務工廠"], "ans": 0, "diff": "簡單", "type": "單選"},
        {"q": "在定價策略中，『收益管理』(Yield Management) 最常應用於哪些行業？(多選)", "options": ["航空公司", "旅館業", "吃到飽餐廳", "便利商店"], "ans": [0, 1], "diff": "中等", "type": "多選"},
        {"q": "CRM (顧客關係管理) 將顧客分為四類，其中『忠誠度低、貢獻度高』的顧客稱為？", "options": ["蝴蝶 (Butterflies)", "摯友 (True Friends)", "陌生人 (Strangers)", "藤壺 (Barnacles)"], "ans": 0, "diff": "困難", "type": "單選"},
        
        # --- 服務品質與 PZB ---
        {"q": "PZB服務品質缺口模型中，『顧客期望的服務』與『顧客認知的服務』之間的落差，稱為？", "options": ["缺口5 (服務缺口)", "缺口1 (知識缺口)", "缺口3 (傳遞缺口)", "缺口2 (標準缺口)"], "ans": 0, "diff": "困難", "type": "單選"},
        {"q": "PZB 模型中，造成『缺口 3』(傳遞缺口) 的主要原因不包含？", "options": ["誇大的廣告宣傳", "員工與工作未能適配", "缺乏團隊合作", "缺乏適當的監控系統"], "ans": 0, "diff": "困難", "type": "單選"},
        {"q": "『可靠性』(Reliability) 在 SERVQUAL 量表中通常被顧客認為是？", "options": ["最重要的構面", "最不重要的構面", "與有形性一樣重要", "無法衡量的"], "ans": 0, "diff": "中等", "type": "單選"},
        {"q": "顧客對於服務品質的容忍範圍，介於『理想服務』與『適當服務』之間，稱為？", "options": ["容忍區 (Zone of Tolerance)", "接受區", "危險區", "滿意區"], "ans": 0, "diff": "困難", "type": "單選"},
        {"q": "『關鍵時刻』(Moments of Truth) 的概念是由哪位學者或企業家發揚光大？", "options": ["北歐航空總裁 Jan Carlzon", "現代管理學之父 Peter Drucker", "行銷大師 Philip Kotler", "蘋果創辦人 Steve Jobs"], "ans": 0, "diff": "中等", "type": "單選"},
        
        # --- 策略與管理 ---
        {"q": "『服務利潤鏈』(Service Profit Chain) 認為企業獲利的源頭是？", "options": ["內部服務品質 (員工滿意)", "低廉的成本", "大量的廣告", "高端的設備"], "ans": 0, "diff": "中等", "type": "單選"},
        {"q": "關於服務藍圖(Service Blueprint)的三條界線，下列排序何者正確（由上而下）？", "options": ["互動線 → 可視線 → 內部互動線", "可視線 → 互動線 → 內部互動線", "內部互動線 → 可視線 → 互動線", "互動線 → 內部互動線 → 可視線"], "ans": 0, "diff": "困難", "type": "單選"},
        {"q": "服務補救悖論 (Service Recovery Paradox) 是指什麼現象？", "options": ["服務失敗後經過成功的補救，顧客滿意度反而比未發生失敗前更高", "服務補救越做越糟", "顧客永遠不會原諒服務失誤", "補救成本高於服務利潤"], "ans": 0, "diff": "中等", "type": "單選"},
        {"q": "關於『情感勞務』的深層演出 (Deep Acting)，是指員工？", "options": ["嘗試從內心改變感受，真誠地表現出情緒", "只是表面假裝", "戴上面具", "皮笑肉不笑"], "ans": 0, "diff": "中等", "type": "單選"},
        {"q": "SSTs (自助服務科技) 的成功關鍵在於？", "options": ["顧客願意使用且能從中獲益", "完全取代員工", "技術越複雜越好", "強迫顧客使用"], "ans": 0, "diff": "簡單", "type": "單選"}
    ],

    "(114上)家庭、社區與環境": [
        # --- 生態系統理論 (必考) ---
        {"q": "Bronfenbrenner 的生態系統理論中，個人直接參與且互動最頻繁的環境（如家庭、學校）稱為？", "options": ["微系統 (Microsystem)", "中系統 (Mesosystem)", "外系統 (Exosystem)", "巨系統 (Macrosystem)"], "ans": 0, "diff": "簡單", "type": "單選"},
        {"q": "Bronfenbrenner 理論中，『時間系統』(Chronosystem) 指的是？", "options": ["個人與環境隨時間推移的變化與歷史背景", "一天24小時", "生理時鐘", "交通時間"], "ans": 0, "diff": "中等", "type": "單選"},
        {"q": "下列何者屬於『巨系統』(Macrosystem)？(多選)", "options": ["社會文化價值觀", "國家法律", "經濟制度", "鄰居的狗"], "ans": [0, 1, 2], "diff": "中等", "type": "多選"},
        {"q": "家庭與社區之間的互動，屬於生態系統的哪一層次？", "options": ["中系統 (Mesosystem)", "微系統", "外系統", "巨系統"], "ans": 0, "diff": "困難", "type": "單選"},
        {"q": "父母的工作場所、社區的醫療資源屬於哪一層？", "options": ["外系統 (Exosystem)", "微系統", "中系統", "巨系統"], "ans": 0, "diff": "困難", "type": "單選"},

        # --- 社區功能與類型 ---
        {"q": "社區的『社會控制』功能主要目的是？", "options": ["維持社區秩序與規範", "控制居民的思想", "限制居民的自由", "分配物資"], "ans": 0, "diff": "簡單", "type": "單選"},
        {"q": "『功能性社區』是指？", "options": ["基於共同興趣、職業或目標而形成的群體 (如學術社群)", "住在同一個里的人", "行政劃分的社區", "有功能的建築物"], "ans": 0, "diff": "中等", "type": "單選"},
        {"q": "關於『社區意識』(Sense of Community) 的要素，不包含？", "options": ["排他性", "成員感", "影響力", "整合與滿足需求"], "ans": 0, "diff": "困難", "type": "單選"},
        {"q": "下列何者屬於社區的『生產-分配-消費』功能？", "options": ["鄰居互相幫忙照顧小孩", "社區舉辦中秋晚會", "社區內的便利商店提供生活物資販售", "制定社區公約"], "ans": 2, "diff": "中等", "type": "單選"},

        # --- 環境與永續 ---
        {"q": "『地方依附』(Place Attachment) 包含哪兩個面向？", "options": ["地方認同與地方依賴", "地方稅與地方建設", "地方政府與地方派系", "房價與地段"], "ans": 0, "diff": "困難", "type": "單選"},
        {"q": "環境正義 (Environmental Justice) 強調？", "options": ["所有人不分種族階級，應公平享有環境資源並分擔環境風險", "有錢人可以享受好環境", "工廠應該蓋在窮人區", "環境保護不重要"], "ans": 0, "diff": "簡單", "type": "單選"},
        {"q": "聯合國 SDGs 目標11 是？", "options": ["永續城市與社區", "消除貧窮", "優質教育", "性別平等"], "ans": 0, "diff": "中等", "type": "單選"},
        {"q": "『鄰避效應』(NIMBY) 通常是指社區居民對於哪類設施的抗拒？", "options": ["公園綠地", "嫌惡設施（如垃圾場、變電所）", "圖書館", "便利商店"], "ans": 1, "diff": "簡單", "type": "單選"},

        # --- 家庭與資源 ---
        {"q": "家庭資源管理中，『決策』的三個步驟通常是？", "options": ["確認問題 → 尋求方案 → 執行與評估", "執行 → 後悔 → 放棄", "詢問鄰居 → 照做 → 抱怨", "以上皆非"], "ans": 0, "diff": "簡單", "type": "單選"},
        {"q": "『社會資本』(Social Capital) 在社區中通常表現為？", "options": ["信任、互惠規範與網絡", "銀行的存款", "公共設施的數量", "政府的補助款"], "ans": 0, "diff": "中等", "type": "單選"},
        {"q": "高齡友善環境的『通用的設計』(Universal Design) 精神是？", "options": ["讓所有人(含身障、長者)都能方便使用的設計", "專為身障者設計", "專為兒童設計", "外觀好看最重要"], "ans": 0, "diff": "簡單", "type": "單選"}
    ],

    "(114上)生態旅遊": [
        # --- 核心定義與原則 ---
        {"q": "根據國際生態旅遊協會(TIES)定義，生態旅遊的核心精神包含哪些？(多選)", "options": ["對自然環境負責任", "保障當地居民福祉", "具有解說與教育意義", "以獲取最大商業利潤為首要目標"], "ans": 0, "diff": "中等", "type": "多選"},
        {"q": "下列何者『不是』生態旅遊的特質？", "options": ["大量消費與奢華享受", "小規模", "低衝擊", "社區參與"], "ans": 0, "diff": "簡單", "type": "單選"},
        {"q": "『硬式生態旅遊』(Hard Ecotourism) 的特徵是？", "options": ["需要較強的體能，強調深度體驗與環境倫理", "住豪華飯店", "以購物為主", "搭遊覽車走馬看花"], "ans": 0, "diff": "中等", "type": "單選"},
        {"q": "IUCN 定義的保護區分類中，等級最嚴格（除了科學研究外禁止進入）的是？", "options": ["Ia 嚴格自然保留區", "II 國家公園", "IV 棲地/物種管理區", "V 地景保護區"], "ans": 0, "diff": "困難", "type": "單選"},
        
        # --- 營運與衝擊 ---
        {"q": "『經濟漏損』(Economic Leakage) 在旅遊業中是指？", "options": ["觀光收益流向境外（如外資飯店），當地人未受益", "遊客掉錢", "政府稅收減少", "飯店漏水"], "ans": 0, "diff": "中等", "type": "單選"},
        {"q": "生態旅遊的『乘數效應』(Multiplier Effect) 是希望能？", "options": ["讓旅遊收入在當地經濟體系中循環，創造更多價值", "增加遊客人數", "增加垃圾量", "增加碳排放"], "ans": 0, "diff": "中等", "type": "單選"},
        {"q": "下列何者屬於生態旅遊的『社會文化衝擊』？(多選)", "options": ["傳統文化的商品化", "示範效果導致當地人模仿遊客行為", "增加當地自豪感", "造成物價上漲"], "ans": [0, 1, 2, 3], "diff": "中等", "type": "多選"},
        {"q": "『漂綠』(Greenwashing) 是指？", "options": ["企業誇大其環保作為，誤導消費者", "在牆壁漆上綠色", "多種樹", "使用綠能"], "ans": 0, "diff": "簡單", "type": "單選"},

        # --- 規劃與管理 ---
        {"q": "『環境承載量』(Carrying Capacity) 是指？", "options": ["遊覽車的最大載客數", "環境能承受人類活動干擾而不發生不可逆破壞的最大限度", "遊客願意支付的最高金額", "飯店的最大容納人數"], "ans": 1, "diff": "簡單", "type": "單選"},
        {"q": "在遊憩資源管理中，『LAC』(可接受改變限度) 的核心步驟不包含？", "options": ["無限制開放遊客進入", "選擇關注的指標", "設定標準", "監測與評估"], "ans": 0, "diff": "困難", "type": "單選"},
        {"q": "解說規劃中，『主題』(Theme) 應該要是？", "options": ["一個完整的句子或概念，而非僅是話題", "一個單字", "一個問題", "一張圖片"], "ans": 0, "diff": "中等", "type": "單選"},
        {"q": "下列何者是『非消耗性』的生態旅遊活動？", "options": ["賞鳥", "打獵", "採集植物標本", "釣魚"], "ans": 0, "diff": "簡單", "type": "單選"},
        {"q": "無痕山林 (LNT) 運動的七大準則包括？(多選)", "options": ["事前充分規劃與準備", "在可承受的地點行走與宿營", "適當處理垃圾維護環境", "保持環境原有的風貌", "減低用火對環境的衝擊", "尊重野生動植物", "考量其他使用者"], "ans": [0, 1, 2, 3, 4, 5, 6], "diff": "困難", "type": "多選"},
        {"q": "『遊憩機會序列』(ROS) 的管理概念是為了？", "options": ["提供多樣化的遊憩體驗以滿足不同遊客", "限制所有遊客只能去同一區", "將所有區域開發成遊樂園", "完全禁止進入"], "ans": 0, "diff": "困難", "type": "單選"},
        {"q": "社區參與生態旅遊的『階梯理論』中，最高層次是？", "options": ["公民控制 (Citizen Control)", "告知", "諮詢", "安撫"], "ans": 0, "diff": "困難", "type": "單選"}
    ],

    "(114上)婚姻與家人關係": [
        # --- 擇偶與愛情 ---
        {"q": "Sternberg 的『愛情三角理論』包含哪三個元素？", "options": ["金錢、時間、體力", "親密(Intimacy)、激情(Passion)、承諾(Commitment)", "溝通、妥協、接納", "外貌、個性、背景"], "ans": 1, "diff": "簡單", "type": "單選"},
        {"q": "『過濾理論』(Filter Theory) 認為擇偶的第一個過濾網通常是？", "options": ["社會學因素 (居住地、社會階級)", "心理特質", "價值觀", "互補需求"], "ans": 0, "diff": "中等", "type": "單選"},
        {"q": "在愛情風格理論 (Lee) 中，『遊戲之愛』(Ludus) 的特徵是？", "options": ["視愛情為遊戲，不輕易許下承諾", "強烈的佔有慾", "無私的奉獻", "基於理性的選擇"], "ans": 0, "diff": "簡單", "type": "單選"},
        {"q": "Sternberg 愛情三角中，『圓滿之愛』(Consummate Love) 具備？", "options": ["親密 + 激情 + 承諾", "親密 + 激情", "激情 + 承諾", "親密 + 承諾"], "ans": 0, "diff": "簡單", "type": "單選"},
        
        # --- 婚姻與家庭動力 ---
        {"q": "Satir (薩提爾) 提出的溝通姿態中，『指責型』的人通常忽略了什麼？", "options": ["自我", "他人", "情境", "所有一切"], "ans": 1, "diff": "中等", "type": "單選"},
        {"q": "Gottman 提出的『婚姻殺手』(末日四騎士) 不包含？", "options": ["誠實", "批評", "蔑視", "辯解/防衛"], "ans": 0, "diff": "簡單", "type": "單選"},
        {"q": "『空殼婚姻』(Empty Shell Marriage) 是指？", "options": ["夫妻缺乏感情與互動，僅維持法律上的名義", "夫妻分居", "沒有小孩的婚姻", "沒有房子的婚姻"], "ans": 0, "diff": "中等", "type": "單選"},
        {"q": "家庭系統理論認為，家庭是一個『恆定系統』，意味著？", "options": ["家庭傾向維持穩定與平衡，抗拒改變", "家庭永遠不變", "家庭成員都一樣", "家庭不需要溝通"], "ans": 0, "diff": "困難", "type": "單選"},
        {"q": "依據家庭生命週期，婚姻滿意度通常呈現什麼形狀的變化？", "options": ["U型 (新婚高，育兒期降，空巢期回升)", "倒U型 (育兒期最高)", "直線上升", "直線下降"], "ans": 0, "diff": "中等", "type": "單選"},

        # --- 壓力與危機 ---
        {"q": "家庭壓力 ABC-X 模型中，決定危機是否產生的關鍵因素『C』是指？", "options": ["家庭對壓力事件的認知與界定", "壓力事件本身", "家庭擁有的資源", "危機的結果"], "ans": 0, "diff": "困難", "type": "單選"},
        {"q": "雙重 ABC-X 模型 (Double ABC-X) 中，強調的是？", "options": ["家庭壓力的『累積』與『長期適應』過程", "單一事件的衝擊", "婚前協議的重要性", "離婚的法律程序"], "ans": 0, "diff": "困難", "type": "單選"},
        {"q": "『家庭韌性』(Family Resilience) 的關鍵歷程包含？(多選)", "options": ["共同的信仰系統", "組織模式 (彈性、連結)", "溝通與解決問題", "互相指責"], "ans": [0, 1, 2], "diff": "中等", "type": "多選"},
        {"q": "離婚對兒童的影響中，『雙親衝突』通常比『離婚本身』？", "options": ["更具殺傷力", "影響較小", "沒有差別", "反而有益"], "ans": 0, "diff": "中等", "type": "單選"},
        
        # --- 代間關係 ---
        {"q": "『三明治世代』(Sandwich Generation) 是指哪一群人？", "options": ["喜歡吃三明治的人", "同時要照顧年邁父母與未成年子女的中年人", "夾在兩位主管之間的員工", "在學校與補習班之間奔波的學生"], "ans": 1, "diff": "簡單", "type": "單選"},
        {"q": "成年子女照顧年邁父母的壓力，常被稱為？", "options": ["照顧者負荷 (Caregiver Burden)", "甜蜜的負擔", "孝道的表現", "代溝"], "ans": 0, "diff": "簡單", "type": "單選"},
        {"q": "『代間傳遞』(Intergenerational Transmission) 最常見於？", "options": ["教養方式、價值觀或暴力行為的複製", "財產繼承", "遺傳病", "長相"], "ans": 0, "diff": "簡單", "type": "單選"}
    ],

    "(114上)個人行銷與形象管理": [
        # --- 形象與心理 ---
        {"q": "根據 Albert Mehrabian 的法則，在第一印象中，視覺外表(非語言)佔了多少比例？", "options": ["7%", "38%", "55%", "90%"], "ans": 2, "diff": "中等", "type": "單選"},
        {"q": "『月暈效應』(Halo Effect) 在形象管理中是指？", "options": ["因某一個突出的優點，而讓人誤以為此人樣樣都好", "月亮的光暈", "模糊不清的印象", "因為缺點而否定全部"], "ans": 0, "diff": "中等", "type": "單選"},
        {"q": "印象管理 (Impression Management) 的『防衛性策略』是用來？", "options": ["挽救受損的形象 (如道歉、找藉口)", "提升形象", "攻擊對手", "行銷產品"], "ans": 0, "diff": "中等", "type": "單選"},
        {"q": "在色彩心理學中，『紅色』通常給人什麼感覺？", "options": ["熱情、能量、危險", "冷靜、專業", "自然、放鬆", "神秘、高貴"], "ans": 0, "diff": "簡單", "type": "單選"},
        {"q": "Johari Window (喬哈里窗) 中，『自己不知道，別人卻知道』的區域是？", "options": ["盲目區 (Blind Spot)", "開放區 (Open Area)", "隱藏區 (Hidden Area)", "未知區 (Unknown Area)"], "ans": 0, "diff": "中等", "type": "單選"},

        # --- 行銷工具與策略 ---
        {"q": "進行個人行銷時，SWOT分析中的『O』代表什麼？", "options": ["優勢 (Strengths)", "劣勢 (Weaknesses)", "機會 (Opportunities)", "威脅 (Threats)"], "ans": 2, "diff": "簡單", "type": "單選"},
        {"q": "個人品牌的『原型』(Archetype) 理論，源自於哪位心理學家？", "options": ["榮格 (Carl Jung)", "佛洛伊德", "阿德勒", "皮亞傑"], "ans": 0, "diff": "困難", "type": "單選"},
        {"q": "進行『電梯簡報』時，最常見的架構是？", "options": ["我是誰 → 我做什麼 → 我能為你創造什麼價值 → 呼籲行動", "家庭背景 → 學歷 → 興趣", "抱怨現狀 → 批評他人", "沈默"], "ans": 0, "diff": "簡單", "type": "單選"},
        {"q": "在網路個人行銷中，『內容策展』(Content Curation) 是指？", "options": ["蒐集、整理並分享有價值的資訊，建立專業形象", "只發自拍照", "轉貼假新聞", "隨意洗版"], "ans": 0, "diff": "中等", "type": "單選"},
        {"q": "USP (Unique Selling Proposition) 的中文意思是？", "options": ["獨特銷售主張 (核心競爭力)", "通用銷售計畫", "聯合服務平台", "使用者標準程序"], "ans": 0, "diff": "簡單", "type": "單選"},

        # --- 禮儀與溝通 ---
        {"q": "形象管理的『T.P.O.』原則是指穿著要考慮哪三點？(多選)", "options": ["時間 (Time)", "地點 (Place)", "場合/目的 (Occasion)", "價格 (Price)"], "ans": [0, 1, 2], "diff": "中等", "type": "多選"},
        {"q": "關於『坐姿禮儀』，男士穿西裝時，坐下前應該？", "options": ["解開西裝外套的扣子", "扣上所有扣子", "脫掉外套", "捲起袖子"], "ans": 0, "diff": "中等", "type": "單選"},
        {"q": "交換名片時，若收到對方的名片，應該？", "options": ["雙手接過，仔細閱讀並妥善收好", "直接放口袋", "拿在手上玩", "當場寫字在上面"], "ans": 0, "diff": "簡單", "type": "單選"},
        {"q": "有效的『傾聽』技巧不包含？", "options": ["急著打斷對方發表意見", "眼神接觸", "適時點頭", "複述對方重點"], "ans": 0, "diff": "簡單", "type": "單選"},
        {"q": "『鏡像效應』(Mirroring) 在溝通中是指？", "options": ["模仿對方的肢體語言或語氣，以建立親和感", "照鏡子", "模仿對方的缺點", "完全不理對方"], "ans": 0, "diff": "中等", "type": "單選"},
        {"q": "在商務介紹禮儀中，下列順序何者正確？", "options": ["將職位低者介紹給職位高者", "將女性介紹給男性", "將長輩介紹給晚輩", "將客人介紹給自己公司的人"], "ans": 0, "diff": "困難", "type": "單選"}
    ]
}

# ==========================================
# 2. APP 邏輯 (V3.1 穩定修正版)
# ==========================================
def reset_exam():
    """當使用者改變設定時，強制重置考試狀態"""
    st.session_state.exam_started = False
    st.session_state.current_questions = []
    st.session_state.exam_results = {}
    st.session_state.user_answers = {}
    st.session_state.exam_finished = False # <--- 關鍵修復：這裡必須重置為 False

def main():
    st.set_page_config(page_title="空大期末考衝刺", page_icon="📝")
    
    # 初始化 Session State
    if 'exam_started' not in st.session_state:
        st.session_state.exam_started = False
    if 'current_questions' not in st.session_state:
        st.session_state.current_questions = []
    if 'exam_results' not in st.session_state:
        st.session_state.exam_results = {}
    if 'exam_finished' not in st.session_state:
        st.session_state.exam_finished = False

    # 側邊欄：設定考試參數 (加入 on_change 監聽)
    st.sidebar.title("⚙️ 考試設定")
    selected_subject = st.sidebar.selectbox(
        "1. 選擇科目", 
        list(QUESTION_DB.keys()),
        on_change=reset_exam
    )
    
    difficulty = st.sidebar.radio(
        "2. 選擇難度", 
        ["簡單", "中等", "困難"], 
        index=1,
        on_change=reset_exam
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
            # 確保狀態乾淨
            st.session_state.exam_finished = False 
            st.session_state.exam_results = {} 

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
        # 增加保護：只有當 result 有資料且 finished 為 True 時才顯示
        if st.session_state.get("exam_finished") and st.session_state.exam_results:
            res = st.session_state.exam_results
            if res['total'] > 0:
                final_score = int((res['score'] / res['total']) * 100)
            else:
                final_score = 0
            
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
                st.session_state.exam_results = {}
                st.rerun()

if __name__ == "__main__":
    main()
