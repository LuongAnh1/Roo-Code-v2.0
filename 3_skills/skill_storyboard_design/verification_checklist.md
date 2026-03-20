# CHECKLIST KIỂM CHỨNG: storyboard_art_direction

Trước khi trình bày Storyboard cho người dùng, Agent BẮT BUỘC phải đối chiếu ý tưởng thiết kế với danh sách này. Mọi mục phải đạt trạng thái **PASS**.

| ID | Tiêu chí kiểm tra | Kết quả (PASS/FAIL) | Ghi chú sửa đổi |
|:---|:---|:---:|:---|
| 1 | **Né Dead Zone Đỉnh?** Đảm bảo không có chi tiết nào (trừ Logo) vượt quá Y = +5.5. | | |
| 2 | **Né Dead Zone Đáy?** Đảm bảo không có chi tiết nội dung nào thấp hơn Y = -4.0. | | |
| 3 | **Tránh vùng nút TikTok?** Các thông tin quan trọng đã dạt sang trái hoặc nằm giữa (né X > +3.8) chưa? | | |
| 4 | **Tính trực quan?** Ý tưởng có sử dụng hình khối/ẩn dụ không, hay chỉ hiện toàn chữ (dry text)? | | |
| 5 | **Giới hạn từ ngữ?** Các đoạn text hiển thị trên màn hình có đảm bảo **dưới 15 từ** mỗi cụm không? | | |
| 6 | **Sử dụng Paragraph?** Nếu text > 8 từ, đã lên kế hoạch dùng `Paragraph()` để ngắt dòng thay vì `Text()` chưa? | | |
| 7 | **Tỷ lệ 80%?** Các hành động có khớp với thời lượng thoại (để dư 20% thời gian cuối) không? | | |

---

### 🚨 LỆNH THỰC THI CHO AGENT:
- **Nếu FAIL mục 1, 2, 3:** Bắt buộc điều chỉnh tọa độ Y và X dựa trên `2_knowledge/aesthetics_architecture.md`.
- **Nếu FAIL mục 4:** Tự động đề xuất lại ít nhất 1 phương án sử dụng hình khối (Circle, Square, Arrow) thay thế.
- **Nếu FAIL mục 5, 6:** Chủ động cắt ngắn từ ngữ hoặc chia thành nhiều nhịp xuất hiện khác nhau.

### ✍️ XÁC NHẬN CỦA AGENT:
Agent phải ghi dòng này vào cuối bản Storyboard:
*"Tôi đã tự kiểm chứng qua `3_skills/skill_storyboard_design/verification_checklist.md` và xác nhận thiết kế đạt chuẩn an toàn (PASS)."*