---
name: social-content
description: Create high-converting social media content — captions, hooks, content calendars, hashtags — for TikTok, Instagram, Facebook, LinkedIn, X
---

# Purpose
Tạo nội dung social media chuyển đổi cao — từ hook đến caption, lịch nội dung và hashtag, cho mọi nền tảng.

# When to use
- "Viết caption cho Instagram/Facebook/TikTok"
- "Tạo content calendar tháng này"
- "Lên ý tưởng nội dung cho sản phẩm X"
- "Tối ưu caption đang có của tôi"
- "Viết thread cho LinkedIn"
- "Tạo hook viral"

# Inputs needed
Đọc `marketing-context.json` hoặc gọi skill `product-marketing-context` trước.
Cần tối thiểu:
- Tên sản phẩm
- ICP (đối tượng mục tiêu)
- Brand voice
- Nền tảng mục tiêu
- Mục tiêu bài post (awareness / engagement / conversion)

# Workflow

1. **Identify platform** — TikTok / Instagram / LinkedIn / Facebook / X?
2. **Analyze target audience** — ICP đang ở đâu về hành trình mua hàng?
3. **Pick content angle**:
   - Educational (dạy điều gì đó hữu ích)
   - Controversial (quan điểm trái chiều)
   - Relatable (đồng cảm với pain point)
   - Storytelling (kể chuyện cá nhân)
4. **Generate hook** — Câu đầu tiên phải giữ người đọc dừng scroll
5. **Write body** — Giá trị thực sự nằm ở đây
6. **Add CTA** — 1 hành động duy nhất, rõ ràng
7. **Optimize for platform algorithm** — Độ dài, hashtag, format đúng nền tảng

# Frameworks

## Viral hook formulas
```
- "Nobody talks about this..."
- "POV: [tình huống quen thuộc]"
- "This changed everything for me"
- "I was wrong about [điều phổ biến mọi người tin]"
- "[Số] điều [nhóm người] không muốn bạn biết"
- "Đừng [hành động phổ biến] nếu chưa đọc điều này"
- "Nếu bạn đang [pain point], bài này dành cho bạn"
```

## Content pillars (80/20)
```
80% nội dung giá trị:
- Education: Dạy điều gì đó
- Entertainment: Giải trí, relatable
- Inspiration: Truyền cảm hứng

20% nội dung bán hàng:
- Promotion, offer, CTA mua hàng
```

## CTA library
```
Engagement:
- "Comment [từ khóa] để nhận guide miễn phí"
- "Save post này — bạn sẽ cần nó sau"
- "Tag người bạn cần đọc cái này"

Growth:
- "Follow để không bỏ lỡ phần tiếp theo"
- "Share nếu bài này hữu ích với bạn"

Conversion:
- "DM tôi '[từ khóa]' để biết thêm chi tiết"
- "Link ở bio — nhấn vào để xem thêm"
```

## Platform specs

| Nền tảng | Độ dài tối ưu | Hashtag | Giờ đăng |
|----------|--------------|---------|----------|
| TikTok | 100-150 ký tự | 3-5 | 19-21h |
| Instagram Feed | 138-150 từ | 5-10 | 9h, 12h, 19h |
| Instagram Reels | Ngắn — video nói thay | 3-5 | 9-11h |
| Facebook | 40-80 từ | 2-3 | 12h, 19h |
| LinkedIn | 1000-1300 ký tự | 0-3 | 8-9h sáng |
| X/Twitter | <280 ký tự | 1-2 | 9h, 12h |

# Output format

## Single post
```md
# Hook
[Câu đầu tiên — gây dừng scroll]

# Caption
[Thân bài — giá trị thực]

# CTA
[1 hành động duy nhất]

# Hashtags
[#...]
```

## Content calendar (30 ngày)
```md
| Ngày | Nền tảng | Loại | Chủ đề | Hook | CTA |
|------|----------|------|--------|------|-----|
| 1 | TikTok | Education | ... | ... | ... |
```

# Best practices
- Hook nằm trong dòng đầu tiên — không để sau "Xem thêm"
- Chỉ có 1 CTA — nhiều CTA = không CTA nào được thực hiện
- Xuống dòng sau mỗi 1-2 câu để dễ đọc trên mobile
- Không dùng link trong LinkedIn post (giảm reach) — để trong comment đầu tiên
- Test 2-3 hook khác nhau cho cùng 1 bài để tìm winner
