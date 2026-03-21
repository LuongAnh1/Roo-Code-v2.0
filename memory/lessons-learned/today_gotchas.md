# Lỗi gặp phải và Bài học kinh nghiệm (Gotchas)

## 1. Lỗi thiếu thư viện `googletrans`
- **Tình trạng:** Khi chạy code Manim, terminal báo lỗi `ModuleNotFoundError: No module named 'googletrans'`.
- **Nguyên nhân:** Môi trường bị thiếu dependency nội bộ của `skills/fami_lib.py`.
- **Cách khắc phục:** Cài đặt thông qua lệnh `pip install googletrans==4.0.0-rc1`. Rút kinh nghiệm cần check môi trường cẩn thận.

## 2. Lỗi tham số khởi tạo của `BarChart`
- **Tình trạng:** Báo lỗi `TypeError: Mobject.__init__() got an unexpected keyword argument 'width'` tại hàm `BarChart`.
- **Nguyên nhân:** Truyền sai tham số kích thước thẳng vào constructor của `BarChart`.
- **Cách khắc phục:** Loại bỏ `width`, `height` trong `BarChart(...)` và chuyển sang sử dụng hàm `.scale()` để điều chỉnh kích thước: `BarChart(...).scale(0.5)`.

## 3. Lỗi lược bớt kịch bản (Shortcut Issue)
- **Tình trạng:** Code không đủ 21 phân cảnh như trong file `current_plan.json`.
- **Nguyên nhân:** Cố gắng test nhanh quy trình bằng file code rút gọn.
- **Cách khắc phục:** Tuân thủ 100% nguyên tắc "Map dữ liệu 1-1", viết đầy đủ toàn bộ logic và hiệu ứng cho toàn bộ Voiceover đã phân rã.