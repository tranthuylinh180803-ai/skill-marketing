---
name: video
description: Create video scripts, shot lists, B-roll ideas, and AI video prompts for TikTok, Reels, YouTube Shorts, and long-form YouTube
---

# Purpose
Tạo script video, shot list, ý tưởng B-roll và AI video prompts — từ TikTok 15 giây đến YouTube dài.

# When to use
- "Viết script video TikTok/Reels/YouTube"
- "Tạo shot list cho video quảng cáo"
- "Dùng AI làm video mà không cần quay"
- "Lên kịch bản UGC / testimonial video"
- "Tạo hook video mạnh"
- "Làm B-roll list"

# Inputs needed
Đọc `marketing-context.json` hoặc gọi skill `product-marketing-context` trước.
Cần tối thiểu:
- Sản phẩm / chủ đề video
- Nền tảng (TikTok / Reels / YouTube)
- Độ dài mục tiêu
- Mục tiêu (awareness / demo / conversion / UGC)

# Workflow

1. **Define video goal** — Bài này muốn người xem làm gì sau khi xem xong?
2. **Choose format**:
   - UGC (người thật, tự nhiên)
   - Explainer (giải thích vấn đề)
   - Tutorial (hướng dẫn từng bước)
   - Storytelling (kể chuyện)
3. **Create hook** — 3 giây đầu quyết định tất cả
4. **Build retention loop** — Giữ người xem đến cuối
5. **Add CTA** — 1 hành động duy nhất ở cuối
6. **Generate visual directions** — Shot list, B-roll, text overlay

# Frameworks

## Short-form retention formula
```
Hook → Curiosity gap → Fast value → Pattern interrupt → CTA
```
- **Hook** (0-3s): Gây dừng scroll ngay lập tức
- **Curiosity gap** (3-8s): Tạo câu hỏi chưa được trả lời
- **Fast value** (8-40s): Deliver nhanh, không padding
- **Pattern interrupt** (giữa video): Cắt cảnh / âm thanh / text đột ngột để giữ attention
- **CTA** (5-10s cuối): 1 hành động duy nhất

## Script formats theo loại

### UGC / Testimonial (15-60s)
```
[Hook tự nhiên 0-3s] Câu mở không "diễn"
[Pain point 3-10s] "Trước đây tôi đang gặp vấn đề X..."
[Discovery 10-20s] "Rồi tôi tìm thấy [sản phẩm]..."
[Result 20-40s] "Sau [thời gian], tôi đã [kết quả + số liệu]"
[Recommendation 40-60s] "Nếu bạn đang [pain point], hãy thử..."
```

### Explainer / Tutorial (1-5 phút)
```
[Intro 10%] "Trong video này bạn sẽ học [kết quả cụ thể]"
[Body 80%] Bước 1 → Bước 2 → Bước 3 (mỗi bước có tiêu đề rõ)
[Outro 10%] Tóm tắt → CTA subscribe / comment / mua
```

### Storytelling
```
[Setup 20%] Nhân vật / Bối cảnh / Trạng thái "trước"
[Conflict 60%] Vấn đề → Thử cách khác → Tìm thấy giải pháp
[Resolution 20%] Kết quả / Transformation / CTA
```

## AI video production tools
| Tool | Dùng cho | Ghi chú |
|------|----------|---------|
| Pictory.ai | Script → video tự động | Tìm stock footage tự động |
| Synthesia | AI avatar nói theo script | Hỗ trợ nhiều ngôn ngữ |
| HeyGen | Clone giọng / khuôn mặt | Tiếng Việt tốt |
| ElevenLabs | Voiceover AI | Giọng tự nhiên nhất |
| CapCut | Chỉnh sửa + auto caption | Miễn phí, dễ dùng |
| Descript | Chỉnh video như chỉnh text | Edit bằng cách xóa chữ |

# Output format

```md
# Script: [Tên video]
**Nền tảng**: [TikTok/Reels/YouTube]
**Độ dài**: [X giây/phút]
**Mục tiêu**: [Awareness/Demo/Conversion]

---

| Thời gian | Hình ảnh (Visual) | Lời thoại | Text overlay | Nhạc/SFX |
|-----------|-------------------|-----------|--------------|----------|
| 00:00-00:03 | [mô tả cảnh] | [lời nói] | [text trên màn hình] | [nhạc] |

---

**Caption khi đăng**: [...]
**Hashtag**: [#...]
**Thumbnail**: [Mô tả thumbnail]
```

# Best practices
- 3 giây đầu không có hook mạnh = video chết
- Caption video cần hook riêng — người tắt tiếng vẫn phải hiểu
- B-roll nên cắt mỗi 2-3 giây để giữ nhịp
- Đặt face cam ở đầu video — khuôn mặt giữ attention tốt hơn text
- Luôn có captions/subtitles — 85% người xem TikTok không bật âm thanh
