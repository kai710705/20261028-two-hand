# 20261028-two-hand｜雙手手勢圖片播放器

以 Flask 提供頁面、MediaPipe Tasks Vision 在瀏覽器端執行手勢辨識的互動圖片播放器。影像只在使用者瀏覽器處理，不會上傳或保存至伺服器。

## 功能

- 攝影機畫面與雙手骨架線條。
- 手掌左移／右移切換圖片；食指跳至第一張；小指跳至最後一張。
- 手心／手背翻轉圖片鏡像；單獨比讚切換黑白負片。
- 雙手食指交叉成 X，播放疾風能量動畫。
- 雙手合掌，逐字呈現墨跡詩句，接續重力封印動畫。
- 五張 SVG 展示圖片與按鈕輔助控制。

## 專案結構

```text
main.py                 Flask 入口、首頁與健康檢查
templates/index.html    使用者介面
static/app.js           MediaPipe 與手勢互動邏輯
static/style.css        介面與動畫樣式
static/images/          五張本機 SVG 展示圖片
requirements.txt        Render pip 安裝清單
render.yaml             Render Blueprint 設定
```

## 本機啟動

```powershell
uv sync --locked
uv run main.py
```

本機預設使用自簽 HTTPS，請開啟 `https://localhost:5000` 或
`https://<區網-IP>:5000`。瀏覽器首次會要求確認本機憑證，允許攝影機後即可使用。

若只檢查一般畫面、無須攝影機，可使用：

```powershell
$env:LOCAL_HTTPS = "false"
uv run main.py
```

## Render 部署

1. 將此資料夾推送至 GitHub。
2. 在 Render 建立 **Blueprint**，選取此儲存庫。
3. Render 讀取 `render.yaml`，執行 `pip install -r requirements.txt` 及 `gunicorn --bind 0.0.0.0:$PORT main:app`。
4. 部署完成後，以 Render 的 `https://...onrender.com` 網址使用攝影機。

`GET /health` 可作為 Render health check。Render 在反向代理層處理 HTTPS，因此不會使用本機的自簽憑證。

## 相依套件

`requirements.txt` 由 `uv.lock` 匯出。前端 MediaPipe Tasks Vision 透過 CDN 載入，不需要在 Render 安裝 Python MediaPipe。
