# SKILL: parse_fami_script

## 🎯 Purpose (Mục đích)
Trích xuất và ánh xạ (map) dữ liệu từ file kịch bản (`.csv` hoặc `.md`) vào cấu trúc dữ liệu chuẩn của dự án video FaMI.

## 📥 Required Inputs (Đầu vào)
- Tệp kịch bản: `scripts/script.csv` (ưu tiên) hoặc nội dung Markdown Table.

## 📤 Expected Output (Đầu ra)
Một bản tóm tắt phân tích gồm 4 Scene:
1. **Scene 1 (Hook)**: {Voiceover, Visual Description, Duration Check}
2. **Scene 2 (Main Body)**: {Voiceover, Visual Description}
3. **Scene 3 (Takeaways)**: {Voiceover, Visual Description}
4. **Scene 4 (CTA)**: {Voiceover, Visual Description}

## ⚙️ Execution Approach (Quy trình thực thi)

### 1. Phân tách cấu trúc 2 hàng (Pair-Row Parsing)
Agent phải đọc file theo quy tắc "Cụm 2 hàng":
- **Dòng 1 (Header)**: Tuyệt đối **KHÔNG** lấy nội dung ở dòng này làm kịch bản. Nó chỉ là tên cột.
- **Cụm kịch bản 1 (Dòng 2 & 3)**: 
  - Dòng 2: Là **Voiceover** (Lời thoại) cho cả 4 phân cảnh.
  - Dòng 3: Là **Visuals** (Mô tả hình ảnh) cho cả 4 phân cảnh tương ứng.
- **Ánh xạ cột**:
  - Cột 1 -> Scene1_Hook
  - Cột 2 -> Scene2_MainBody
  - Cột 3 -> Scene3_Takeaways
  - Cột 4 -> Scene4_CTA

### 2. Kiểm định khả thi (Feasibility Check)
Với mỗi phân cảnh, Agent phải tự đánh giá:
- **Duration Check (Ước tính thời gian):** Sử dụng hệ số: 1 giây = 2.5 từ.
- **Tính khả thi của Manim**: Nếu "Mô tả hình ảnh" yêu cầu "người đi bộ", "phong cảnh thật"... hãy ghi chú lại để đề xuất chuyển sang "Biểu tượng/Hình học" ở Pha 2.


## 🔍 Verification & Reporting (BẮT BUỘC)
Sau khi trích xuất dữ liệu, Agent phải thực hiện quy trình kiểm soát chất lượng sau:

1. **Đối chiếu:** Mở tệp `verification_checklist.md` và tự chấm điểm YES/NO cho kết quả vừa làm.
2. **Báo cáo:** Khi trình bày danh sách 4 phân cảnh cho người dùng, bạn **PHẢI** kèm theo dòng xác nhận: 
   > *"Tôi đã đối chiếu với `verification_checklist.md` và xác nhận kịch bản đạt tiêu chuẩn (YES cho mọi mục)."*
3. **Xử lý lỗi:** Nếu có mục đạt NO, hãy tự sửa hoặc dừng lại hỏi ý kiến tùy theo chỉ dẫn trong checklist.

## 📝 Changelog
- v1.0: Khởi tạo quy tắc đọc cụm 2 hàng.