# Marketing AI Agent Skills

Bộ skills marketing cho AI agents — giúp thực hiện các tác vụ marketing với đúng framework và best practices.

## Cấu trúc

```
.claude/skills/
│
├── product-marketing-context.md   ← Skill nền tảng (đọc trước tiên)
│
├── social-content.md              ← Caption, content calendar, hashtag
├── video.md                       ← Script, shot list, AI video tools
├── image.md                       ← AI prompt, creative brief, ad creative
├── sales-enablement.md            ← Battlecard, objection handling, pitch deck
├── referral-affiliate.md          ← Referral program & affiliate program
│
└── shared/
    ├── frameworks.md              ← AIDA, PAS, SPIN, retention loop...
    ├── hooks.md                   ← Thư viện hook viral theo nền tảng
    ├── ctas.md                    ← Thư viện CTA theo mục tiêu & funnel
    └── brand-voice.md             ← Template hướng dẫn brand voice
```

## Cách hoạt động

1. **Mọi skill đều đọc `product-marketing-context` trước** để hiểu sản phẩm và ICP
2. **Skills tham chiếu `shared/`** khi cần hook, CTA hay framework chuẩn
3. **Context lưu trong `marketing-context.json`** — tạo 1 lần, dùng mãi

## Kích hoạt skill

| Câu bạn nói | Skill kích hoạt |
|-------------|-----------------|
| "Viết caption / content calendar..." | `social-content` |
| "Viết script / làm video..." | `video` |
| "Tạo ảnh / AI prompt / brief designer..." | `image` |
| "Battlecard / objection / pitch deck..." | `sales-enablement` |
| "Referral program / affiliate program..." | `referral-affiliate` |
| "Cập nhật thông tin sản phẩm..." | `product-marketing-context` |

## Cấu trúc chuẩn của mỗi skill

Mỗi file skill có 7 phần:
1. **YAML frontmatter** — name, description
2. **Purpose** — Skill làm gì
3. **When to use** — Câu trigger
4. **Inputs needed** — Cần thông tin gì
5. **Workflow** — Các bước thực hiện
6. **Frameworks** — Template, công thức
7. **Output format** — Agent biết cần output gì
8. **Best practices** — Quy tắc quan trọng

## Bắt đầu lần đầu

Nếu chưa có `marketing-context.json`, skill `product-marketing-context` sẽ hỏi từng câu để tạo file context. Chỉ cần làm 1 lần — mọi session sau đều dùng lại.
