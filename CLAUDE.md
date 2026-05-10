# Marketing AI Agent Skills — Hướng dẫn cho Agent

## Tổng quan dự án
Thư mục này chứa bộ Marketing AI Agent Skills — các skill markdown hỗ trợ marketer thực hiện tác vụ marketing với đúng framework.

## Skills có sẵn

Đọc `.claude/skills/README.md` để hiểu toàn bộ bộ skills.

### Skill nền tảng (luôn đọc trước)
- `.claude/skills/product-marketing-context.md` — Thu thập và quản lý context về sản phẩm, ICP, brand

### Skill chuyên biệt
- `.claude/skills/sales-enablement.md` — Referral & Affiliate program
- `.claude/skills/social-content.md` — Social media content (caption, calendar, hashtag)
- `.claude/skills/video.md` — Video script, storyboard, AI production workflow
- `.claude/skills/image.md` — AI image prompt, creative brief, thiết kế marketing

## Nguyên tắc làm việc

1. **Luôn đọc `marketing-context.json` trước** mỗi tác vụ marketing (nếu file tồn tại)
2. **Hỏi từng câu một** khi cần thu thập thông tin — không hỏi nhiều câu cùng lúc
3. **Output phải actionable** — cụ thể, copy-paste được, không lý thuyết chung chung
4. **Tone tiếng Việt** trừ khi được yêu cầu khác
5. **Kích thước và spec kỹ thuật** phải chính xác theo nền tảng

## Quy tắc lưu file (BẮT BUỘC)

Mọi nội dung marketing mà người dùng xây dựng đều được lưu vào `.claude/skills/`:
- Skill mới → `.claude/skills/<tên-skill>.md`
- Framework / template → `.claude/skills/<tên>.md`
- Context sản phẩm → `.claude/skills/` hoặc `marketing-context.json` ở thư mục gốc

**Không lưu nội dung marketing vào thư mục gốc** trừ khi người dùng yêu cầu rõ ràng.

## File context
`marketing-context.json` — File tự động tạo khi chạy skill `product-marketing-context` lần đầu. Chứa toàn bộ thông tin sản phẩm và brand.
