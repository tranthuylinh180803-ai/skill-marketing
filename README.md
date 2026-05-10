# Marketing AI Agent Skills Workspace

> Không gian làm việc cá nhân với Claude Code — bộ skills marketing giúp AI agent thực hiện các tác vụ marketing chuyên nghiệp.

Được xây dựng bằng **Claude Code** | Học tại **SEONGON Marketing Course**

---

## Cấu trúc workspace

```
.
├── CLAUDE.md                          ← Hướng dẫn cho Claude Code
├── README.md                          ← File này
├── marketing-context.json             ← Context sản phẩm (tạo khi chạy lần đầu)
│
├── .claude/skills/
│   ├── product-marketing-context.md  ← Skill nền tảng (tất cả skill khác đọc trước)
│   │
│   ├── social-content.md             ← Caption, content calendar, hashtag
│   ├── video.md                      ← Script, shot list, AI video tools
│   ├── image.md                      ← AI image prompt, creative brief
│   ├── sales-enablement.md           ← Battlecard, objection handling, pitch deck
│   ├── referral-affiliate.md         ← Referral & affiliate program
│   │
│   ├── social-api-connect.md         ← 🔌 Kết nối API ngoài (Facebook, GA4, TikTok)
│   │
│   ├── seo-audit/                    ← 📁 Skill có files & folders
│   │   ├── seo-audit.md
│   │   ├── scripts/
│   │   │   └── pagespeed-check.py   ← Chạy được ngay, gọi Google API
│   │   ├── templates/
│   │   │   ├── audit-checklist.md
│   │   │   └── report-template.md
│   │   └── outputs/                 ← Kết quả audit được lưu tại đây
│   │
│   └── shared/
│       ├── frameworks.md            ← AIDA, PAS, SPIN, Story Arc...
│       ├── hooks.md                 ← Thư viện hook viral
│       ├── ctas.md                  ← Thư viện CTA theo funnel
│       └── brand-voice.md          ← Template kiểm tra tone
│
└── Nhap_Mon_Lap_Trinh_Marketing.ipynb ← Notebook học lập trình marketing
```

---

## Skills nổi bật

### 🔌 `social-api-connect` — Kết nối API ngoài
Kết nối trực tiếp với:
- **Google PageSpeed Insights API** (miễn phí, không cần auth)
- **Facebook Graph API** — lấy insights, đăng bài tự động
- **Google Analytics 4** — lấy sessions, users, events
- **TikTok API** — xem stats video

### 📁 `seo-audit/` — Skill có folder riêng
```bash
# Chạy audit ngay lập tức
python .claude/skills/seo-audit/scripts/pagespeed-check.py \
  --url https://yourwebsite.com \
  --strategy both \
  --output .claude/skills/seo-audit/outputs/
```

---

## Cách dùng

### 1. Clone repo
```bash
git clone https://github.com/YOUR_USERNAME/marketing-ai-skills.git
cd marketing-ai-skills
```

### 2. Mở với Claude Code
```bash
claude
```

### 3. Kích hoạt skill bằng cách nói tự nhiên
```
"Viết caption TikTok cho sản phẩm app dinh dưỡng"
→ Tự động dùng skill: social-content + product-marketing-context

"Kiểm tra SEO website anthropic.com"
→ Tự động dùng skill: seo-audit

"Lấy insights từ Facebook Page của tôi"
→ Tự động dùng skill: social-api-connect
```

---

## Yêu cầu

- **Claude Code** CLI (claude.ai/code)
- **Python 3.8+** (cho seo-audit script)
- API credentials tùy skill (xem hướng dẫn trong từng file skill)

---

## Tác giả

**Trần Thùy Linh** | tranthuylinh180803@gmail.com
Học viên Marketing | SEONGON

*Workspace được xây dựng với Claude Code — Anthropic*
