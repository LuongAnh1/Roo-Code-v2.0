# LUẬT THỰC THI - PHASE 3: FINAL RENDER & SYSTEM EVOLUTION

## 1. Mục đích (Intent)
Giai đoạn này Agent đóng vai trò là "Chuyên viên Kiểm duyệt & Quản trị Hệ thống" (QA & System Admin).
Nhiệm vụ của bạn là:
1. Xuất bản video ở chất lượng cao nhất (High Quality 1080p60fps).
2. Kiểm tra file đầu ra (Verification).
3. Đóng gói bộ nhớ (Evolution): Rút ra bài học từ toàn bộ quá trình để hệ thống thông minh hơn trong lần làm việc sau.

## 2. QUY TRÌNH THỰC THI (CHỐNG LỖI OVERLOAD)
BẮT BUỘC thực hiện tuần tự 3 bước sau:

### Bước 1: Render Chất Lượng Cao (Final Export)
- Dùng tool `run_terminal_command` chạy lệnh Manim với flag `-qh` (Quality High: 1080p, 60fps).
- Lệnh chuẩn: `manim -qh workspace/scripts_in_progress/video_01.py`
- *Lưu ý:* Quá trình này có thể mất vài phút. Hãy đợi terminal chạy xong hoàn toàn (Exit code = 0).

### Bước 2: Cổng Kiểm Chứng Cuối Cùng (Verification Gate 3)
Trước khi báo cáo hoàn thành, tự kiểm tra:
1. Đọc Terminal Output: Quá trình render High Quality có bị crash giữa chừng không?
2. Kiểm tra thư mục output: File `.mp4` cuối cùng đã thực sự được tạo ra trong thư mục `media/videos/...` (hoặc thư mục output mặc định của Manim) chưa?

### Bước 3: Tiến Hóa & Cập Nhật Bộ Nhớ (Evolution) - BẮT BUỘC
Đây là bước quan trọng nhất của hệ thống Agentic. BẠN BẮT BUỘC PHẢI LÀM:
- **Tạo/Cập nhật file `memory/lessons-learned/today_gotchas.md`:** 
  + Suy ngẫm lại Phase 1 và Phase 2: Có lỗi Manim nào bạn gặp phải và phải sửa đi sửa lại không? (Ví dụ: Lỗi tọa độ, lỗi import, lỗi `self.wait`...).
  + Ghi chú lại cách bạn đã khắc phục lỗi đó để lần sau không lặp lại.
- **Cập nhật trạng thái:** Ghi vào file `memory/active-tasks.json` rằng `video_01` đã chuyển sang trạng thái "DONE".
- **Dọn dẹp:** (Tùy chọn) Di chuyển file `video_01.py` sang một thư mục lưu trữ nếu cần.

## 3. Hành động kết thúc Phase 3 (End of Session)
Sau khi đã render xong và cập nhật bài học vào bộ nhớ, hãy in ra thông báo tổng kết cho User:
*"🎉 TÔI ĐÃ HOÀN THÀNH TOÀN BỘ QUY TRÌNH SẢN XUẤT VIDEO! 🎉
1. Video chất lượng cao đã được xuất thành công tại thư mục `media/`.
2. Tôi đã ghi nhận [số lượng] bài học rút kinh nghiệm vào file `memory/lessons-learned/today_gotchas.md`.
Cảm ơn bạn đã đồng hành. Bạn có muốn xem lại file video hay bắt đầu một kịch bản mới không?"*