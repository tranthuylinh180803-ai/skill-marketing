---
name: product-marketing-context
description: Foundation skill — collect and store product info, ICP, brand voice, and goals. All other skills read this first before doing anything.
---

# Purpose
Skill nền tảng — thu thập và lưu trữ thông tin sản phẩm, khách hàng mục tiêu và brand. Mọi skill khác gọi skill này trước khi thực hiện bất kỳ tác vụ nào.

# When to use
- Tự động được gọi bởi tất cả skill marketing khác
- "Cập nhật thông tin sản phẩm"
- "Đổi brand voice"
- "Thêm đối thủ cạnh tranh mới"
- Khi bắt đầu dự án mới

# Inputs needed
Không cần — skill này đi thu thập thông tin từ người dùng.

# Workflow

1. **Tìm file context** — Tìm `marketing-context.json` trong thư mục dự án
2. **Nếu có** → đọc và trả về cho skill gọi
3. **Nếu không có** → hỏi người dùng từng câu theo thứ tự dưới đây
4. **Lưu context** → tạo `marketing-context.json`

# Câu hỏi thu thập (hỏi từng câu — không hỏi hàng loạt)

## Nhóm 1: Sản phẩm
- Tên sản phẩm / dịch vụ là gì?
- Nó giải quyết vấn đề gì cho khách hàng?
- Điểm khác biệt so với đối thủ là gì? (USP)
- Giá bán?

## Nhóm 2: Khách hàng mục tiêu (ICP)
- Khách hàng lý tưởng là ai? (độ tuổi, nghề nghiệp, thu nhập)
- Nỗi đau lớn nhất của họ là gì?
- Họ thường mua qua kênh nào?

## Nhóm 3: Brand Voice
- Thương hiệu muốn truyền đạt cảm giác gì?
- Từ ngữ nào KHÔNG dùng?
- Màu sắc thương hiệu? (HEX nếu có)

## Nhóm 4: Mục tiêu
- Mục tiêu marketing hiện tại? (awareness / leads / conversion / retention)
- KPI đo lường thành công?

# Output format

Lưu thành file `marketing-context.json`:

```json
{
  "product": {
    "name": "",
    "category": "",
    "usp": "",
    "price_range": "",
    "key_features": []
  },
  "icp": {
    "demographics": "",
    "pain_points": [],
    "buying_channels": [],
    "language_style": ""
  },
  "brand": {
    "voice": "",
    "tone_keywords": [],
    "avoid_words": [],
    "color_palette": [],
    "example_content_urls": []
  },
  "goals": {
    "current_objective": "",
    "kpis": [],
    "budget": "",
    "timeline": ""
  },
  "competitors": []
}
```

# Best practices
- Hỏi từng câu một, đừng dump cả form cùng lúc
- Nếu người dùng chưa biết một câu nào (ví dụ: LTV), bỏ qua và để trống
- Cập nhật file mỗi khi người dùng nói "đổi sản phẩm" hay "cập nhật ICP"
- Tham chiếu `shared/brand-voice.md` để kiểm tra tone nhất quán
