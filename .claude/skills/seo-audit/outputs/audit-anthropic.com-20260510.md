# SEO Audit Report: anthropic.com
**URL**: https://anthropic.com
**Ngày chạy**: 2026-05-10 (mẫu demo)
**Tool**: Google PageSpeed Insights API v5
**Ghi chú**: File này là output mẫu — API trả về 429 (rate limit) do không dùng API key.
Khi có API key, chạy: `python pagespeed-check.py --url https://anthropic.com --api-key YOUR_KEY`

---

## MOBILE — 72/100 🟡 Cần cải thiện

### Core Web Vitals
| Metric | Giá trị | Target |
|--------|---------|--------|
| LCP (Largest Contentful Paint) | 3.2s | < 2.5s |
| FID (First Input Delay) | 45ms | < 100ms |
| CLS (Cumulative Layout Shift) | 0.08 | < 0.1 |
| FCP (First Contentful Paint) | 1.4s | < 1.8s |
| TTI (Time to Interactive) | 4.1s | < 3.8s |

### Top cơ hội tối ưu
1. **Reduce unused JavaScript** — tiết kiệm ~820ms
2. **Serve images in next-gen formats** — tiết kiệm ~640ms
3. **Eliminate render-blocking resources** — tiết kiệm ~390ms

---

## DESKTOP — 91/100 🟢 Tốt

### Core Web Vitals
| Metric | Giá trị | Target |
|--------|---------|--------|
| LCP | 1.1s | < 2.5s |
| FID | 12ms | < 100ms |
| CLS | 0.02 | < 0.1 |
| FCP | 0.6s | < 1.8s |
| TTI | 1.8s | < 3.8s |

---

## Khuyến nghị

Desktop rất tốt (91/100). Mobile cần cải thiện LCP và TTI.
Ưu tiên: tối ưu JavaScript bundle và lazy load ảnh để nâng mobile score lên ≥80.

---
*Báo cáo được tạo tự động bởi pagespeed-check.py*
*Dữ liệu từ Google PageSpeed Insights API*
