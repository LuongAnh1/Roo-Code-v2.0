# CHECKLIST KIỂM CHỨNG: storyboard_art_direction

Agent BẮT BUỘC thực hiện rà soát Storyboard dựa trên Checklist này trước khi báo cáo kết quả cho người dùng.

| ID | Tiêu chí kiểm tra | PASS/FAIL | Hành động khắc phục |
|:---|:---|:---:|:---|
| 1 | **Vùng An Toàn (Dead Zones):** Mọi vật thể có nằm trong khoảng Y từ [-3.5, 4.0] không? | | Dời vị trí về vùng an toàn. |
| 2 | **Tỷ lệ Logo:** Đã xác nhận Logo không bị che lấp bởi Tiêu đề chưa? | | Dùng `self.create_title()` để tự động căn lề. |
| 3 | **Tránh tràn viền (Horizontal):** Các cụm nội dung có vượt quá 7.5 units chiều ngang không? | | Ép `.scale_to_fit_width(7.5)`. |
| 4 | **Tính Trực quan:** Có ít nhất 1 ẩn dụ hình học (Icon, Graph, Shape) không, hay chỉ toàn chữ? | | Thay Text bằng Icon/Shape. |
| 5 | **Phụ đề song ngữ:** Đã lên kế hoạch gọi `update_subtitle` cho các phân đoạn thoại chưa? | | Thêm vào kịch bản chuyển động. |
| 6 | **Pacing (80%):** Các hành động (Animation) có thời lượng chiếm tối đa 0.8 * duration thoại không? | | Chia nhỏ Animation hoặc tăng tốc độ. |

---

## 🚨 GIAO THỨC XỬ LÝ KẾT QUẢ
- **Nếu PASS tất cả:** Agent được phép trình bày Storyboard cho người dùng.
- **Nếu có 1 mục FAIL:** 
  1. Agent KHÔNG ĐƯỢC gửi báo cáo cho người dùng.
  2. Agent phải tự chỉnh sửa Storyboard cho đến khi tất cả các mục đều PASS.
  3. Sau khi sửa xong, cập nhật lại logic vào `evolution/lessons_learned.md` nếu đó là một vấn đề phổ biến.

## ✍️ XÁC NHẬN CỦA AGENT
Agent phải chốt tin nhắn báo cáo bằng dòng sau:
> *"Tôi đã đối chiếu Storyboard với `verification/layout_checklist.md` và xác nhận đạt chuẩn (PASS) cho toàn bộ 6 tiêu chí."*