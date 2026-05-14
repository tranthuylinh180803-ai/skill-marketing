---
name: image
description: Create, edit, and optimize marketing images — AI image prompts for Midjourney/DALL-E/Flux, creative briefs for designers, thumbnail and ad creative optimization
---

# Purpose
Tạo hình ảnh marketing hiệu quả — từ viết AI prompt đến creative brief cho designer và tối ưu creative hiện có.

# When to use
- "Tạo hình ảnh quảng cáo cho sản phẩm X"
- "Viết prompt để tạo ảnh marketing"
- "Tối ưu hình ảnh đang có để tăng CTR"
- "Thiết kế thumbnail YouTube"
- "Tạo banner / ad creative"
- "Viết brief cho designer"

# Inputs needed
Đọc `marketing-context.json` hoặc gọi skill `product-marketing-context` trước.
Cần tối thiểu:
- Mục đích hình ảnh (ad / organic / thumbnail / banner)
- Nền tảng và kích thước
- Brand color palette
- Tone / style mong muốn

# Workflow

1. **Determine image purpose** — Ad performance, organic engagement, hay brand awareness?
2. **Define emotional tone** — Người xem phải cảm thấy gì khi nhìn vào?
3. **Identify focal point** — Mắt nhìn vào đâu đầu tiên?
4. **Create composition** — Hierarchy thị giác: Hero → Headline → CTA
5. **Add branding elements** — Màu, logo, font nhất quán
6. **Optimize for platform** — Kích thước và safe zone đúng

# Frameworks

## AI Prompt Structure
```
[Subject] + [Style] + [Lighting] + [Composition] + [Mood]

Ví dụ:
"Modern SaaS dashboard on MacBook screen,
cinematic lighting, dark mode interface,
clean minimal composition, rule of thirds,
professional futuristic mood, 4K quality"
```

## Kích thước chuẩn theo nền tảng
```
Facebook Feed: 1200×628px hoặc 1080×1080px
Instagram Feed: 1080×1350px (4:5 — reach tốt nhất)
Story/Reels: 1080×1920px (9:16)
YouTube Thumbnail: 1280×720px (16:9)
Google Display: 300×250, 728×90, 160×600
```

## Visual hierarchy cho Ad
```
1. HERO (lớn nhất): Hình ảnh sản phẩm hoặc người
2. HEADLINE: Benefit chính — 5-7 từ
3. SUBTEXT: Chi tiết hỗ trợ
4. CTA BUTTON: Màu tương phản, text rõ
5. LOGO: Nhỏ, góc dưới
```

## Màu sắc và tâm lý
```
Đỏ → Urgency, passion, sale
Xanh lam → Trust, security (fintech, healthcare)
Xanh lá → Growth, health, nature
Vàng/Cam → Energy, value, friendly (food & beverage)
Đen/Trắng → Premium, minimalist
```

## Quy tắc 60-30-10
```
60% màu chủ đạo (nền)
30% màu phụ (text, element chính)
10% màu nhấn (CTA, highlight)
```

# Output format

## AI Prompt (copy vào Midjourney / DALL-E / Flux)
```md
# Prompt

[Subject mô tả cụ thể] + [Style: cinematic/editorial/minimalist] +
[Lighting: soft natural/studio/golden hour] +
[Composition: rule of thirds/flat lay/close-up] +
[Mood: professional/energetic/calm] +
[Quality: 4K/hyperrealistic/commercial photography] +
[Brand colors: hex codes] +
[Avoid: no text/no watermark/no cluttered background]

**Tool phù hợp**: [Midjourney / DALL-E 3 / Ideogram / Adobe Firefly]
**Ratio**: [--ar 4:5] hoặc [--ar 16:9]
```

## Creative Brief (gửi cho designer)
```md
# Creative Brief: [Tên dự án]

**Mục đích**: [Ad / Organic / Banner]
**Nền tảng & kích thước**: [...]
**Deadline**: [...]

**Thông điệp chính** (1 câu):
→ [Điều duy nhất người xem phải nhớ]

**Headline**: [Text chính]
**CTA**: [Text nút hoặc lời kêu gọi]

**Visual direction**:
- Style: [Lifestyle / Product / Abstract]
- Màu: [HEX codes]
- Cảm xúc: [Gợi lên cảm giác gì]
- Tránh: [Không dùng gì]

**Đối tượng**: [Tóm tắt ICP]
**Ví dụ tham khảo**: [Link hoặc mô tả]
```

## Feedback / Optimize existing image
```md
**Checklist phân tích**:
- [ ] Hiểu nội dung trong 3 giây không?
- [ ] Text đọc được trên mobile?
- [ ] CTA có nổi bật không?
- [ ] Có quá nhiều element cạnh tranh nhau không?

**Top 3 cần sửa**:
1. [Vấn đề cụ thể + cách sửa]
2. [...]
3. [...]
```

# Best practices
- High contrast giữa text và background — test trên mobile trước
- Clear focal point — mắt người phải biết nhìn vào đâu ngay lập tức
- Minimal text — ảnh marketing không phải brochure
- Đặt khuôn mặt người nhìn về phía CTA — mắt người theo hướng nhìn
- Dùng số cụ thể trong headline: "Tiết kiệm 40%" tốt hơn "Tiết kiệm đáng kể"
- Mobile-first: test xem ảnh trông thế nào ở kích thước 375px width
