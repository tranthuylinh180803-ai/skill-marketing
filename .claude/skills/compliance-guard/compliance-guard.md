---
name: compliance-guard
description: Kiểm tra content affiliate trước khi đăng — phát hiện spam signals, link risks, AI-content markers; tính shadowban risk score; rewrite nếu cần
metadata:
  type: skill
  platforms: [facebook, threads]
  layer: protection
---

# Compliance Guard

## Purpose
Checkpoint cuối cùng trước khi đăng bài. Quét content để phát hiện các yếu tố có thể gây giảm reach tự nhiên, shadowban, hoặc bị giới hạn phân phối. Một bài viết hay bị spam-flagged = công sức bằng không.

**Nguyên tắc:** Platform algorithms không ghét affiliate — họ ghét behavior pattern trông giống spam. Mục tiêu là viết content trông như người thật, không như bot.

## When to use
- Trước MỌI bài đăng có link affiliate
- Khi thấy reach đột ngột giảm không rõ lý do (chẩn đoán nguyên nhân)
- Khi muốn review toàn bộ content calendar trước khi lên lịch

**Trigger phrases:** "kiểm tra bài trước đăng", "compliance check", "có bị shadowban không", "bài có an toàn không", "check spam", "review trước khi đăng"

## Inputs needed
1. Bài đăng hoàn chỉnh (paste text + link nếu có)
2. Nền tảng: Facebook hay Threads?

## Workflow

### Bước 1 — CTA Spam Scan

Kiểm tra và trừ điểm nếu có:

| Red Flag | Điểm trừ | Lý do |
|----------|----------|-------|
| "Click ngay" / "Mua ngay" | -2 | Trigger spam filter |
| "Đừng bỏ lỡ" / "Cơ hội cuối cùng" | -2 | Fake urgency pattern |
| CTA lặp > 2 lần trong bài | -3 | Spam behavior |
| Yêu cầu tag/share ép buộc | -2 | Engagement bait (vi phạm policy) |
| Urgency giả không có bằng chứng | -2 | Misleading (vd: "Chỉ còn X suất" mà không có proof) |
| Từ "miễn phí" + link affiliate | -1 | Misleading về offer |

### Bước 2 — Link Hygiene Check

**Facebook:**
| Link Pattern | Risk Level | Điểm trừ | Đề xuất |
|-------------|-----------|----------|---------|
| Link thẳng trong caption | HIGH | -3 | Chuyển sang comment đầu tiên |
| Nhiều hơn 1 link trong post | HIGH | -3 | Chỉ giữ 1 link, để comment |
| Affiliate link lộ tracking param | MEDIUM | -2 | Dùng link rút gọn đáng tin |
| Link rút gọn không rõ nguồn | MEDIUM | -1 | Dùng tên domain rõ ràng |
| Link ở bio, caption chỉ nhắc tên | LOW | 0 | Tốt — cách an toàn nhất |

**Threads:**
| Link Pattern | Risk Level | Điểm trừ |
|-------------|-----------|----------|
| Link trong thread | MEDIUM | -1 |
| Nhiều link trong 1 thread | HIGH | -2 |
| Link ở bio, thread nhắc "link bio" | LOW | 0 |

### Bước 3 — AI-Content Detection

**Structural markers — phát hiện bằng cách đọc:**

| Dấu hiệu | Điểm trừ | Cách fix |
|---------|----------|---------|
| Tất cả câu đều ~15 chữ | -2 | Mix câu ngắn + dài |
| Cấu trúc "Điểm 1... Điểm 2... Điểm 3..." | -2 | Viết dạng tự nhiên, không liệt kê |
| Mở đầu bằng "Tất nhiên" / "Chắc chắn" / "Đương nhiên" | -1 | Xóa/thay thế |
| Không có chi tiết cụ thể nào (ngày, số, tên) | -2 | Thêm ít nhất 1 chi tiết |
| Không có nhược điểm sản phẩm | -1 | Thêm honest review element |

**Word markers — từ AI hay dùng quá mức:**
Mỗi từ dưới đây trong bài → trừ 1 điểm (tối đa -3 điểm cho mục này):
```
tuyệt vời, hiệu quả vượt trội, đột phá, thần kỳ, bí quyết,
không thể tin được, kết quả ngoài mong đợi, trải nghiệm tuyệt vời,
hoàn toàn miễn phí, 100% tự nhiên, được chứng minh khoa học,
cơ hội vàng, ưu đãi đặc biệt, hiếm có
```

**Humanizing elements — cộng điểm:**
| Element | Điểm cộng |
|---------|-----------|
| Có chi tiết cụ thể (ngày, số, tên, địa điểm) | +1 |
| Nhắc nhược điểm hoặc hạn chế của sản phẩm | +2 |
| Có câu ngắn xen câu dài (độ dài đa dạng) | +1 |
| Có ngôn ngữ đời thường, không hoàn hảo | +1 |
| Có cảm xúc thật (không phải "tôi rất vui") | +1 |

### Bước 4 — Platform-Specific Risk Check

**Facebook:**
| Pattern | Risk | Điểm trừ |
|---------|------|----------|
| Đăng > 3 bài/ngày với link | MEDIUM | -1 |
| Caption giống hệt bài trước đó | HIGH | -3 |
| Hashtag > 5 cái | LOW | -1 |
| Bài quảng cáo rõ ràng không dùng Ad | MEDIUM | -1 |

**Threads:**
| Pattern | Risk | Điểm trừ |
|---------|------|----------|
| Hashtag > 3 cái | LOW | -1 |
| Nội dung quá "polished", thiếu voice tự nhiên | MEDIUM | -1 |
| Thread lặp lại cấu trúc giống bài hôm qua | LOW | -1 |

### Bước 5 — Tính Risk Score

**Công thức:** Risk Score = 10 + (tổng điểm cộng) − (tổng điểm trừ)

**Thang đánh giá:**
| Score | Màu | Đánh giá | Hành động |
|-------|-----|----------|-----------|
| 8–10 | Xanh | An toàn | Đăng được |
| 5–7 | Vàng | Cần chỉnh nhỏ | Sửa theo gợi ý, đăng được |
| 3–4 | Cam | Rủi ro cao | Phải rewrite trước khi đăng |
| 0–2 | Đỏ | Nguy hiểm | Không đăng — viết lại từ đầu |

### Bước 6 — Rewrite Mode (nếu Score ≤ 4)

Liệt kê từng vấn đề cụ thể → đề xuất sửa → output bài clean:

**Format sửa:**
```
Issue: [Mô tả vấn đề cụ thể]
Hiện tại: "[đoạn text cần sửa]"
Đề xuất: "[phiên bản đã sửa]"
Lý do: [tại sao phiên bản mới tốt hơn]
```

## Output format

```
COMPLIANCE REPORT
══════════════════════════════════════
Platform: [Facebook / Threads]
Risk Score: [X/10]
Đánh giá: [An toàn / Cần chỉnh / Rủi ro cao / Nguy hiểm]

Issues tìm thấy:
[✗] [Tên issue] — [mô tả] (−X điểm)
...

Điểm cộng:
[✓] [Element tốt] (+X điểm)
...

Tổng: [+X cộng] − [X trừ] = Score [X/10]

Đề xuất sửa:
1. [Thay đổi cụ thể]
2. [Thay đổi cụ thể]

[Bài đã rewrite — chỉ hiển thị nếu Score ≤ 4]
══════════════════════════════════════
```

## Best practices
- Đây là checkpoint CUỐI — chạy sau `hook-cta-optimizer`, không trước
- Facebook nghiêm hơn Threads về link — mặc định để link ở comment, không caption
- Nhắc nhược điểm sản phẩm = tín hiệu human mạnh nhất + tăng credibility
- Score 7–8 là "đủ tốt" — không cần hoàn hảo, quá "clean" cũng bị nghi là bot
- Khi phát hiện pattern vi phạm lặp lại nhiều lần → lưu vào `data/winning-patterns.md` phần "Patterns Cần Tránh"
- Shadowban thường không thông báo — nếu reach đột ngột giảm 50%+ không rõ lý do, dùng skill này để audit 5–7 bài gần nhất
