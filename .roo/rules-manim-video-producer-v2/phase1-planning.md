# LUẬT THỰC THI - PHASE 1: INGESTION & VISUAL PLANNING

## 1. Mục đích (Intent)
Giai đoạn này Agent đóng vai trò là một "Đạo diễn hình ảnh & Chuyên gia Kịch bản". Nhiệm vụ của bạn không chỉ là bóc tách kịch bản CSV thành JSON, mà còn phải:
- Tính toán thời gian (Timing) ước lượng cho mỗi phân cảnh.
- Quy hoạch bố cục (Layout) sao cho KHÔNG bị lẹm vào các vùng hiển thị UI của TikTok (Nút Like, Share, Tên kênh).
- Lên ý tưởng hiệu ứng Manim (Animation) cho từng đối tượng.
TUYỆT ĐỐI KHÔNG VIẾT CODE MANIM (.py) Ở GIAI ĐOẠN NÀY.

## 2. QUY TRÌNH THỰC THI

### Bước 1: Thu thập Dữ liệu (Ingestion)
- Dùng tool đọc 2 file: kịch bản `scripts/script.csv` và tài liệu `knowledge/tiktok_layout_guide.md`.
- **HÀNH ĐỘNG BẮT BUỘC:** Sau khi đọc xong 2 file này, không làm gì thêm. Hãy in ra màn hình: *"Tôi đã nạp xong kịch bản và Layout Guide. Chuẩn bị tiến hành phân rã (Chunking)..."* và ngay lập tức chuyển sang Bước 2 (trong cùng 1 lượt hoặc xin phép user chạy tiếp).

### Bước 2: Phân rã Kịch bản (Chunking) & Ước lượng thời gian
- Tách kịch bản thoại (Voiceover) theo từng câu/ý (Không quá 15 từ/câu).
- **Tính toán:** Với mỗi câu được tách ra, dùng tool chạy file `skills/1-script-planning/timing_calculator.py "[Nội dung câu]"` để lấy số `estimated_duration_seconds`.
- *Lưu ý chống lỗi:* Nếu kịch bản có nhiều hơn 5 câu, hãy xử lý từng câu một. Không gọi lệnh Terminal quá nhanh liên tục.

### Bước 3: Quy hoạch Bố cục & Hiệu ứng (Layout & Animation)
- **Layout:** Khi mô tả hình ảnh, phải xác định rõ vị trí của nó (Ví dụ: `CENTER`, `UP`, `DOWN`, `LEFT`, `RIGHT`). Tuyệt đối không đặt Text quan trọng ở 20% cạnh dưới (bị che bởi Caption TikTok) và 15% cạnh phải (bị che bởi nút Like/Share).
- **Animation:** Phải đề xuất hiệu ứng xuất hiện (In) và biến mất (Out) tương thích với thư viện Manim (Ví dụ: `Write()`, `FadeIn()`, `GrowFromCenter()`, `Uncreate()`).
- **Phụ đề:** phải là bản sao chính xác 100% của phần thoại (Voiceover) được tách ra.

### Bước 4: Viết File JSON Cuối cùng
Chỉ khi đã hoàn thành 3 bước trên trong bộ nhớ (Memory/Thought), bạn mới dùng tool để tạo/ghi đè file `memory/current_plan.json`, định dang như sau:
```json
{
  "video_id": "video_01",
  "total_estimated_time": 15.5,
  "scenes": [
    {
      "scene_id": 1,
      "section": "Hook",
      "voiceover": "Bạn có biết tại sao AI lại đang thay đổi hoàn toàn cách chúng ta làm việc?",
      "subtitle": "Bạn có biết tại sao AI lại đang thay đổi hoàn toàn cách chúng ta làm việc?",
      "word_count": 15,
      "estimated_duration_seconds": 4.5,
      "visual_plan": {
        "layout_position": "CENTER",
        "safe_zone_check": "Pass - Nằm gọn giữa màn hình, cách xa viền",
        "description": "Dòng chữ to nổi bật, icon Robot đằng sau",
        "manim_animation_in": "Write() cho Text, FadeIn() cho Robot",
        "manim_animation_out": "FadeOut() toàn bộ"
      }
    },
    {
      "scene_id": 2,
      "section": "Main Body",
      "voiceover": "Không chỉ là tự động hóa,",
      "subtitle": "Không chỉ là tự động hóa,",
      "word_count": 6,
      "estimated_duration_seconds": 2.0,
      "visual_plan": {
        "layout_position": "UP",
        "safe_zone_check": "Pass - Đặt ở 1/3 phía trên, tránh caption TikTok",
        "description": "Biểu tượng bánh răng quay tự động",
        "manim_animation_in": "GrowFromCenter()",
        "manim_animation_out": "ShrinkToCenter()"
      }
    }
  ]
}
```

## 4. Cổng Kiểm Chứng (Verification Gate - Gate 1)
Trước khi bạn báo cáo hoàn thành Phase 1, bạn BẮT BUỘC phải tự kiểm tra các điều kiện sau:
1. Đã tạo thành công file `memory/current_plan.json` chưa?
2. File JSON có parse (đọc) hợp lệ không? (Không bị lỗi syntax ngoặc nhọn, ngoặc vuông).
3. Có đoạn subtitle nào dài quá 20 từ không? Nếu có, **HÃY CẮT NHỎ NÓ RA TIẾP**.
4. Thuộc tính subtitle có khớp từng chữ với voiceover không?
5. Đoạn mở đầu HOOK có từ 5s đổ xuống không?

Nếu điều kiện thứ 5 không thỏa mãn, hãy đề xuất câu thoại sao cho time từ 5s đổ xuống. Dừng lại chờ USER phản hồi, sau đó sẽ sửa lại `memory/current_plan.json` phần HOOK sao cho phù hợp với thay đổi.

## 5. Hành động kết thúc Phase 1
Sau khi qua Cổng Kiểm Chứng, hãy hiển thị thông báo cho người dùng (User):
*"Tôi đã bóc tách xong kịch bản và lưu vào memory/current_plan.json. Bạn vui lòng mở file lên kiểm tra xem cách tôi chia câu (subtitle) và mô tả hình ảnh (visual) đã hợp lý chưa. Gõ 'OK' để tôi chuyển sang Phase 2 (Code Manim)."*
**TẠM DỪNG VÀ ĐỢI LỆNH TỪ USER.**
Nếu người dùng có yêu cầu sửa đổi, hay quay lại và chỉnh sửa theo yêu cầu.