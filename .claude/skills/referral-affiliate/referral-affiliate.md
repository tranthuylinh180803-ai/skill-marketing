---
name: referral-affiliate
description: Design and build referral programs (customer-to-customer) and affiliate programs (partner/KOL-driven) — mechanics, copy, emails, and tracking setup
---

# Purpose
Thiết kế và triển khai chương trình giới thiệu khách hàng (referral) và chương trình tiếp thị liên kết (affiliate) — từ cơ chế thưởng đến landing page, email sequence và hướng dẫn tracking.

# When to use
- "Tạo referral program cho sản phẩm"
- "Thiết kế affiliate program"
- "Làm chương trình giới thiệu bạn bè"
- "Viết email cho affiliate"
- "Tính hoa hồng cho đối tác"
- "Tạo landing page referral"

# Inputs needed
Đọc `marketing-context.json` hoặc gọi skill `product-marketing-context` trước.
Cần tối thiểu:
- Tên sản phẩm và giá
- LTV (lifetime value) của khách hàng
- ICP — ai là người sẽ giới thiệu?
- Ngân sách hoa hồng

# Workflow

1. **Xác định loại chương trình** — Referral (khách → khách) hay Affiliate (đối tác → khách)?
2. **Thiết kế cơ chế thưởng** — Tính hoa hồng hợp lý theo LTV
3. **Tạo landing page copy** — Trang đăng ký và giới thiệu chương trình
4. **Viết email sequence** — Chào mừng, nhắc nhở, báo cáo hoa hồng
5. **Tạo affiliate kit** — Caption mẫu, banner, FAQ
6. **Xác định tracking setup** — Tool và quy tắc thanh toán

# Frameworks

## Tính hoa hồng hợp lý
```
Hoa hồng lý tưởng = LTV × 10-20%

Ví dụ:
LTV = 1.200.000đ/năm
→ Affiliate: 120.000 - 240.000đ/đơn
→ Referral: voucher 50.000đ hoặc 1 tháng free
```

## Mô hình thưởng theo loại sản phẩm
| Mô hình | Phù hợp với | Ví dụ |
|---------|-------------|-------|
| % hoa hồng | Affiliate, sản phẩm giá cao | 15% mỗi đơn |
| Tiền mặt cố định | Referral đơn giản | 100.000đ/người |
| Credit/điểm | SaaS, subscription | 1 tháng miễn phí |
| Bậc thang | Affiliate chuyên nghiệp | 10% → 15% → 20% |

## Học từ case study tốt nhất
- **Dropbox**: Tặng storage cho cả 2 bên → tăng 3900% trong 15 tháng
- **Airbnb**: Tặng credit đi ở → viral vì reward gắn liền sản phẩm
- **Tesla**: Reward cao cấp (test drive, event độc quyền) → phù hợp ICP giàu

# Output format

## Landing page copy
```md
# [Tiêu đề]: Kiếm [X]đ mỗi lần giới thiệu bạn bè

**Phụ đề**: Chia sẻ [Tên sản phẩm] và nhận hoa hồng tự động

**Cơ chế (3 bước)**:
1. Đăng ký miễn phí → nhận link cá nhân
2. Chia sẻ link với bạn bè
3. Nhận [thưởng] khi bạn bè mua hàng

**Mức thưởng**: [Chi tiết rõ ràng]

**CTA**: [Đăng ký ngay — miễn phí]
```

## Email chào mừng affiliate
```md
Subject: Chào mừng [Tên] — Link affiliate của bạn đây!

Nội dung:
- Link affiliate cá nhân
- Hướng dẫn bắt đầu (3 bước)
- Tài nguyên hỗ trợ (caption mẫu, banner)
- Liên hệ support
```

## Affiliate kit (caption mẫu)
```md
**TikTok/Reels** (60 giây):
"Tôi vừa tìm thấy [sản phẩm] và đây là lý do tôi không thể ngừng dùng nó..."

**Instagram caption**:
"Honest review sau [thời gian] dùng [sản phẩm]..."

**Facebook**:
"Nếu bạn đang gặp [pain point], đây là thứ tôi đang dùng..."
```

# Best practices
- Reward phải đủ lớn để người dùng thực sự hành động
- Quá trình chia sẻ phải cực kỳ đơn giản (1-2 click)
- Người được giới thiệu cũng phải nhận benefit → tăng tỉ lệ chuyển đổi
- Tracking phải minh bạch → affiliate trust = affiliate effort
- Thanh toán hoa hồng đúng hẹn là yếu tố giữ chân affiliate lâu dài
