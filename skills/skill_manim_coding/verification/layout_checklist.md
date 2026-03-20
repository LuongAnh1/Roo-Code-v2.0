# CHECKLIST KIỂM CHỨNG: manim_pro_coding (FINAL VERIFICATION)

Trước khi chạy lệnh render `manim -pql`, Agent BẮT BUỘC phải đối chiếu mã nguồn với danh sách này. Mọi mục phải đạt trạng thái **PASS**.

| ID | Tiêu chí kỹ thuật & Thẩm mỹ | PASS/FAIL | Hành động khắc phục |
|:---|:---|:---:|:---|
| 1 | **Import chuẩn:** Đã có Hack Path (sys.path) và `from execution.fami_lib import *` chưa? | | Dán từ file templates. |
| 2 | **Subtitle Chunking:** Phụ đề đã được chia nhỏ theo từng hành động (1 action = 1 subtitle)? | | Dùng `self.update_subtitle(text)` trước mỗi lệnh `play`. |
| 3 | **Bản vá 80%:** Tổng `run_time` các animation trong khối `voiceover` có $\le 0.8 \times duration$ không? | | Giảm `run_time` hoặc tăng tốc độ hiệu ứng. |
| 4 | **Chống tràn ngang:** Các VGroup nội dung chính đã có `.scale_to_fit_width(7.5)` chưa? | | Thêm lệnh kiểm tra `.width > 7.5`. |
| 5 | **Khóa trục Y (Typing):** Hiệu ứng gõ chữ đã dùng `.match_y()` và vòng lặp `if char == " ":` chưa? | | Sửa vòng lặp theo chuẩn "Locked Y-axis". |
| 6 | **Vùng Stage:** Nội dung có nằm trong vùng an toàn (Y: -3.5 đến +4.0) không? | | Dùng `next_to(self.logo, DOWN, ...)` để dời. |
| 7 | **Gradient chuẩn:** Đã dùng `apply_fami_gradient()` thay vì tự gán `.set_color()` thủ công chưa? | | Gọi skill `apply_fami_gradient(obj)`. |

---

### 🚨 LỆNH THỰC THI & NGHIỆM THU:
- **Nguyên tắc "Zero-Bug Tolerance":** Nếu có bất kỳ mục nào **FAIL**, Agent **TUYỆT ĐỐI KHÔNG** được chạy lệnh render. Hãy quay lại sửa code cho đến khi đánh dấu **PASS** tất cả.
- **Reporting:** Khi nộp video nháp (mp4), Agent phải viết: 
  > *"Tôi xác nhận mã nguồn đã vượt qua kiểm chứng `layout_checklist.md` (Mục 1-7 đều đạt PASS)."*

---
## 🏁 EXIT PROTOCOL
Sau khi nhận lệnh "OK/Tiếp tục" từ người dùng, hãy mở `master_runbook.md` để xác định phân cảnh tiếp