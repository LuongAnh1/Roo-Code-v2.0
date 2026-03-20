# SKILL: storyboard_art_direction

## 🎯 Purpose (Mục đích)
Chuyển hóa dữ liệu kịch bản (Text) thành Ý tưởng hình học (Visual Metaphors) và Cấu trúc bố cục (Layout Structure) cho 4 phân cảnh.

## ⚙️ Execution Approach (Quy trình Sáng tạo)

### 1. Phân tích Nội dung (Content Parsing)
- Đọc kỹ phân cảnh hiện tại.
- Xác định "Điểm nhấn kiến thức" (Key Knowledge): Cái gì quan trọng nhất cần người xem nhớ?
- **Ẩn dụ hình học (Visual Metaphor):**
    - Nếu có sự so sánh: Gọi skill `arrange_comparison()`.
    - Nếu là quy trình/thứ tự: Dùng `VGroup(...).arrange(DOWN)`.
    - Nếu là công thức: Dùng `MathTex` kết hợp `skill_apply_gradient()`.

### 2. Thiết lập Tọa độ (Spatial Strategy)
Không dùng tọa độ cứng. Phải sử dụng "Hệ trục FaMI":
- **Header**: `POS_TITLE` (Y=4.8).
- **Stage**: Tập trung nội dung chính tại `POS_CENTER` (Y=0.5).
- **Context**: Nếu có thêm thông tin phụ, đặt tại `POS_BOTTOM_FOCUS` (Y=-2.5).
- **Subtitle**: Mặc định `POS_SUBTITLE` (Y=-3.8).

### 3. Choreography (Nhịp điệu)
- Thiết kế luồng xuất hiện của đối tượng theo nhịp thoại:
    - **Ý chính 1**: Hiện Tiêu đề.
    - **Ý chính 2**: Hiện đối tượng minh họa (Dùng `skill_pop_in`).
    - **Ý chính 3**: Nhấn mạnh (Indicate) hoặc Biến đổi (ReplacementTransform).

## 📥 Required Resources (Tài nguyên cần kiểm tra)
- Kiểm tra file `execution/assets/` xem có biểu tượng (SVG) phù hợp với kịch bản không.
- Nếu không có biểu tượng phù hợp, hãy tự tạo hình khối cơ bản (Circle, Rectangle, Polygon) trong Manim.

## ✅ Verification Protocol (Trước khi báo cáo)
Agent phải tự kiểm tra với file `verification_checklist.md` trong cùng thư mục.
- Nếu ý tưởng vi phạm vùng an toàn (Dead Zones) hoặc quá khô khan (toàn chữ), BẮT BUỘC sửa lại ngay trước khi gửi báo cáo cho người dùng.

## 📝 Reporting Format
Trình bày Storyboard theo form:
1. **Visual Metaphor:** [Mô tả hình ảnh bạn định vẽ].
2. **Object Plan:** [Liệt kê các đối tượng sẽ dùng].
3. **Motion Flow:** [Thứ tự xuất hiện theo nhịp thoại].