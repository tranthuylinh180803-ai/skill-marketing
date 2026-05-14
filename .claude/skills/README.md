# Marketing AI Agent — Bảng điều khiển

---

## AGENTS (Invoke bằng /<tên>)

| # | Tên | Invoke | Làm gì | Tần suất |
|---|-----|--------|--------|----------|
| **A1** | **research-strategist** | `/research-strategist` | Đánh giá sản phẩm → nghiên cứu audience kênh → tìm lifestyle keyword → chiến lược 70/30 | 1 lần/tháng |
| **A2** | **content-creator** | `/content-creator` | Phân loại TYPE A/B → viết bài → tối ưu hook/CTA → check compliance → log metric | Hàng ngày |

**Quy trình chuẩn:**
```
[A1] research-strategist  ──→  research-brief.md  ──→  [A2] content-creator  ──→  bài đăng
       (tháng 1 lần)              (handoff)                  (ngày nào cũng dùng)
```

---

## SKILLS (A1 sử dụng)

| # | Tên | Nhiệm vụ trong A1 |
|---|-----|------------------|
| S1 | **product-marketing-context** | Đánh giá sản phẩm theo 4 tiêu chí (Step 1) |
| S2 | **affiliate-audience-research** | Research audience của kênh — không phải buyer của sản phẩm (Step 2) |
| S3 | **seo-audit** | Tìm lifestyle keyword theo TOFU/MOFU/BOFU (Step 3) |
| S4 | **affiliate-content-strategist** | Lên chiến lược 70% trust / 30% affiliate + 7-day calendar (Step 4) |
| S5 | **data** *(winning-patterns + memory)* | Filter proven patterns, check repeat-buy potential (Step 5) |

---

## SKILLS (A2 sử dụng)

| # | Tên | Nhiệm vụ trong A2 |
|---|-----|------------------|
| S6 | **creative-angle-system** | Chọn angle đúng TYPE (A hoặc B), tránh lặp (Step 2) |
| S7 | **affiliate-post-writer** | Viết bài theo TYPE: A = không link, B = link sau context (Step 3) |
| S8 | **hook-cta-optimizer** | Hook TYPE A = gây tò mò / TYPE B = surprise giá hoặc kết quả (Step 4) |
| S9 | **compliance-guard** | Platform check + Amazon ToS check (chỉ bắt buộc TYPE B) (Step 5) |
| S10 | **content-performance-tracker** | Log riêng: TYPE A → save/share rate / TYPE B → click/commission (Step 6) |
| S11 | **social-content** | Adapt content sang platform khác nếu cần (Step 7, tùy chọn) |

---

## SKILLS ĐỘC LẬP (invoke trực tiếp, không qua agent)

| # | Tên | Invoke | Dùng khi nào |
|---|-----|--------|-------------|
| S12 | **sales-enablement** | `/sales-enablement` | Cần battlecard, objection handling, pitch deck |
| S13 | **video** | `/video` | Cần script, shot list, AI video prompt |
| S14 | **image** | `/image` | Cần AI image prompt, creative brief |
| S15 | **referral-affiliate** | `/referral-affiliate` | Thiết kế chương trình referral hoặc affiliate |
| S16 | **social-api-connect** | `/social-api-connect` | Kết nối Facebook API, GA4, TikTok API |
| S17 | **seo-audit** | `/seo-audit` | Audit SEO kỹ thuật (dùng độc lập, khác với S3) |

---

## DATA LAYER (bộ nhớ chung — mọi agent đều đọc)

| File | Cập nhật bởi | Đọc bởi |
|------|-------------|---------|
| `data/winning-patterns.md` | content-performance-tracker (S10) | A1 Step 5, A2 Step 2 |
| `data/performance-memory.json` | content-performance-tracker (S10) | A1 Step 5, A2 Step 2 |

---

## SƠ ĐỒ ĐẦY ĐỦ

```
┌─────────────────────────────────────────────────────────────────┐
│  AGENT A1 — research-strategist                                 │
│                                                                 │
│  S1 product-marketing-context  →  đánh giá 4 tiêu chí          │
│  S2 affiliate-audience-research →  nghiên cứu kênh, không sp   │
│  S3 seo-audit                  →  lifestyle keyword             │
│  S4 affiliate-content-strategist → chiến lược 70/30            │
│  S5 data                       →  filter patterns              │
│                          ↓                                      │
│                   research-brief.md                             │
└──────────────────────┬──────────────────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────────────────┐
│  AGENT A2 — content-creator                                     │
│                                                                 │
│  Step 1: xác định TYPE A (xây kênh) hoặc TYPE B (bán hàng)     │
│                                                                 │
│  S6 creative-angle-system  →  chọn angle đúng TYPE             │
│  S7 affiliate-post-writer  →  viết theo format TYPE            │
│  S8 hook-cta-optimizer     →  hook + CTA đúng TYPE             │
│  S9 compliance-guard       →  check (bắt buộc TYPE B)          │
│  S10 content-performance-tracker → log metric theo TYPE        │
│  S11 social-content        →  adapt platform (tùy chọn)        │
│                          ↓                                      │
│    TYPE A: bài không link (KPI: save/share/follow)              │
│    TYPE B: bài có link Amazon (KPI: click/commission)           │
└─────────────────────────────────────────────────────────────────┘

DATA LAYER (shared):  data/winning-patterns.md
                      data/performance-memory.json
```

---

## BẢNG TỈ LỆ & TẦN SUẤT

| Loại | Tỉ lệ | Ví dụ nếu đăng 10 bài/tháng |
|------|-------|------------------------------|
| TYPE A — Xây kênh | 70% | 7 bài: tips, story, tutorial, opinion |
| TYPE B — Bán hàng | 30% | 3 bài: review, haul, case study có link |

---

## QUICK START

**Lần đầu tiên:**
1. `/research-strategist` → trả lời câu hỏi về kênh + sản phẩm
2. `/content-creator` → chọn TYPE → viết bài hôm nay

**Hàng ngày:**
- `/content-creator` (đọc brief tự động, hỏi TYPE hoặc tự chọn theo tỉ lệ)

**Đầu tháng:**
- `/research-strategist` để refresh chiến lược, đánh giá sản phẩm mới

**Sau 2 tuần:**
- `/content-creator` → yêu cầu "báo cáo 2 tuần" → xem TYPE nào đang work tốt hơn
