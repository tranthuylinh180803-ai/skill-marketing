---
name: affiliate-content-strategist
description: Xây dựng chiến lược content affiliate — content pillars, TOFU/MOFU/BOFU mapping, tỉ lệ value/story/sell, định hướng reach/trust/conversion
metadata:
  type: skill
  platforms: [facebook, threads]
  layer: strategy
---

# Affiliate Content Strategist

## Purpose
Xây xương sống chiến lược content trước khi viết bất cứ bài nào. Output của skill này là kim chỉ nam cho tất cả các skill sản xuất content. Không có chiến lược → content hỗn loạn, không có hướng, không biết bài nào phục vụ mục tiêu gì.

**Triết lý:** Mọi bài đăng phải làm được ít nhất 1 trong 3 việc: kéo Attention, xây Trust, hoặc tạo Conversion.

## When to use
- Bắt đầu dự án affiliate mới
- Đổi sản phẩm hoặc target audience
- Review chiến lược định kỳ mỗi tháng
- Khi content không có hướng, không biết viết gì tiếp

**Trigger phrases:** "xây chiến lược content", "lập kế hoạch content affiliate", "content pillars", "TOFU MOFU BOFU", "tỉ lệ content", "định hướng content"

## Inputs needed
Hỏi lần lượt từng câu — không hỏi nhiều câu cùng lúc:
1. Sản phẩm affiliate cụ thể là gì? Giá? Loại sản phẩm (vật lý / khóa học / SaaS / khác)?
2. Trang đang ở giai đoạn nào? (mới dưới 3 tháng / tăng trưởng 3–6 tháng / đã có trust trên 6 tháng)
3. Nền tảng chính: Facebook, Threads, hay cả hai?
4. Mục tiêu ưu tiên tháng này: tăng reach / xây trust / tăng conversion?

Đọc thêm trước khi bắt đầu:
- `marketing-context.json` nếu tồn tại
- `.claude/skills/affiliate-audience-research/outputs/buyer-persona.md` nếu tồn tại
- `data/winning-patterns.md` nếu tồn tại

## Workflow

### Bước 1 — Xây Content Pillars (3–5 pillars)

Mỗi pillar phải:
- Map với 1 pain point thật của ICP
- Phục vụ 1 mục tiêu rõ ràng (reach / trust / convert)
- Có thể viết ít nhất 10 bài khác nhau xoay quanh nó

Template mỗi pillar:
```
Pillar [N]: [Tên ngắn gọn]
Mục tiêu: [reach / trust / convert]
Funnel stage: [TOFU / MOFU / BOFU]
Pain point giải quyết: [mô tả cụ thể]
Dạng bài tiêu biểu:
  - Facebook: [ví dụ cụ thể]
  - Threads: [ví dụ cụ thể]
Hook mẫu: "[câu mở đầu ví dụ cho pillar này]"
Tần suất đề xuất: [X bài/tuần]
```

Ví dụ pillar cho sản phẩm giảm cân:
```
Pillar 1: Sự thật về giảm cân
Mục tiêu: reach
Funnel stage: TOFU
Pain point: Người ta thử đủ cách mà không hiệu quả, không biết tại sao
Dạng bài:
  - Facebook: "3 lý do bạn tập gym 3 tháng mà vẫn không xuống cân"
  - Threads: "Sự thật không ai nói với bạn về việc đếm calories"
Hook mẫu: "Tôi đã tốn 8 tháng tập sai trước khi hiểu ra điều này..."
Tần suất: 2 bài/tuần
```

### Bước 2 — TOFU / MOFU / BOFU Mapping

**TOFU — Awareness & Reach**
- Mục tiêu: Tiếp cận người chưa biết mình/sản phẩm
- Facebook: Tips, sự thật ít biết, "X điều bạn cần biết về...", bài giáo dục
- Threads: Hook confession/rant, câu hỏi tranh luận, observation tâm lý, relatable pain
- Tỉ lệ đề xuất: 50–60% tổng bài
- Metric đo lường: Reach, New follows

**MOFU — Consideration & Trust**
- Mục tiêu: Chuyển người đã biết → người tin tưởng
- Facebook: Review thật (kèm nhược điểm), so sánh A vs B, Q&A dạng hỏi đáp
- Threads: Mini case study có số liệu cụ thể, before-after chi tiết, behind-the-scenes
- Tỉ lệ đề xuất: 25–35% tổng bài
- Metric đo lường: Comments, Saves, DM

**BOFU — Decision & Conversion**
- Mục tiêu: Chuyển người tin tưởng → người mua
- Facebook: Social proof tập hợp, offer cụ thể, deadline nếu có, FAQ trả lời objection
- Threads: Personal recommendation thẳng thắn, "link ở bio", last-mile trust
- Tỉ lệ đề xuất: 10–20% tổng bài
- Metric đo lường: Link clicks, Conversions

### Bước 3 — Tỉ lệ Value / Story / Sell

| Giai đoạn | Value | Story | Sell | Lý do |
|-----------|-------|-------|------|-------|
| Mới (<3 tháng) | 60% | 30% | 10% | Phải cho trước khi xin |
| Tăng trưởng (3–6 tháng) | 40% | 40% | 20% | Cân bằng xây trust và convert |
| Chín (>6 tháng) | 30% | 35% | 35% | Trust đủ để sell nhiều hơn |

Định nghĩa rõ ràng:
- **Value content:** Tips, kiến thức, giáo dục — không nhắc sản phẩm hoặc nhắc rất nhẹ
- **Story content:** Câu chuyện, trải nghiệm, case study — sản phẩm xuất hiện tự nhiên trong context
- **Sell content:** Đề xuất mua hàng rõ ràng, CTA trực tiếp, social proof để convert

### Bước 4 — Định hướng Reach / Trust / Conversion

Tùy mục tiêu ưu tiên của tháng, điều chỉnh mix content:

**Tháng tập trung REACH:**
- Tăng TOFU lên 70%
- Ưu tiên angle: Relatable Pain, Contrarian, Confession
- Format: Rant, Hook mạnh trên Threads
- Hạn chế BOFU còn 5–10%

**Tháng tập trung TRUST:**
- Tăng MOFU lên 50%
- Ưu tiên angle: Case Study, Before-After, Behind Scenes
- Format: Mini case study, Review thật
- Thêm nhược điểm sản phẩm → tăng credibility

**Tháng tập trung CONVERSION:**
- Tăng BOFU lên 30–40%
- Ưu tiên angle: Social Proof, Comparison, Prediction
- Format: Testimonial tổng hợp, FAQ objection handling
- Đảm bảo TOFU vẫn ≥ 30% để không cạn audience mới

### Bước 5 — Lịch Content Mẫu 7 ngày

Giai đoạn tăng trưởng (7 bài/tuần):
| Ngày | Funnel | Loại | Dạng bài |
|------|--------|------|---------|
| Thứ 2 | TOFU | Value | Tips / Sự thật ít biết |
| Thứ 3 | MOFU | Story | Mini case study / Before-after |
| Thứ 4 | TOFU | Value | Insight bất ngờ / Sự thật ngược |
| Thứ 5 | TOFU | Story | Confession / Rant |
| Thứ 6 | MOFU | Story | Review / So sánh |
| Thứ 7 | BOFU | Sell | Offer / Social proof / CTA |
| Chủ nhật | Linh hoạt | Tự chọn | Repost bài tốt / Engagement bait |

## Output format

Lưu tại `.claude/skills/affiliate-content-strategist/outputs/`:

**content-pillars.md** — 3–5 pillars đầy đủ theo template
**funnel-mapping.md** — Bảng TOFU/MOFU/BOFU với ví dụ content cụ thể theo nền tảng
**content-ratio.md** — Tỉ lệ value/story/sell + lịch tuần mẫu cho giai đoạn hiện tại

## Best practices
- Không nhảy vào BOFU khi trang chưa có trust — sẽ mất follower thay vì tăng conversion
- Mỗi pillar phải trả lời câu hỏi: "Tại sao người đọc quan tâm đến điều này?"
- Khi không biết viết gì → quay về content-pillars.md, chọn 1 pillar + 1 dạng bài
- Review pillars mỗi tháng và đối chiếu với data từ `content-performance-tracker`
- Đọc `data/winning-patterns.md` để bổ sung pillar từ pattern đã proven
- Chiến lược tốt nhất là chiến lược được dùng — đừng quá phức tạp ở giai đoạn đầu
