---
name: seo-audit
description: Run SEO audits on websites — page speed analysis, on-page checklist, keyword research, and generate structured reports. Connects to Google PageSpeed Insights API via Python CLI.
---

# Purpose
Kiểm tra và đánh giá SEO của một website — từ tốc độ tải trang đến on-page optimization — rồi xuất báo cáo có thể gửi cho khách hàng.

# When to use
- "Kiểm tra SEO website X"
- "Chạy audit cho trang landing page"
- "Tốc độ tải trang của mình như thế nào?"
- "Tạo báo cáo SEO cho khách hàng"
- "Kiểm tra Core Web Vitals"

# Inputs needed
- URL cần kiểm tra
- Loại thiết bị (mobile / desktop)
- Từ khóa mục tiêu (tùy chọn)

# Workflow

1. **Run PageSpeed audit** — Gọi Google PageSpeed Insights API lấy điểm và metrics
2. **Check on-page elements** — H1, meta description, alt text, internal links
3. **Analyze keywords** — Từ khóa mục tiêu có xuất hiện đúng chỗ không?
4. **Generate report** — Điền vào template `templates/report-template.md`
5. **Save output** — Lưu kết quả vào `outputs/`

# External connection
Script `scripts/pagespeed-check.py` gọi **Google PageSpeed Insights API** (miễn phí, không cần auth).

```bash
# Chạy audit trực tiếp từ terminal
python .claude/skills/seo-audit/scripts/pagespeed-check.py --url https://example.com

# Chạy cả mobile và desktop
python .claude/skills/seo-audit/scripts/pagespeed-check.py --url https://example.com --strategy both

# Lưu kết quả ra file
python .claude/skills/seo-audit/scripts/pagespeed-check.py --url https://example.com --output .claude/skills/seo-audit/outputs/
```

# Output format

Dùng template `templates/report-template.md` để điền kết quả.
Lưu báo cáo cuối vào `outputs/audit-[domain]-[date].md`.

```md
# SEO Audit Report: [Domain]
**Ngày**: [Date]
**Người thực hiện**: [Tên]

## Điểm PageSpeed
- Mobile: [X]/100
- Desktop: [X]/100

## Core Web Vitals
- LCP: [X]s (target < 2.5s)
- FID: [X]ms (target < 100ms)
- CLS: [X] (target < 0.1)

## Khuyến nghị ưu tiên
1. [Vấn đề nghiêm trọng nhất]
2. [...]
```

# Files trong folder này
```
seo-audit/
├── seo-audit.md          ← File skill này
├── scripts/
│   └── pagespeed-check.py  ← Script chạy audit (kết nối API ngoài)
├── templates/
│   ├── audit-checklist.md  ← Checklist on-page SEO
│   └── report-template.md  ← Template báo cáo
└── outputs/               ← Kết quả audit được lưu tại đây
```

# Best practices
- Luôn test cả mobile và desktop — Google index mobile-first
- LCP > 4s = cần fix ngay, ảnh hưởng ranking trực tiếp
- Báo cáo cho khách: chỉ giữ top 5 vấn đề quan trọng nhất, không list hết
- Chạy audit trước và sau khi optimize để so sánh
