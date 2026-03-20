# KIẾN TRÚC THẨM MỸ VIDEO DỌC (FA MI VERSION)

Đây là bản đồ không gian 9:16. Mọi thiết kế ở Pha 2 và Code ở Pha 3 BẮT BUỘC phải dựa trên tọa độ này.

## 1. HỆ TỌA ĐỘ VÀ CÁC VÙNG CẤM (DEAD ZONES)
Màn hình Manim dọc có: `frame_height = 16.0`, `frame_width = 9.0`.
- **Trục Y:** Từ `+8.0` (Đỉnh) đến `-8.0` (Đáy).
- **Trục X:** Từ `-4.5` (Trái) đến `+4.5` (Phải).

### ⛔ VÙNG CẤM (TUYỆT ĐỐI KHÔNG ĐẶT NỘI DUNG)
1. **Header Zone (Y > +5.5):** Vùng của Logo FaMI. Không vẽ hình chồng lên đây.
2. **Footer Zone (Y < -4.2):** Vùng của Subtitle và Giao diện TikTok (Like/Comment). Cấm đặt text nội dung bài học ở đây.
3. **Right Sidebar (X > +3.8):** Vùng chứa nút Like/Share của TikTok. Tránh đặt thông tin quan trọng sát lề phải.

---

## 2. PHÂN VÙNG VÀNG (GOLDEN STAGE)
Mọi ma thuật và ẩn dụ hình ảnh PHẢI diễn ra gọn gàng trong:
- **Tọa độ Y:** Từ `-3.5` đến `+4.0`.

## 3. CHEAT SHEET TỌA ĐỘ (AGENT TRA CỨU NHANH)
| Thành phần | Tọa độ Y chuẩn | Ghi chú |
| :--- | :--- | :--- |
| **Tiêu đề (Title)** | `+4.8` | Dùng `self.create_title()` |
| **Vùng nội dung trên**| `+2.0` | Dùng `POS_TOP_FOCUS` |
| **Trung tâm hình ảnh**| `-0.5` | Dùng `POS_CENTER` |
| **Vùng nội dung dưới**| `-3.0` | Dùng `POS_BOTTOM_FOCUS` |
| **Phụ đề (Subtitle)** | `-3.8` | Dùng `self.update_subtitle()` |

---

## 4. NGUYÊN TẮC BỐ CỤC "CHỐNG TRÀN"
Dù thiết kế bất kỳ đồ thị hay nhóm đối tượng nào, Agent phải tuân thủ:
- **Ngắt dòng chủ động:** Nếu câu văn dài hơn 15 từ, bắt buộc dùng `Paragraph()` để chia dòng, tuyệt đối không dùng `Text()`.
- **Giới hạn 7.5:** Mọi cụm vật thể ngang PHẢI được ép kích thước:
  `if obj.width > 7.5: obj.scale_to_fit_width(7.5)`