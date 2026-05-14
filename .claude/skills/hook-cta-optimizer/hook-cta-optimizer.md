---
name: hook-cta-optimizer
description: Tối ưu hook và CTA cho content affiliate — tăng stop rate, click rate, conversion; tạo A/B variants; đọc từ winning-patterns
metadata:
  type: skill
  platforms: [facebook, threads]
  layer: optimization
---

# Hook & CTA Optimizer

## Purpose
Hook quyết định có ai đọc bài không — CTA quyết định có ai click link không. Cả hai cần tối ưu riêng biệt và liên tục học từ data thực tế. Skill này chạy sau khi bài đã viết xong, trước khi đăng.

**Luật 3 giây:** Người dùng Facebook quyết định đọc tiếp hay không trong 3 giây đầu. Threads thậm chí còn ít hơn — chỉ cần 1 dòng.

## When to use
- Trước khi đăng bất kỳ bài affiliate nào
- Khi bài đang có reach tốt nhưng click affiliate thấp (CTA yếu)
- Khi bài đang có engagement thấp (hook yếu)
- Khi muốn tạo A/B hook để test

**Trigger phrases:** "tối ưu hook", "viết lại CTA", "hook mạnh hơn", "tăng click affiliate", "A/B hook", "câu mở đầu hay hơn"

## Inputs needed
1. Bài đăng cần tối ưu (paste toàn bộ vào)
2. Nền tảng: Facebook hay Threads?
3. Mục tiêu bài: tăng reach / tăng comment / tăng click link?
4. Funnel stage: TOFU / MOFU / BOFU?

Đọc trước:
- `data/performance-memory.json` → `winning_hooks` và `winning_cta_patterns`
- `data/winning-patterns.md` → patterns đang hoạt động tốt

## Workflow

---

### PHẦN 1 — HOOK DIAGNOSTIC

Đánh giá hook hiện tại theo 4 tiêu chí (mỗi tiêu chí 1–5 điểm):

**1. Curiosity (Tò mò):** Hook có tạo ra câu hỏi chưa được trả lời trong đầu người đọc không?
**2. Relevance (Liên quan):** Người trong ICP có thấy bài này viết về mình không?
**3. Specificity (Cụ thể):** Có con số, chi tiết, hoặc tình huống cụ thể không?
**4. Pattern Interrupt (Khác biệt):** Có phá vỡ kỳ vọng, khác với bài thông thường họ scroll qua không?

**Kết luận:**
- Tổng > 14: Hook tốt — giữ nguyên, chỉ fine-tune
- Tổng 10–14: Hook khá — nên tạo 1 variant tốt hơn để test
- Tổng < 10: Hook yếu — phải viết lại

---

### PHẦN 2 — HOOK LIBRARY

**8 loại hook — chọn đúng loại cho mục tiêu:**

**1. NUMBER HOOK** — Dùng số liệu gây bất ngờ
```
Template: "[Con số bất ngờ] về [chủ đề] mà ít ai biết"
Ví dụ FB: "73% người tập gym hơn 6 tháng không thấy kết quả — đây là lý do."
Ví dụ Threads: "6 tháng. 0 kg giảm. Lý do tôi tìm ra sau đó khiến tôi muốn bắt đầu lại từ đầu."
Best for: Reach, Share
```

**2. QUESTION HOOK** — Câu hỏi kích thích tự kiểm tra
```
Template: "Bạn có [dấu hiệu/đặc điểm] này không? Đây là điều bạn cần biết."
Ví dụ FB: "Bạn có hay đói lúc 3–4 giờ chiều dù đã ăn đủ bữa trưa? Đây là điều cơ thể đang báo hiệu."
Ví dụ Threads: "Hay mệt sau 2 tiếng làm việc dù ngủ 8 tiếng? Đọc tiếp."
Best for: Engagement, Comment
```

**3. CONFESSION HOOK** — Thú nhận tạo vulnerability
```
Template: "Tôi phải thú nhận [điều thật, đáng ngại ngùng]..."
Ví dụ FB: "Tôi phải thú nhận: Tôi đã trả tiền cho 3 chương trình giảm cân khác nhau mà không theo đến cuối cái nào."
Ví dụ Threads: "Tôi từng là người nói 'diet không hiệu quả với tôi'. Tôi đã sai."
Best for: Trust, TOFU
```

**4. MISTAKE HOOK** — Sai lầm làm người đọc muốn tránh
```
Template: "Tôi đã [tốn X / mất X] vì không biết điều này — đừng lặp lại sai lầm của tôi"
Ví dụ FB: "Tôi đã tốn 8 tháng tập sai trước khi ai đó chỉ cho tôi điều này. 8 tháng."
Ví dụ Threads: "Sai lầm lớn nhất tôi làm năm 28 tuổi liên quan đến sức khỏe. Giờ tôi 32 và vẫn đang trả giá."
Best for: MOFU, Convert
```

**5. PREDICTION HOOK** — Tạo urgency tự nhiên không spam
```
Template: "Trong [thời gian], [consequence] nếu không [hành động]"
Ví dụ FB: "5 năm nữa, ai không xây thói quen này từ bây giờ sẽ mất thêm 10 lần công sức để thay đổi."
Ví dụ Threads: "2027: Người nào không hiểu về [chủ đề] sẽ ở đâu so với người bắt đầu từ hôm nay?"
Best for: TOFU, Viral
```

**6. CONTRARIAN HOOK** — Phản bác số đông
```
Template: "Mọi người đều làm [X], nhưng đó chính xác là lý do [kết quả xấu]"
Ví dụ FB: "Mọi người đều đếm calories. Và đó chính xác là lý do nhiều người không giảm được cân dù ăn rất ít."
Ví dụ Threads: "Hot take: Ý chí không phải vấn đề của bạn. Môi trường mới là."
Best for: Reach, Debate, Threads viral
```

**7. RELATABLE PAIN HOOK** — Chạm đúng cảm xúc phổ biến
```
Template: "Ai mà không [cảm giác/tình huống cụ thể và quen thuộc]?"
Ví dụ FB: "Ai mà không bực khi mặc đồ cũ vào thấy tight hơn mà mình không làm gì khác đi?"
Ví dụ Threads: "Cái cảm giác muốn thay đổi mà không biết bắt đầu từ đâu. Ai hiểu?"
Best for: Reach, Share, TOFU
```

**8. CURIOSITY GAP HOOK** — Tạo khoảng trống thông tin
```
Template: "Điều tôi không nói trong bài trước là... / Cái tôi chưa kể là..."
Ví dụ FB: "Điều tôi không nói trong bài giảm cân tuần trước — phần khó nhất không phải ăn kiêng."
Ví dụ Threads: "Update: Điều xảy ra ở tuần thứ 3 mà tôi không expect."
Best for: Retention, Return audience
```

---

### PHẦN 3 — TẠO 3 HOOK VARIANTS

Dựa trên bài đã có, viết 3 hook thay thế:

**Variant A:** Lấy từ `winning_hooks` trong `performance-memory.json` nếu có — áp dụng pattern đã proven
**Variant B:** Hook type phù hợp nhất với mục tiêu bài (chọn trong 8 loại trên)
**Variant C:** Hook type hoàn toàn khác Variant A và B

Với mỗi variant, giải thích ngắn: "Hook này hoạt động vì [tâm lý/lý do cụ thể]"

---

### PHẦN 4 — CTA DIAGNOSTIC

Đánh giá CTA hiện tại:
- Có đúng 1 hành động rõ ràng không? (không kêu gọi 2 việc cùng lúc)
- Friction có thấp không? (dễ làm: comment 1 từ dễ hơn click link)
- Có phù hợp với funnel stage không?

---

### PHẦN 5 — CTA LIBRARY

**Mục tiêu TOFU: Tăng engagement, comment**
```
"Comment [từ/emoji] bên dưới nếu bạn cũng từng [pain này]"
"Bạn đang ở giai đoạn [A] hay [B]? Comment nhé — tôi tò mò"
"Tag người bạn đang [gặp vấn đề tương tự] — họ cần đọc điều này"
"Bạn đã thử [giải pháp X] chưa? Share kết quả bên dưới"
```

**Mục tiêu MOFU: Tăng save, warm up**
```
"Save bài này lại — bạn sẽ cần khi [tình huống cụ thể xảy ra]"
"Follow để tôi update kết quả [tuần tới / sau 30 ngày]"
"Comment '[keyword]' để tôi gửi thêm thông tin chi tiết"
```

**Mục tiêu BOFU: Tăng click link affiliate**
```
Facebook (không để link thẳng):
"Tên đầy đủ: [tên sản phẩm]. Tìm link ở comment đầu tiên bên dưới."
"Comment '[keyword]' để mình gửi link trực tiếp cho bạn"
"DM mình chữ '[X]' — mình gửi link + hướng dẫn chọn loại phù hợp"

Threads:
"Link đầy đủ ở bio — tìm mục [tên sản phẩm]"
"Tên: [sản phẩm]. Link ở bio."
```

**Quy tắc chọn CTA theo funnel:**
- TOFU → Comment / Tag / Share (friction thấp, không cần click link)
- MOFU → Save / Follow / Comment để nhận info
- BOFU → Click link (ẩn) / DM / Comment keyword

---

### PHẦN 6 — FINAL OUTPUT

Trả về đầy đủ:
1. Điểm hook hiện tại (4 tiêu chí + tổng) + nhận xét
2. 3 hook variants với giải thích ngắn từng cái
3. Đánh giá CTA hiện tại + issue nếu có
4. CTA tối ưu + 1 backup CTA
5. Bài hoàn chỉnh với hook tốt nhất + CTA tốt nhất — ready to post

---

## Best practices
- Hook Facebook: dòng đầu tối đa 125 ký tự (giới hạn "Xem thêm")
- Hook Threads: phải đủ sức kéo chỉ với 1 dòng — giả định người đọc sẽ không đọc tiếp nếu dòng 1 không hấp dẫn
- Không dùng CTA "Click ngay" hay "Mua ngay" — đây là CTA spam trigger
- 1 bài 1 CTA — không mix "comment + click link + share" trong cùng 1 bài
- Sau khi có performance data → cập nhật `winning_hooks` trong `data/performance-memory.json`
- Hook Confession và Relatable Pain tốt cho TOFU; Mistake và Case Study tốt cho MOFU-BOFU
