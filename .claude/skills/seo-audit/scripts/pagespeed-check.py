"""
pagespeed-check.py
Gọi Google PageSpeed Insights API và xuất báo cáo SEO.
Không cần API key cho cơ bản (100 requests/ngày miễn phí).
"""

import urllib.request
import json
import argparse
import os
from datetime import datetime


API_URL = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"


def fetch_pagespeed(url, strategy="mobile", api_key=None):
    params = f"?url={urllib.parse.quote(url)}&strategy={strategy}"
    if api_key:
        params += f"&key={api_key}"
    full_url = API_URL + params

    try:
        with urllib.request.urlopen(full_url, timeout=30) as response:
            return json.loads(response.read().decode())
    except Exception as e:
        print(f"  Lỗi khi gọi API: {e}")
        return None


def parse_results(data, strategy):
    if not data:
        return None

    cats = data.get("lighthouseResult", {}).get("categories", {})
    audits = data.get("lighthouseResult", {}).get("audits", {})
    metrics = audits.get("metrics", {}).get("details", {}).get("items", [{}])[0]

    score = int((cats.get("performance", {}).get("score", 0) or 0) * 100)

    def ms(key):
        val = metrics.get(key, 0) or 0
        return f"{val/1000:.2f}s" if val >= 1000 else f"{val}ms"

    def score_label(s):
        if s >= 90: return "🟢 Tốt"
        if s >= 50: return "🟡 Cần cải thiện"
        return "🔴 Kém"

    lcp = metrics.get("largestContentfulPaint", 0) or 0
    cls = (audits.get("cumulative-layout-shift", {})
                 .get("displayValue", "0").replace(" ", ""))

    opportunities = []
    for key, audit in audits.items():
        if audit.get("score") is not None and audit.get("score") < 0.9:
            savings = (audit.get("details", {})
                           .get("overallSavingsMs", 0) or 0)
            if savings > 200:
                opportunities.append({
                    "title": audit.get("title", key),
                    "savings_ms": savings,
                    "description": audit.get("description", "")[:120]
                })

    opportunities.sort(key=lambda x: x["savings_ms"], reverse=True)

    return {
        "strategy": strategy,
        "score": score,
        "score_label": score_label(score),
        "lcp": ms("largestContentfulPaint"),
        "lcp_raw": lcp,
        "fid": ms("maxPotentialFid"),
        "cls": cls,
        "fcp": ms("firstContentfulPaint"),
        "tti": ms("interactive"),
        "opportunities": opportunities[:5]
    }


def generate_report(url, results, output_dir=None):
    domain = url.replace("https://", "").replace("http://", "").split("/")[0]
    date = datetime.now().strftime("%Y-%m-%d %H:%M")
    date_file = datetime.now().strftime("%Y%m%d-%H%M")

    lines = []
    lines.append(f"# SEO Audit Report: {domain}")
    lines.append(f"**URL**: {url}")
    lines.append(f"**Ngày chạy**: {date}")
    lines.append(f"**Tool**: Google PageSpeed Insights API v5")
    lines.append("")

    for r in results:
        if not r:
            continue
        lines.append(f"## {r['strategy'].upper()} — {r['score']}/100 {r['score_label']}")
        lines.append("")
        lines.append("### Core Web Vitals")
        lines.append(f"| Metric | Giá trị | Target |")
        lines.append(f"|--------|---------|--------|")
        lines.append(f"| LCP (Largest Contentful Paint) | {r['lcp']} | < 2.5s |")
        lines.append(f"| FID (First Input Delay) | {r['fid']} | < 100ms |")
        lines.append(f"| CLS (Cumulative Layout Shift) | {r['cls']} | < 0.1 |")
        lines.append(f"| FCP (First Contentful Paint) | {r['fcp']} | < 1.8s |")
        lines.append(f"| TTI (Time to Interactive) | {r['tti']} | < 3.8s |")
        lines.append("")

        if r["opportunities"]:
            lines.append("### Top cơ hội tối ưu")
            for i, opp in enumerate(r["opportunities"], 1):
                saved = f"~{opp['savings_ms']}ms"
                lines.append(f"{i}. **{opp['title']}** — tiết kiệm {saved}")
            lines.append("")

    lines.append("---")
    lines.append("*Báo cáo được tạo tự động bởi pagespeed-check.py*")

    report = "\n".join(lines)
    print(report)

    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
        filename = os.path.join(output_dir, f"audit-{domain}-{date_file}.md")
        with open(filename, "w", encoding="utf-8") as f:
            f.write(report)
        print(f"\n✅ Đã lưu báo cáo: {filename}")

    return report


def main():
    import urllib.parse

    parser = argparse.ArgumentParser(description="Google PageSpeed Insights Audit")
    parser.add_argument("--url", required=True, help="URL cần kiểm tra")
    parser.add_argument("--strategy", default="mobile",
                        choices=["mobile", "desktop", "both"],
                        help="Thiết bị (mobile/desktop/both)")
    parser.add_argument("--output", default=None,
                        help="Thư mục lưu báo cáo (để trống = chỉ in ra terminal)")
    parser.add_argument("--api-key", default=None,
                        help="API key (tùy chọn — không có vẫn chạy được)")
    args = parser.parse_args()

    url = args.url
    if not url.startswith("http"):
        url = "https://" + url

    strategies = ["mobile", "desktop"] if args.strategy == "both" else [args.strategy]
    results = []

    for s in strategies:
        print(f"\n⏳ Đang kiểm tra {s.upper()}: {url}")
        data = fetch_pagespeed(url, s, args.api_key)
        r = parse_results(data, s)
        if r:
            results.append(r)
            print(f"   Điểm: {r['score']}/100 {r['score_label']}")

    if results:
        print("\n" + "="*50)
        generate_report(url, results, args.output)


if __name__ == "__main__":
    main()
