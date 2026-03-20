# MANIM API CHEAT SHEET (FA MI EDITION)

Tài liệu này dùng để tra cứu nhanh cú pháp, KHÔNG ĐƯỢC dùng thay thế cho các Skill trong `fami_lib.py`.

## 1. HÌNH KHỐI CƠ BẢN (GEOMETRY)
- **Hình chữ nhật:** `Rectangle(width=4, height=2, color=WHITE, fill_opacity=0.2)`
- **Hình tròn:** `Circle(radius=1.5, color=WHITE)`
- **Hình chữ nhật bo góc:** `RoundedRectangle(corner_radius=0.2, height=1.0, width=7.5)`
- **Đường thẳng:** `Line(start=LEFT*2, end=RIGHT*2, buff=0.1)`
- **Mũi tên:** `Arrow(start=LEFT, end=RIGHT, buff=0.1, color=FAMI_CYAN)`

## 2. VĂN BẢN & CÔNG THỨC (TYPOGRAPHY & MATH)
- **Text thường:** `Text("Nội dung", font="Segoe UI", font_size=40)`
- **Nhiều dòng:** `Paragraph("Dòng 1", "Dòng 2", alignment="center")`
- **Markup (Tô màu từng từ):** 
  `MarkupText('Từ <span color="#00d4ff">đặc biệt</span>', font="Segoe UI")`
- **Công thức Toán học (LaTeX):**
  - Luôn dùng: `MathTex(r"công_thức", font_size=60)`
  - Quy tắc: Luôn thêm tiền tố `r` trước chuỗi.
  - Phân số: `r"\frac{a}{b}"`
  - Chỉ số: `r"x_i"`, `r"x^2"`
  - Ký hiệu: `r"\infty"`, `r"\sum_{n=1}^{\infty}"`

## 3. CĂN LỀ & BỐ CỤC (LAYOUT TOOLS)
- **Căn giữa:** `obj.center()`
- **Căn lề:** `obj.next_to(target, direction, buff=0.5)`
- **Ép chiều ngang:** `if obj.width > 7.5: obj.scale_to_fit_width(7.5)`
- **Căn trục Y:** `obj.match_y(target_obj)` (Dùng để khóa trục Y cho chữ khi chạy hiệu ứng Typing).

## 4. HIỆU ỨNG (ANIMATIONS)
- **Xuất hiện cơ bản:** `self.play(FadeIn(obj, shift=UP*0.5), run_time=1.0)`
- **Hiệu ứng Juicy:** `self.play(FadeIn(obj, scale=0.5), rate_func=rate_functions.ease_out_back)`
- **Biến đổi:** `self.play(ReplacementTransform(old_obj, new_obj))`
- **Nhấn mạnh:** `self.play(Indicate(obj, color=ACCENT))`

## 5. BẢNG MÀU THƯƠNG HIỆU (BRAND CONSTANTS)
Khi cần màu, Agent PHẢI dùng các biến đã định nghĩa trong `fami_lib.py`:
- `FAMI_BLUE` (#005BAA)
- `FAMI_CYAN` (#45C4D9)
- `FAMI_SUB` (#DFE858)
- `ACCENT` (#fffa65)
- `DANGER` (#ff4d4d)
- `SUCCESS` (#00e676)
- `TEXT_COLOR` (WHITE)