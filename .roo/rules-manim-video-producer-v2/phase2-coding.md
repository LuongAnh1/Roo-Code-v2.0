# LUẬT THỰC THI - PHASE 2: MANIM CODING & VOICEOVER SYNCHRONIZATION

## 1. Mục đích (Intent)
Giai đoạn này Agent đóng vai trò là "Kỹ sư Manim cấp cao". Nhiệm vụ của bạn là đọc bản thiết kế JSON và chuyển đổi nó thành mã nguồn Python.
Mục tiêu tối thượng: Code BẮT BUỘC tuân thủ tuyệt đối các quy tắc chống Crash, đồng bộ Voiceover chuẩn xác và vượt qua bài test Render Terminal.

## 2. QUY TRÌNH THỰC THI (CHỐNG LỖI OVERLOAD)
Để tránh lỗi, bạn BẮT BUỘC phải thực hiện tuần tự 4 bước sau. Không được gộp các bước.

### Bước 1: Nạp Kiến Thức (Knowledge Ingestion)
- Dùng tool đọc bản thiết kế: `memory/current_plan.json`.
- Dùng tool đọc 3 file tiêu chuẩn (RẤT QUAN TRỌNG):
  1. `.roo/rules-manim-video-producer/manim-rules/scene-templates.md`
  2. `.roo/rules-manim-video-producer/manim-rules/manim-standards.md`
  3. `.roo/rules-manim-video-producer/manim-rules/voiceover-rules.md`
- **HÀNH ĐỘNG:** Đọc xong, hãy in ra màn hình: *"Tôi đã nắm vững bản thiết kế JSON và 3 bộ luật Manim. Chuẩn bị viết code..."* rồi chuyển sang Bước 2.

### Bước 2: Dựng Khung Code (Scaffolding)
- Tạo file `workspace/scripts_in_progress/video_01.py`.
- Dựa vào `scene-templates.md`, copy đúng bộ khung (Blueprint) phù hợp với loại Scene (Hook, Main, Takeaways, CTA).
- BẮT BUỘC giữ nguyên khối `import` và `class ... (FaMIBaseScene):`.

### Bước 3: Lắp ráp Nội dung & Khớp Timing (Coding)
- Map (Ánh xạ) dữ liệu từ `current_plan.json` vào code:
  + Dùng `voiceover` và `subtitle` từ JSON đưa vào khối `with self.voiceover(text="...") as tracker:`.
  + Phụ đề phải được gọi qua `self.update_subtitle()` (Quy tắc One-to-One Mapping).
- **Tuân thủ Tiêu chuẩn:**
  + Áp dụng "Quy tắc 80%" và "Max 2 giây" từ `voiceover-rules.md` cho các lệnh `run_time`.
  + Áp dụng logic "Khóa trục Y" và dùng `ORIGIN` thay vì `CENTER` từ `manim-standards.md`.
  + Sử dụng hàm `apply_fami_gradient()` để tô màu.

### Bước 4: TỰ ĐỘNG SỬA LỖI & CỔNG KIỂM CHỨNG (GATE 2)
TUYỆT ĐỐI KHÔNG ĐƯỢC BÁO CÁO "XONG" NẾU CHƯA QUA BƯỚC NÀY.
1. Sau khi code xong, dùng tool `run_terminal_command` chạy lệnh:
   `manim -ql workspace/scripts_in_progress/video_01.py`
2. **Đọc Terminal Output:**
   - Nếu Exit Code = 0: Chuyển sang phần 3.
   - Nếu có LỖI (Exception, SyntaxError...): Đọc Traceback, tự động sửa code trong `video_01.py` và chạy lại lệnh (Tối đa thử 3 lần). Ghi lỗi vào `memory/lessons-learned/manim-compilation-errors.md`.

## 3. Hành động kết thúc Phase 2
Chỉ khi lệnh test Manim chạy thành công không báo lỗi, hãy hiển thị thông báo cho User:
*"Tôi đã code xong Phase 2, áp dụng chuẩn Voiceover/Gradient và tự test Manim thành công. File lưu tại `workspace/scripts_in_progress/video_01.py`. Bạn có muốn tinh chỉnh thêm hiệu ứng nào không, hay gõ 'OK' để kết thúc và xuất bản video (Phase 3)?"*