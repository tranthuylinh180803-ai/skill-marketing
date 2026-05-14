---
name: affiliate-audience-research
description: Nghiên cứu đối tượng mục tiêu cho affiliate — xây ICP, phân tích pain points 3 cấp, mapping hành vi trên Facebook/Threads
metadata:
  type: skill
  platforms: [facebook, threads]
  layer: research
---

# Affiliate Audience Research

## Purpose
Xây dựng bức tranh rõ ràng về người mua affiliate: họ là ai, nỗi đau thật sự ở đâu, và họ hành xử như thế nào trên từng nền tảng. Content tốt phải "nói đúng tiếng" của người đọc — skill này cung cấp ngôn ngữ đó.

## When to use
- Khởi động dự án affiliate mới
- Khi đổi sản phẩm hoặc ngành hàng
- Review ICP mỗi quý
- Khi content reach tốt nhưng không convert (sai người)
- Khi không biết viết về pain point gì

**Trigger phrases:** "nghiên cứu đối tượng affiliate", "tạo buyer persona", "ICP của sản phẩm này là ai", "phân tích audience", "đối thủ đang target ai"

## Inputs needed
Hỏi lần lượt từng câu:
1. Sản phẩm/dịch vụ affiliate là gì? Giá bán? Ai thường mua?
2. Ngành hàng cụ thể: sức khỏe / làm đẹp / tài chính / giáo dục / phần mềm / e-commerce / khác?
3. Bạn đã có khách hàng thật chưa? Nếu có, mô tả 1–2 người điển hình.
4. Có link page/profile/account đối thủ nào để tham khảo không?

Đọc thêm trước khi bắt đầu:
- `marketing-context.json` nếu tồn tại
- `data/winning-patterns.md` — audience nào đã tương tác tốt

## Workflow

### Bước 1 — Xây ICP (Ideal Customer Profile)

Tạo 2–3 chân dung khách hàng lý tưởng. Mỗi persona gồm:

**Nhân khẩu học:**
- Tuổi, giới tính, nghề nghiệp
- Thu nhập / khả năng chi tiêu
- Nơi sống (thành thị / ngoại ô), tình trạng hôn nhân

**Tâm lý học:**
- Giá trị sống quan trọng nhất
- Nỗi sợ lớn nhất liên quan đến vấn đề sản phẩm giải quyết
- Mong muốn / kết quả lý tưởng họ hướng tới
- Tự nhìn nhận bản thân như thế nào

**Hành vi mua hàng:**
- Ra quyết định mua nhanh hay cần nhiều thông tin?
- Trust ai nhất: chuyên gia / người dùng thật / người nổi tiếng?
- Cần gì để quyết định: giá / review / proof / bảo đảm?
- Đã thử giải pháp nào khác chưa? Tại sao thất bại?

**Ngôn ngữ tự nhiên:**
- Họ tự mô tả vấn đề của mình bằng từ gì?
- Từ nào họ dùng thường xuyên trong comment/post liên quan?
- Câu hỏi nào họ hay đặt ra?

### Bước 2 — Pain Point Analysis (3 Cấp)

```
CẤP 1 — SURFACE PAIN (họ nói ra được):
  Ví dụ: "Tôi muốn giảm cân"
  → Đây là vấn đề họ tìm kiếm trên Google
  → Content cấp này cạnh tranh cao, reach rộng nhưng convert yếu

CẤP 2 — UNDERLYING PAIN (lý do thật sự):
  Ví dụ: "Tôi mệt mỏi khi nhìn vào gương và không thích những gì mình thấy"
  → Cảm xúc thật phía sau cấp 1
  → Content cấp này tạo được resonance, người đọc thấy "bài viết về mình"

CẤP 3 — IDENTITY PAIN (sâu nhất, mạnh nhất):
  Ví dụ: "Tôi sợ mình thiếu kỷ luật và sẽ mãi không thay đổi được"
  → Mối đe dọa với self-image và identity
  → Content cấp này tạo emotional trigger mạnh nhất
  → Dùng tinh tế, không thao túng — chỉ dùng khi thực sự muốn giúp
```

**Quy tắc áp dụng:**
- TOFU content → nhắm vào Cấp 1 và 2
- MOFU content → nhắm vào Cấp 2 và 3
- BOFU content → kết nối từ Cấp 3 → giải pháp cụ thể

### Bước 3 — Messaging Map

Chuyển pain points thành message cho content:

| Pain Point | Cấp | Message Core | Hook mẫu |
|------------|-----|-------------|-----------|
| [pain cụ thể] | [1/2/3] | [góc tiếp cận] | [câu hook ví dụ] |

Ví dụ:
| Pain Point | Cấp | Message Core | Hook mẫu |
|------------|-----|-------------|-----------|
| Muốn giảm cân | 1 | Phương pháp đúng vs sai | "3 lý do tập gym 3 tháng mà vẫn không xuống cân" |
| Chán nản vì thử mãi không được | 2 | Cảm thông + lý giải | "Tôi hiểu cảm giác đó — và đây là lý do thật sự" |
| Sợ mình không có kỷ luật | 3 | Reframe + hope | "Vấn đề không phải ý chí của bạn yếu. Vấn đề là hệ thống." |

### Bước 4 — Platform Behavior Mapping

**Facebook — Người dùng Facebook:**
- Scroll thụ động nhiều hơn tìm kiếm chủ động
- Dừng lại khi: nhận ra mình trong bài, thấy số liệu bất ngờ, hoặc cảm xúc mạnh
- Comment khi: đồng cảm mạnh, muốn chia sẻ ý kiến, muốn tag người khác
- Giờ online cao điểm: 7–9h sáng (trước làm), 12–13h (giờ nghỉ), 20–22h (tối)
- Tin tưởng: review người dùng thật > quảng cáo > chuyên gia ẩn danh

**Threads — Người dùng Threads:**
- Tìm kiếm nội dung thú vị, quan điểm cá nhân
- Dừng lại khi: hook dòng đầu khác biệt, confess/rant có resonance
- Tương tác: repost khi đồng ý mạnh, reply khi muốn tranh luận
- Giờ online cao điểm: 12–13h, 21–23h
- Tin tưởng: giọng nói tự nhiên, authentic > tone chuyên nghiệp cứng

### Bước 5 — Competitor Audience Analysis (nếu có link)

Phân tích page/profile đối thủ:
- Họ đang target audience nào? (đọc từ comment, người tương tác)
- Angle nào họ hay dùng?
- Audience nào họ CHƯA khai thác? → Đây là cơ hội

**Không copy đối thủ — tìm khoảng trống họ bỏ qua.**

## Output format

Lưu tại `.claude/skills/affiliate-audience-research/outputs/`:

**buyer-persona.md** — 2–3 persona chi tiết theo format trên
**pain-points-map.md** — 3 cấp pain points + messaging map đầy đủ
**platform-behavior.md** — Insight hành vi theo từng nền tảng + giờ đăng gợi ý

## Best practices
- Dùng ngôn ngữ KHÁCH HÀNG tự dùng — không phải ngôn ngữ marketer
- Pain point cấp 3 mạnh nhất nhưng phải dùng để empathize, không phải để exploit
- Persona không phải con số nhân khẩu học — phải có cảm xúc và ngôn ngữ thật
- Cập nhật persona khi có data mới từ `content-performance-tracker` (audience thật vs giả định)
- Nếu không có dữ liệu thực tế: dùng common sense + research công khai, ghi rõ là giả định
