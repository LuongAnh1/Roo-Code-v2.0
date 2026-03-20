# SKILL: auto_debug_&_self_healing

## 🎯 Purpose (Mục đích)
Tự động phân tích, chẩn đoán và sửa lỗi mã nguồn khi lệnh render Terminal (`manim -pql`) thất bại. Mục tiêu là render thành công video mà không cần sự can thiệp của con người.

## 📥 Required Resources (Công cụ hỗ trợ)
- **Traceback:** Nội dung lỗi từ Terminal.
- **Tri thức tiến hóa:** `evolution/lessons_learned.md` (Để xem các lỗi tương tự đã sửa).
- **Kiểm chứng trực tiếp:** Lệnh `python -c "import manim; help(manim.ClassName)"` để kiểm tra API thật trên máy.

## ⚙️ Execution Approach (Quy trình chẩn đoán 4 bước)

### Bước 1: Đọc và Phân loại lỗi (Diagnosis)
Agent phải đọc dòng cuối cùng của Traceback để xác định loại "bệnh":
1. **ModuleNotFoundError**: Lỗi đường dẫn/import (Kiểm tra Hack Path).
2. **IndexError / AttributeError**: Lỗi thao tác trên vật thể rỗng (Kiểm tra VGroup/match_y).
3. **NameError**: Lỗi thiếu biến/thư viện (Kiểm tra import numpy/math).
4. **ValueError**: Lỗi tham số (Ví dụ: wait thời gian âm).
5. **EncodingError**: Lỗi ký tự lạ/Unicode (Kiểm tra MarkupText/UTF-8).

### Bước 2: Truy xuất bộ nhớ (Retrieval)
Mở file `evolution/lessons_learned.md`. Tìm kiếm xem lỗi này đã có trong danh sách "Gotchas" chưa. Nếu có, áp dụng ngay giải pháp `✅ ĐÚNG`.

### Bước 3: Thử nghiệm sửa đổi (Remediation)
1. Thực hiện sửa code dựa trên chẩn đoán.
2. Nếu không chắc chắn về hàm, dùng công cụ Terminal chạy lệnh `python -c` để hỏi trực tiếp thư viện Manim.
3. Chạy lại lệnh render nháp `-pql`.

### Bước 4: Lưu vết tiến hóa (Evolution) - QUAN TRỌNG
Nếu lỗi vừa gặp là **LỖI MỚI** (chưa có trong nhật ký):
- Agent **BẮT BUỘC** sử dụng công cụ `edit_file` để cập nhật lỗi đó vào mục `## 10. CÁC LỖI MỚI TỰ HỌC` trong tệp `5_evolution/lessons_learned.md` theo format ❌/✅.

## 📤 Output Standard (Báo cáo kết quả)
Sau khi tự sửa thành công, Agent báo cáo cho người dùng:
> "📍 [Auto-Debug]: Đã phát hiện lỗi [Tên Lỗi]. Nguyên nhân: [...]. Cách đã sửa: [...]. Đã cập nhật bài học vào `lessons_learned.md`. Video đã render xong!"

## ✅ Verification Protocol
- [ ] Tôi đã tự đọc Traceback thay vì hỏi người dùng chưa?
- [ ] Tôi đã kiểm tra file `reference_errors.md` trước khi sửa chưa?
- [ ] Tôi đã lưu lỗi mới (nếu có) vào nhật ký tiến hóa chưa?
