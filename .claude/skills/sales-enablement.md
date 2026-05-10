---
name: sales-enablement
description: Create sales assets to help sales team close deals — battlecards, objection handling, one-pagers, demo scripts, pitch decks, competitor comparison
---

# Purpose
Hỗ trợ sales team chốt deal bằng cách tạo tài liệu bán hàng chuyên nghiệp — từ xử lý objection đến pitch deck và battlecard.

# When to use
- "Tạo battlecard cho sản phẩm X"
- "Viết script demo cho sales team"
- "Xây dựng one-pager giới thiệu sản phẩm"
- "Cách trả lời khi khách nói đắt quá"
- "So sánh sản phẩm với đối thủ"
- "Tạo pitch deck"

# Inputs needed
Đọc `marketing-context.json` hoặc gọi skill `product-marketing-context` trước.
Cần tối thiểu:
- Tên sản phẩm và USP
- ICP (khách hàng mục tiêu)
- Đối thủ cạnh tranh
- Giá và mô hình kinh doanh
- Pain points phổ biến nhất của khách

# Workflow

1. **Understand ICP** — Xác định loại khách hàng sales đang tiếp cận
2. **Identify pain points** — Nỗi đau nào đang dẫn đến cuộc trò chuyện này?
3. **Map product benefits** — Gắn benefit với từng pain point cụ thể
4. **Generate sales asset** — Tạo tài liệu phù hợp với yêu cầu
5. **Handle objections** — Chuẩn bị xử lý phản đối phổ biến
6. **Reinforce differentiation** — Nhấn mạnh điểm khác biệt so với đối thủ

# Frameworks

## Objection Handling — Feel / Felt / Found
```
"Tôi hiểu bạn CẢM THẤY vậy.
Nhiều khách hàng của chúng tôi cũng ĐÃ CẢM THẤY như thế.
Nhưng sau khi dùng thử, họ NHẬN RA rằng..."
```

## Value Messaging — Pain / Solution / Outcome
```
[Pain]: Khách đang gặp vấn đề gì?
[Solution]: Sản phẩm giải quyết thế nào?
[Outcome]: Kết quả cụ thể sau khi dùng?
```

## SPIN Selling — Câu hỏi dẫn dắt
```
Situation: "Hiện tại bạn đang xử lý [X] như thế nào?"
Problem: "Điều đó có gây ra [Y] không?"
Implication: "Nếu không giải quyết, điều đó ảnh hưởng thế nào đến [Z]?"
Need-payoff: "Nếu có giải pháp giúp [kết quả], nó có giá trị không?"
```

# Output format

## Battlecard
```md
# Battlecard: [Tên sản phẩm] vs [Đối thủ]

## Khi khách nhắc đến [Đối thủ]
**Điểm yếu của họ**: ...
**Lợi thế của chúng ta**: ...
**Câu trả lời gợi ý**: "..."

## Win rates
Chúng ta thắng khi: ...
Chúng ta thua khi: ...
```

## Objection Handling Guide
```md
# Objection: "[Câu phản đối của khách]"

**Đừng nói**: ...
**Hãy nói**: ...

**Ví dụ thực tế**: "..."

**Follow-up question**: "..."
```

## One-pager
```md
# [Tên sản phẩm] — Giải pháp cho [Pain point]

**Vấn đề**: [1-2 câu mô tả pain point]
**Giải pháp**: [1-2 câu mô tả sản phẩm]
**Kết quả**: [3 bullet points — số liệu cụ thể]
**Tại sao chúng tôi**: [USP ngắn gọn]
**Bước tiếp theo**: [CTA rõ ràng]
```

## Demo Script
```md
# Script Demo: [Tên sản phẩm]

**[0:00-2:00] Hook**
"Trước khi tôi show demo, cho tôi hỏi — [câu hỏi tìm pain point]?"

**[2:00-10:00] Demo flow**
Bước 1: [Feature giải quyết pain lớn nhất]
Bước 2: [Feature tạo wow moment]
Bước 3: [Feature chứng minh ROI]

**[10:00-15:00] Close**
"Dựa trên những gì bạn vừa xem, phần nào giải quyết được vấn đề bạn đang gặp nhất?"
```

# Best practices
- Đặt câu hỏi trước khi pitch — hiểu đúng pain point mới pitch đúng
- Số liệu cụ thể luôn tốt hơn lời hứa chung (giảm 40% thay vì "tiết kiệm đáng kể")
- Không attack đối thủ trực tiếp — chỉ nêu điểm khác biệt
- Mỗi objection response nên kết thúc bằng một câu hỏi ngược
