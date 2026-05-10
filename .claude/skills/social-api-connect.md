---
name: social-api-connect
description: Connect to external marketing APIs — Facebook Graph API, Google Analytics 4, and TikTok API — to fetch insights, post content, and automate reporting via CLI and Python.
---

# Purpose
Kết nối trực tiếp với các nền tảng marketing bên ngoài qua API để lấy dữ liệu thật, đăng nội dung tự động, và tạo báo cáo — không cần đăng nhập thủ công.

# When to use
- "Lấy insights từ Facebook Page của tôi"
- "Xem số liệu Google Analytics hôm nay"
- "Tự động đăng bài lên Facebook"
- "Lấy dữ liệu TikTok về video của tôi"
- "Kiểm tra tốc độ website bằng API"

# Inputs needed
- Access token / API key của nền tảng cần kết nối
- Page ID / Account ID tương ứng
- Thời gian lấy dữ liệu (ngày bắt đầu, ngày kết thúc)

# External platforms supported

## 1. Google PageSpeed Insights API (Miễn phí, không cần auth)

```bash
# Kiểm tra tốc độ website ngay lập tức
python .claude/skills/seo-audit/scripts/pagespeed-check.py --url https://yourwebsite.com --strategy both

# Hoặc dùng curl trực tiếp
curl "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=https://yourwebsite.com&strategy=mobile"
```

---

## 2. Facebook Graph API

### Bước setup (1 lần duy nhất)
```
1. Vào: developers.facebook.com
2. Tạo app → Chọn "Business"
3. Thêm sản phẩm: "Facebook Login" + "Pages API"
4. Lấy Page Access Token từ Graph API Explorer
5. Lưu token vào biến môi trường:
   $env:FB_ACCESS_TOKEN = "your_token_here"
   $env:FB_PAGE_ID = "your_page_id"
```

### Lấy insights Facebook Page
```bash
# Reach và impressions 7 ngày gần nhất
curl "https://graph.facebook.com/v19.0/$env:FB_PAGE_ID/insights?metric=page_impressions,page_reach,page_engaged_users&period=day&since=$(date -d '7 days ago' +%s)&access_token=$env:FB_ACCESS_TOKEN"
```

```python
# Python version — dễ đọc hơn
import os, urllib.request, json

token = os.environ["FB_ACCESS_TOKEN"]
page_id = os.environ["FB_PAGE_ID"]

url = (f"https://graph.facebook.com/v19.0/{page_id}/insights"
       f"?metric=page_impressions,page_reach,page_engaged_users"
       f"&period=day&access_token={token}")

with urllib.request.urlopen(url) as r:
    data = json.loads(r.read())
    for item in data["data"]:
        print(f"{item['name']}: {item['values'][-1]['value']}")
```

### Đăng bài lên Facebook Page
```python
import os, urllib.request, urllib.parse

token = os.environ["FB_ACCESS_TOKEN"]
page_id = os.environ["FB_PAGE_ID"]
message = "Nội dung bài viết của bạn đây!"

url = f"https://graph.facebook.com/v19.0/{page_id}/feed"
data = urllib.parse.urlencode({"message": message, "access_token": token}).encode()

with urllib.request.urlopen(url, data) as r:
    result = json.loads(r.read())
    print(f"✅ Đã đăng bài: {result['id']}")
```

---

## 3. Google Analytics 4 (GA4)

### Bước setup
```
1. Vào: console.cloud.google.com
2. Tạo Service Account → tải file credentials.json
3. Trong GA4: Admin → Property Access Management → thêm service account email
4. Cài thư viện: pip install google-analytics-data
5. Lưu đường dẫn: $env:GOOGLE_APPLICATION_CREDENTIALS = "path/to/credentials.json"
```

### Lấy sessions và users 7 ngày
```python
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import RunReportRequest, DateRange, Metric, Dimension
import os

client = BetaAnalyticsDataClient()
property_id = "YOUR_GA4_PROPERTY_ID"

request = RunReportRequest(
    property=f"properties/{property_id}",
    date_ranges=[DateRange(start_date="7daysAgo", end_date="today")],
    metrics=[Metric(name="sessions"), Metric(name="activeUsers")],
    dimensions=[Dimension(name="date")]
)

response = client.run_report(request)
for row in response.rows:
    date = row.dimension_values[0].value
    sessions = row.metric_values[0].value
    users = row.metric_values[1].value
    print(f"{date}: {sessions} sessions, {users} users")
```

---

## 4. TikTok API (Research API)

### Bước setup
```
1. Vào: developers.tiktok.com
2. Đăng ký tài khoản developer
3. Tạo app → Lấy client_key và client_secret
4. Dùng OAuth 2.0 để lấy access token
```

```python
# Lấy thông tin video TikTok của bạn
import os, urllib.request, json

token = os.environ["TIKTOK_ACCESS_TOKEN"]
url = "https://open.tiktokapis.com/v2/video/list/"
headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
body = json.dumps({"max_count": 10}).encode()

req = urllib.request.Request(url, data=body, headers=headers)
with urllib.request.urlopen(req) as r:
    data = json.loads(r.read())
    for video in data["data"]["videos"]:
        print(f"{video['title']}: {video['view_count']} views")
```

# Workflow

1. **Chọn platform** cần kết nối
2. **Setup credentials** theo hướng dẫn từng platform ở trên
3. **Lưu credentials** vào biến môi trường (không hardcode vào code)
4. **Chạy script** để lấy dữ liệu
5. **Kết hợp với skill khác** — đưa data vào `social-content` để tạo báo cáo

# Output format

```md
## API Report: [Platform] — [Ngày]

| Metric | Giá trị | So với kỳ trước |
|--------|---------|----------------|
| [Metric 1] | [X] | ▲/▼ [Y]% |
| [Metric 2] | [X] | ▲/▼ [Y]% |

**Insight nổi bật**: [Nhận xét từ data]
**Đề xuất**: [Hành động tiếp theo]
```

# Best practices
- **Không bao giờ** hardcode token/key vào file code — dùng biến môi trường
- Token Facebook hết hạn sau 60 ngày — cần refresh định kỳ
- Rate limit: Facebook cho phép ~200 calls/giờ; Google Analytics không giới hạn cứng
- Lưu response API vào file .json để debug khi cần
- Dùng `.gitignore` để không commit file credentials lên GitHub
