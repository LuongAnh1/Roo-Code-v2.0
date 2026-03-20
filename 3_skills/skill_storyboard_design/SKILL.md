# SKILL: storyboard_art_direction

## 🎯 Purpose (Mục đích)
Chuyển đổi Lời thoại (Voiceover) thành các Ý tưởng hình ảnh (Visual Metaphors) sinh động bằng ngôn ngữ của Manim.

## 📥 Required Knowledge (Tri thức cần có)
- BẮT BUỘC đọc: `2_knowledge/aesthetics_architecture.md` để nắm vùng an toàn.
- Kiểm tra kho đồ cụ: `4_execution/assets/` để xem có Icon sẵn không.

## ⚙️ Execution Approach (Quy trình thực thi)

### 1. Phân tích Ẩn dụ (Metaphor Brainstorming)
Với mỗi phân cảnh, Agent không được chỉ hiện chữ. Hãy suy nghĩ theo hướng:
- **Nếu là So sánh:** Dùng bập bênh (Seesaw) hoặc 2 cán cân.
- **Nếu là Tăng trưởng:** Dùng đồ thị đi lên hoặc thanh bar chart mọc cao.
- **Nếu là Quy trình:** Dùng các Node (vòng tròn) kết nối bởi Mũi tên (Arrow).
- **Nếu là Công thức:** Highlight (làm nổi bật) các biến số quan trọng bằng màu `ACCENT`.

### 2. Lập kế hoạch Bố cục (Spatial Planning)
Áp dụng "Cheat Sheet" tọa độ để phân bổ vật thể:
- **Title:** Mặc định ở `Y = 4.8`.
- **Nội dung trọng tâm:** Đặt tại `POS_CENTER` (Y = -0.5).
- **Chú thích bổ trợ:** Đặt tại `POS_BOTTOM_FOCUS` (Y = -3.0).

### 3. Thiết kế Chuyển động (Choreography)
Xác định cách vật thể xuất hiện khớp với nhịp nói:
- **Nhịp 1:** Hiện Tiêu đề.
- **Nhịp 2:** Hiện vật thể chính (Dùng `pop_in` hoặc `Write`).
- **Nhịp 3:** Biến đổi (Transform) hoặc Nhấn mạnh (Indicate) khi thoại nhắc đến từ khóa.

## 📤 Output Format (Biểu mẫu báo cáo)
Agent phải trình bày kế hoạch cho Scene hiện tại theo form sau:
1. **Ý tưởng ẩn dụ:** [Mô tả hình ảnh bạn định vẽ thay vì hiện chữ].
2. **Đối tượng sử dụng:** [Liệt kê Shapes, MathTex, Icons].
3. **Sơ đồ tọa độ:** [Vị trí Y của các khối nội dung].
4. **Kịch bản chuyển động:** [Sắp xếp thứ tự xuất hiện].

## ✅ Verification Protocol
Trước khi báo cáo, Agent PHẢI:
1. Mở tệp `verification_checklist.md` trong cùng thư mục này.
2. Đảm bảo mọi ý tưởng đều nằm trong "Vùng Vàng" (Y: -3.5 đến 4.0).
3. Xác nhận trong báo cáo: *"Thiết kế đã tuân thủ vùng an toàn và ẩn dụ hình học (YES)."*

## 📝 Changelog
- v1.0: Thiết lập tư duy Đạo diễn hình ảnh.