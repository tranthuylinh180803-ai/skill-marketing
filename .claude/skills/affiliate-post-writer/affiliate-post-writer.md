---
name: affiliate-post-writer
description: Viết bài đăng affiliate cho Facebook và Threads — caption thông thường, UGC creator-style, content calendar, A/B variants
metadata:
  type: skill
  platforms: [facebook, threads]
  layer: production
---

# Affiliate Post Writer

## Purpose
Sản xuất nội dung bài đăng affiliate hoàn chỉnh cho Facebook và Threads. Có 2 mode chính: Standard Post (caption chuẩn) và UGC/Creator-Style (tự nhiên như người dùng thật). Là skill dùng thường xuyên nhất trong workspace.

**Nguyên tắc cốt lõi:** Bài affiliate tốt nhất là bài mà người đọc không nhận ra ngay là bài affiliate cho đến khi đã bị thu hút.

## When to use
- Viết bài đăng hàng ngày
- Lên content calendar tuần/tháng
- Rewrite bài cũ theo góc mới
- Tạo A/B variants để test

**Trigger phrases:** "viết bài affiliate", "viết caption", "viết thread", "lên lịch content", "bài facebook affiliate", "ugc style", "viết như người dùng thật", "storytelling affiliate"

## Inputs needed

Đọc trước khi bắt đầu (nếu tồn tại):
- `data/winning-patterns.md` — format và angle đang hoạt động tốt
- `.claude/skills/affiliate-content-strategist/outputs/content-pillars.md` — chọn đúng pillar
- `.claude/skills/creative-angle-system/outputs/angle-bank.md` — chọn góc viết hôm nay

Hỏi người dùng:
1. Sản phẩm/benefit muốn viết về hôm nay?
2. Nền tảng: Facebook hay Threads?
3. Format: bài lẻ / thread chuỗi / content calendar / A/B variants?
4. Style: Standard (caption chuẩn) hay UGC-style (tự nhiên như người dùng thật)?
5. Funnel stage: TOFU / MOFU / BOFU?

## Workflow

---

### MODE A — Standard Post

**Facebook Caption — Cấu trúc chuẩn:**

```
[HOOK — 1–2 câu đầu, phải dừng scroll]
[dòng trắng]
[SETUP — 2–3 câu bối cảnh/vấn đề]
[dòng trắng]
[BODY — 3–5 câu nội dung chính / value]
[dòng trắng]
[BRIDGE — 1–2 câu kết nối tự nhiên sang sản phẩm]
[dòng trắng]
[CTA — 1 câu cụ thể, 1 hành động duy nhất]
```

Quy tắc format Facebook:
- Dòng đầu tối đa 125 ký tự (sau đó bị cắt "Xem thêm" — đây là hook)
- Dùng dòng trắng ngăn đoạn — đừng viết 1 khối
- Tối đa 3–5 emoji, dùng có chủ đích, không rải đều
- Không dùng quá 3 hashtag, đặt cuối bài nếu dùng
- Không để link affiliate thẳng trong caption → để comment hoặc bio

**Threads Post — Cấu trúc chuẩn:**

```
1/ [Hook — dòng đầu, tối đa 280 ký tự, phải đứng độc lập]
2/ [Mở rộng hook hoặc setup vấn đề]
3/ [Nội dung / điểm chính 1]
4/ [Nội dung / điểm chính 2]
5/ [Nội dung / điểm chính 3]
...
N/ [CTA hoặc câu kết — thường ở cuối]
```

Quy tắc format Threads:
- Dòng 1 quyết định có ai đọc tiếp — phải đứng được một mình
- Mỗi dòng 1 ý, ngắn gọn — người đọc scroll nhanh
- Link để ở bio, không nhét vào thread
- Hashtag 0–2 cái hoặc không dùng

---

### MODE B — UGC / Creator-Style

**Nguyên tắc UGC — viết như người thật:**
- Thêm chi tiết cụ thể: ngày, con số, tên (dù mơ hồ cũng được: "hôm thứ 3 tuần trước")
- Thêm nhược điểm hoặc điều không hoàn hảo của sản phẩm → tăng credibility gấp đôi
- Tránh từ AI-sounding: "tuyệt vời", "hiệu quả vượt trội", "đừng bỏ lỡ", "cơ hội vàng"
- Tránh liệt kê: Điểm 1… Điểm 2… Điểm 3...
- Dùng câu không hoàn hảo, ngôn ngữ đời thường, câu ngắn xen câu dài
- Sản phẩm xuất hiện SAU khi đã có bối cảnh cảm xúc, không bao giờ mở đầu bằng tên sản phẩm

**7 Format UGC:**

#### 1. STORYTELLING
Kể câu chuyện thật có arc: vấn đề → hành trình → kết quả.
```
[Thời điểm cụ thể: "Tháng 3 năm ngoái..." / "Hôm thứ 6 tuần trước..."]
[Vấn đề xảy ra — mô tả cảm xúc thật, không lý trí]
[Đã thử gì, không hiệu quả như thế nào]
[Tìm/tình cờ gặp sản phẩm — mô tả tự nhiên]
[Kết quả — cụ thể, kể cả phần chưa hoàn hảo]
[Reflection ngắn — 1 câu bài học hoặc cảm nhận thật]
```

#### 2. RANT
Bức xúc thật về vấn đề → sản phẩm là giải pháp xuất hiện sau.
```
[Bức xúc mở đầu — đừng kìm nén, viết như đang nhắn tin cho bạn]
[Giải thích tại sao bực — càng cụ thể càng tốt]
[Đã thử X không hiệu quả — nêu tên cụ thể để realistic]
[Tìm ra giải pháp — tone bình thường, không hype]
[Kết quả thật — không cần drama]
```

#### 3. CONFESSION
Thú nhận điều gì đó → tạo đồng cảm → dẫn tự nhiên vào sản phẩm.
```
[Thú nhận điều đáng xấu hổ/ngại ngùng liên quan đến vấn đề]
[Giải thích hoàn cảnh tại sao lại thế — để người đọc hiểu]
[Điều gì đã thay đổi]
[Không cần kết luận hoành tráng — keep it real và human]
```

#### 4. BEFORE-AFTER
Mô tả trạng thái trước thật chi tiết → kết quả sau.
```
[TRƯỚC: Mô tả thật trạng thái cũ — càng chi tiết, cảm xúc càng nhiều càng tốt]
[Điểm chuyển tiếp: quyết định thay đổi hoặc tình cờ gặp giải pháp]
[SAU: Kết quả cụ thể — có con số, timeline nếu có]
[Điều CHƯA thay đổi hoặc điều còn phải cải thiện — giữ sự thật]
```

#### 5. MINI CASE STUDY
Dữ liệu nhỏ nhưng cụ thể — có số liệu, có timeline.
```
[Bối cảnh: ai (không cần tên thật), vấn đề gì, bắt đầu từ khi nào]
[Tuần 1 / Ngày 1–7: kết quả cụ thể]
[Tuần 2–3 / Ngày 8–21: kết quả tiếp theo]
[Kết quả tổng: số liệu thật]
[Nhận xét thật — kể cả điều tiêu cực hoặc hạn chế]
```

#### 6. DIARY ENTRY
Viết như nhật ký — gần gũi, thân mật.
```
[Ngày/thời điểm cụ thể]
"Hôm nay lần đầu tôi thử..."
[Mô tả cảm giác lúc đầu — thật, không cần phải tốt ngay]
[Điều bất ngờ xảy ra — tích cực hoặc tiêu cực]
[Sẽ update tiếp nếu... / Mình thấy cần thêm thời gian để...]
```

#### 7. FRIEND ADVICE
Viết như đang tư vấn cho bạn bè hỏi ý kiến.
```
[Bạn/người quen hỏi tôi về vấn đề X]
[Tôi đã nói với họ... — viết như đang kể lại cuộc trò chuyện]
[Lý do tôi recommend — cụ thể, không chung chung]
[Thứ tôi KHÔNG recommend kèm theo — honest advice]
```

---

### MODE C — Content Calendar

Tạo bảng lịch 7 hoặc 30 ngày:

| Ngày | Platform | Funnel | Pillar | Angle | Format | Hook mẫu | CTA |
|------|----------|--------|--------|-------|--------|----------|-----|
| T2 | FB | TOFU | [P1] | Relatable Pain | Rant | ... | Comment |
| T3 | Threads | MOFU | [P2] | Case Study | Mini case study | ... | Link bio |

Đảm bảo:
- Không dùng cùng angle 2 ngày liên tiếp
- Tỉ lệ value/story/sell theo giai đoạn từ `content-ratio.md`
- Xen kẽ Facebook và Threads nếu dùng cả hai

---

### MODE D — A/B Variants

Tạo 2–3 phiên bản của cùng 1 bài:
- Cùng body/nội dung chính
- Hook khác nhau (mỗi variant dùng 1 hook type khác)
- CTA có thể khác nhau

Label rõ ràng:
```
--- VARIANT A (Confession hook) ---
[bài]

--- VARIANT B (Số liệu hook) ---
[bài]

--- VARIANT C (Contrarian hook) ---
[bài]
```

---

## Human Check Checklist
Chạy trước khi output bài hoàn chỉnh:

- [ ] Dòng đầu đứng được một mình — không cần đọc phần sau vẫn hấp dẫn?
- [ ] Có ít nhất 1 chi tiết cụ thể (con số, ngày, tên, địa điểm)?
- [ ] Sản phẩm được nhắc sau khi đã có context cảm xúc?
- [ ] Có nhắc ít nhất 1 hạn chế hoặc điều không hoàn hảo của sản phẩm?
- [ ] Không có từ nào trong danh sách từ cần tránh bên dưới?
- [ ] Cấu trúc câu đa dạng (không phải tất cả đều ~15 chữ)?
- [ ] Chỉ có 1 CTA duy nhất?

**Từ cần tránh (AI-sounding / spam-sounding):**
tuyệt vời, hiệu quả vượt trội, đừng bỏ lỡ, cơ hội vàng, thần kỳ, đột phá,
bí quyết, sự thật bất ngờ (nếu overuse), 100% an toàn, kết quả ngoài mong đợi,
không thể tin được, cơ hội hiếm có, ưu đãi đặc biệt

## Output format
- Bài hoàn chỉnh, ready to post (copy-paste được)
- Với Threads: đánh số từng dòng (1/ 2/ 3/...)
- Với Calendar: bảng markdown đầy đủ
- Với A/B: label variant rõ ràng

Sau khi output → nhắc người dùng chạy qua `compliance-guard` trước khi đăng.

## Best practices
- Đọc `data/winning-patterns.md` trước — ưu tiên format đã proven
- Mỗi bài chỉ có 1 CTA chính — không pha lẫn "comment + click link + share"
- BOFU posts không bao giờ là bài đầu tiên tiếp cận cold audience
- UGC style hiệu quả nhất khi dựa trên trải nghiệm thật — nếu không có, hãy thành thật về điều đó
- Confession và Rant cần tone authentic — nếu bịa sẽ bị nhận ra ngay
