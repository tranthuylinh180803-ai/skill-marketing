---
name: content-performance-tracker
description: Theo dõi và phân tích hiệu suất content affiliate — 4 chiều (hook/CTA/format/timing), tìm winning/losing patterns, cập nhật data layer
metadata:
  type: skill
  platforms: [facebook, threads]
  layer: analytics
---

# Content Performance Tracker

## Purpose
Biến data content thành insight hành động. Không chỉ báo số — mà trả lời câu hỏi: "Tại sao bài này thắng? Tại sao bài kia thua? Tuần tới nên thay đổi gì?" Kết quả được lưu vào `data/` để toàn bộ workspace học từ đó.

**Feedback loop:**
```
Đăng bài → Có data → Tracker phân tích → Cập nhật winning-patterns.md
→ creative-angle-system đọc → hook-cta-optimizer đọc → Bài tiếp tốt hơn
```

## When to use
- Cuối tuần: mini review 7 ngày
- Cuối tháng: full report
- Khi reach/engagement đột ngột thay đổi — chẩn đoán nguyên nhân
- Trước khi lên kế hoạch content tháng mới

**Trigger phrases:** "phân tích performance", "báo cáo content", "bài nào hiệu quả nhất", "tại sao reach thấp", "cập nhật winning patterns", "review content tuần này"

## Inputs needed

Hỏi người dùng nhập data cho mỗi bài trong kỳ theo template sau. Nếu họ có CSV/export từ platform, nhận dạng và parse tự động.

**Template nhập liệu cho 1 bài:**
```
Bài [số]:
- Ngày/giờ đăng: [DD/MM/YYYY HH:MM]
- Platform: [FB / Threads]
- Hook (5–10 từ đầu): [...]
- Hook type: [number / question / confession / mistake / prediction / contrarian / relatable-pain / curiosity-gap / other]
- Angle: [confession / mistake / case-study / comparison / relatable-pain / contrarian / prediction / behind-scenes / social-proof / question-hook]
- Format: [storytelling / rant / confession / before-after / mini-case-study / diary / friend-advice / standard]
- Funnel stage: [TOFU / MOFU / BOFU]
- Có link không: [Có - vị trí: caption/comment/bio | Không]
- CTA type: [comment-keyword / comment-opinion / link-comment / link-bio / dm / save / share / follow]
- Reach: [số]
- Likes: [số]
- Comments: [số]
- Shares: [số]
- Link clicks: [số hoặc N/A]
```

## Workflow

### Bước 1 — Tính Metrics Cơ Bản

Cho mỗi bài:
- **Engagement Rate (ER)** = (Likes + Comments + Shares) / Reach × 100%
- **Click Rate** = Link clicks / Reach × 100% (nếu có)
- **Comment Rate** = Comments / Reach × 100%

Phân loại tự động:
- **Top performer** = ER > 5% HOẶC top 20% kỳ này
- **Average** = ER 2–5%
- **Low performer** = ER < 2% HOẶC bottom 20% kỳ này

### Bước 2 — 4 Chiều Phân Tích

**CHIỀU 1: HOOK PERFORMANCE**
Nhóm bài theo hook type → tính ER trung bình mỗi nhóm
```
Hook type       | Số bài | ER TB | Click Rate TB | Trend
Number hook     | X      | X%    | X%           | ↑/↓/→
Confession      | X      | X%    | X%           | ↑/↓/→
...
```
→ Hook type nào đang win? Loại nào underperform?

**CHIỀU 2: CTA PERFORMANCE**
Nhóm bài theo CTA type → tính click rate và comment rate
```
CTA type           | Số bài | ER TB | Click Rate TB
Comment keyword    | X      | X%    | X%
Link bio           | X      | X%    | X%
DM                 | X      | X%    | X%
...
```
→ "Comment X nhận link" vs "Link bio" vs "DM" — cái nào convert tốt hơn?

**CHIỀU 3: FORMAT PERFORMANCE**
Nhóm bài theo format
```
Format         | Số bài | ER TB | Reach TB
UGC Story      | X      | X%    | X
Rant           | X      | X%    | X
Case Study     | X      | X%    | X
Standard       | X      | X%    | X
...
```
→ Format nào reach xa nhất? Format nào conversion tốt nhất?

**CHIỀU 4: TIMING PERFORMANCE**
Nhóm bài theo giờ đăng và ngày trong tuần
```
Khung giờ   | Số bài | ER TB
7–9h        | X      | X%
12–13h      | X      | X%
20–22h      | X      | X%
...

Ngày trong tuần | Số bài | ER TB
Thứ 2           | X      | X%
...
```
→ Giờ nào ER cao nhất? Thứ mấy tốt cho TOFU? BOFU?

### Bước 3 — Pattern Finder

**Phân tích bài THẮNG (top 20%):**
```
Điểm chung của top 20%:
- Hook type phổ biến nhất: [...]
- Angle phổ biến nhất: [...]
- Format: [...]
- Giờ đăng phổ biến: [...]
- Có link không: [Có X% / Không X%]
- Funnel stage: TOFU X% / MOFU X% / BOFU X%
```

**Phân tích bài THUA (bottom 20%):**
```
Điểm chung của bottom 20%:
- Hook type phổ biến nhất: [...]
- Lỗi phổ biến: [...]
- CTA type: [...]
- Giờ đăng: [...]
- Format: [...]
```

**Kết luận patterns:**
- [Pattern A] → tương quan với ER cao (confirm sau N lần test)
- [Pattern B] → tương quan với ER thấp (cần tránh)

### Bước 4 — Tạo Báo Cáo

**Weekly Mini Report:**
```
WEEKLY REVIEW — Tuần [DD/MM – DD/MM/YYYY]
────────────────────────────────────────
Tổng bài: X (FB: Y | Threads: Z)
ER trung bình: X% (vs X% tuần trước → ↑/↓ X%)
Tổng reach: X

🏆 Bài tốt nhất:
  Platform: [...]
  Hook: "[...]"
  Angle: [...] | Format: [...]
  ER: X% | Reach: X

📉 Bài cần cải thiện:
  Platform: [...]
  Hook: "[...]"
  ER: X% — Lý do: [...]

💡 1 điều nên thay đổi tuần tới:
  [Thay đổi cụ thể, actionable]
```

**Monthly Full Report:**
```
MONTHLY REPORT — [Tháng MM/YYYY]
════════════════════════════════════════

OVERVIEW
Tổng bài: X | ER TB: X% | Total reach: X | Total clicks: X
So với tháng trước: ER ↑/↓ X% | Reach ↑/↓ X%

4 CHIỀU PHÂN TÍCH
[Bảng đầy đủ theo workflow trên]

TOP 3 WINNING PATTERNS
1. [Pattern] — ER X%, confirmed N lần
2. [Pattern] — ER X%, confirmed N lần
3. [Pattern] — ER X%, confirmed N lần

TOP 3 PATTERNS CẦN TRÁNH
1. [Pattern] — ER X%, N lần confirm
2. [Pattern] — ER X%, N lần confirm
3. [Pattern] — ER X%, N lần confirm

ĐỀ XUẤT THÁNG TỚI
- Tăng: [angle/format/hook type cụ thể]
- Giảm: [angle/format/hook type cụ thể]
- Test mới: [điều chưa thử]
- Giờ đăng nên dùng: [giờ cụ thể]
════════════════════════════════════════
```

### Bước 5 — Cập nhật Data Layer

Sau mỗi lần phân tích, BẮT BUỘC cập nhật:

**`data/winning-patterns.md`:**
- Thêm winning hooks mới (kèm ER + số lần confirm)
- Cập nhật thứ tự winning angles theo performance thực tế
- Thêm patterns cần tránh mới

**`data/performance-memory.json`:**
Cập nhật các field sau:
- `winning_hooks`: Thêm hook mới có ER cao
- `winning_angles`: Sắp xếp lại theo performance
- `best_posting_times`: Cập nhật khung giờ theo data thực
- `best_formats`: Cập nhật format tốt nhất cho reach / conversion
- `winning_cta_patterns`: Cập nhật CTA hoạt động tốt nhất
- `avoid_patterns`: Thêm pattern cần tránh
- `last_updated`: Ngày hôm nay

## Output format

Lưu báo cáo tại `.claude/skills/content-performance-tracker/outputs/report-[YYYY-MM].md`

## Best practices
- Cần ít nhất 10–15 bài để pattern có ý nghĩa — đừng rút kết luận từ 3–4 bài
- Phân tích RIÊNG Facebook và Threads — đừng gộp chung (behavior platform khác nhau hoàn toàn)
- Outlier (bài viral bất ngờ hoặc fail bất thường) → investigate lý do trước khi đưa vào pattern
- Cập nhật `data/` layer ngay sau mỗi phân tích — đây là bộ nhớ của toàn workspace
- ER trung bình thay đổi theo nền tảng và ngành — so sánh với chính mình, không phải benchmark chung
- Khi reach giảm đột ngột → chạy `compliance-guard` trên 3–5 bài gần nhất trước khi điều chỉnh content
