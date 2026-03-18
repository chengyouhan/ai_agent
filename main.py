from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv
load_dotenv()


def main():
    llm = ChatOpenAI(model="gemma3:27b",
    base_url="http://203.71.78.31:8000/v1",
    api_key="sk-12345678",temperature=0.0)
    messages = []
    messages.append(SystemMessage(content="""你是一位精通電腦硬體架構與資料轉換的「資深系統分析師」。你的性格嚴謹、精確，對資料格式有著技術潔癖，能敏銳捕捉非結構化文字中的關鍵規格參數。
將輸入的筆記型電腦產品行銷文案，精準轉換為結構化的 JSON 資料物件。此資料將直接用於電商後台資料庫，因此必須保證語法正確且內容精煉。
標籤推論：識別文中提及的使用情境（如：電競、設計），將其轉換為 target_audience 陣列。
語意轉化：將中文描述的核心數量（如：八核心）轉化為純數字（Integer）。
規格標準化：容量與頻率需保留數值與原始單位（如：16GB, 3.5GHz）。
零冗餘原則：回應中禁止包含任何開場白（如：這是你要的 JSON...）、解釋或結語。僅輸出純 JSON 內容。
必須嚴格遵循以下 JSON 結構：
target_audience: Array of strings.
cpu: Object 包含 cores (Number) 與 max_frequency (String).
ram: Object 包含 capacity (String).
storage: Object 包含 capacity (String) 與 type (String)."""))
    messages.append(HumanMessage(content="""請解析下方提供的產品描述文案。你的目標是根據 System Prompt 定義的規則，提取硬體規格並將其精煉為結構化 JSON。
Targeting: 辨識文中隱含的目標族群並歸類。
Normalization: 執行語意提取（如：將「八核心」轉化為數字 8）。
Consistency: 確保單位（GHz, GB, TB）與數值緊鄰，且格式符合預定義架構。
「這款針對電競玩家與內容創作者設計的高性能筆電，核心運算單元採用八核心架構，其最高運作頻率可達 3.5GHz，在效能與功耗之間取得平衡。系統記憶體總容量為 16GB，可支援高強度多工處理與大型遊戲執行。儲存部分則配置一顆 1TB 容量的 NVMe 規格固態硬碟，相較於傳統 SATA SSD 具備更快的資料傳輸效率與更低的延遲表現。」
請僅輸出符合格式要求的 JSON 物件，不需解釋過程。"""))

prompt ="""你是一位精通硬體架構的 「資深系統分析師」，擅長將冗長的產品文案精煉為結構化的技術規格（Tech Specs），並對資料處理有著嚴謹的潔癖。
我們正在為電商平台建立自動化產品資料庫。目前收到了一段關於高效能筆記型電腦的行銷描述，我們需要將這些文字中的關鍵硬體參數（如 CPU、RAM、Storage）提取出來，以便系統後台讀取。
專業、簡潔、技術導向。不需要任何贅字或開場白。
請閱讀提供的產品文案，並嚴格遵循以下規則轉換為 JSON 物件：
這款針對電競玩家與內容創作者設計的高性能筆電，
核心運算單元採用八核心架構，其最高運作頻率可達 3.5GHz，
在效能與功耗之間取得平衡。
系統記憶體總容量為 16GB，可支援高強度多工處理與大型遊戲執行。
儲存部分則配置一顆 1TB 容量的 NVMe 規格固態硬碟，
相較於傳統 SATA SSD 具備更快的資料傳輸效率與更低的延遲表現。
數值化：將容量（如 16GB）與頻率（如 3.5GHz）盡量拆分為數值與單位。
語意提取：將「八核心」轉換為數值 8。
推論：將產品定位（電競、創作者）歸類為目標族群。
輸入文字： 「這台電腦搭載四核心處理器，時脈 2.4GHz，擁有 8GB 記憶體與 512GB SSD。」
輸出 JSON：

JSON

{

"processor": {

"cores": 4,

"max_clock_speed": "2.4GHz"

},

"memory": {

"total_capacity": "8GB"

},

"storage": {

"capacity": "512GB",

"interface": "SSD"

}

}

請以此 JSON 格式輸出：
target_audience: 清單形式 (Array)
cpu: 包含 cores (Number) 與 max_frequency (String)
ram: capacity (String)
storage: 包含 capacity (String) 與 type (String)"""

    for chunk in llm.stream(prompt):
        print(chunk.content, end="", flush=True)
    # response = llm.invoke(query)

    # print(response)
    # print(response.content)

if __name__ == "__main__":
    main()
