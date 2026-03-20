# SKILL: manim_pro_coding

## 🎯 Purpose (Mục đích)
Hiện thực hóa Storyboard thành code Python/Manim chuẩn 9:16, đảm bảo tính nhất quán thương hiệu FaMI.

## 🛠️ Execution Approach (Quy trình code)

### 1. Khởi tạo (Scaffolding)
- Luôn sử dụng đoạn "Hack Path" ở dòng 1 để nhận diện folder `skills/`:
```python
  import sys
  import os
  sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
  from execution.fami_lib import *
```

- **Kế thừa:** Mọi Class Scene BẮT BUỘC kế thừa FaMIBaseScene.

### 2. Sử dụng Skill Thư viện (Library Skills)
Agent BẮT BUỘC ưu tiên gọi các hàm sau từ fami_lib.py để đảm bảo đồng bộ thương hiệu:
- `self.create_title(line1, line2)`: Tự động đặt tiêu đề dưới Logo, bóp font nếu tràn, và đổ màu Gradient.
- `self.update_subtitle(text)`: Tự động dịch sang tiếng Anh và hiển thị phụ đề song ngữ ở tọa độ an toàn.
- `apply_fami_gradient(obj)`: Đổ màu Gradient theo dải chuẩn FaMI cho Text hoặc MathTex.
- `skill_pop_in(obj)` / `skill_slide_up(obj)`: Hiệu ứng chuyển động (Juicy Motion) chuẩn TikTok.
- `self.finish_scene()`: Kết thúc Scene bằng lệnh `wait(1)`.

### 3. QUY TẮC ĐÓNG GÓI NHÓM (THE GROUP-WRAP RULE)
Để chống tràn viền tuyệt đối, Agent KHÔNG ĐƯỢC để các đối tượng nằm rời rạc khi render. Hãy áp dụng "Combo 3 bước" cho mọi nhóm nội dung chính:

1. **Gom nhóm**: `my_group = VGroup(obj1, obj2, ...)`.
2. **Căn lề**: `my_group.arrange(DOWN, aligned_edge=LEFT, buff=0.3)`.
3. **Ép khung (BẮT BUỘC)**:
```python
  # Mọi nhóm nội dung chính phải chạy qua lớp lọc này trước khi play()
  if my_group.width > 7.5:
      my_group.scale_to_fit_width(7.5)
  # Sau đó mới đặt vị trí
  my_group.move_to(POS_CENTER)
```
- **Không nhớ tên hàm, lệnh:** Agent có thể tra cứu nhanh trong `knowledge/manim_api_cheat_sheet.md` để tìm cú pháp chính xác. Tuyệt đối không được đoán mò hoặc dùng hàm chưa kiểm chứng.
- **QUY TẮC:** Nếu một vật thể (VD: Text dài) không nằm trong VGroup, nó vẫn phải được kiểm tra `.width`. Chỉ khi gọi `.scale_to_fit_width(7.5)` thì mới đảm bảo video không bao giờ bị cắt mất chữ ở 2 bên mép màn hình.
- **Xếp chồng:** Ưu tiên arrange(DOWN) để tận dụng chiều cao màn hình dọc.

### 4. Đồng bộ hóa Voiceover (Timing)
- **Tỉ lệ 80%:** Tổng run_time của các lệnh self.play không được quá 80% (0.8) tracker.duration.
- **CẤM:** Không dùng `self.wait()` để căn khớp thời gian.
- **Dòng 1:** Lệnh đầu tiên trong khối with self.voiceover luôn là `self.update_subtitle(...)`.

### 5. Xử lý lỗi gõ chữ (Typing) - KHÓA TRỤC Y
Khi làm hiệu ứng hiện từng chữ, tuyệt đối không được để chữ bị nhảy nhấp nhô:

```python
  last_char = reference_obj 
  current_buff = 0.3 
  for i, char in enumerate(text_str):
      if char == " ": 
          current_buff = 0.2; continue
      new_char = Text(char, font="Segoe UI", font_size=40)
      new_char.next_to(last_char, RIGHT, buff=current_buff, aligned_edge=DOWN)
      new_char.match_y(search_bar) # BẮT BUỘC KHÓA TRỤC Y
      self.play(FadeIn(new_char), run_time=0.08)
      last_char, current_buff = new_char, 0.05
```

## ✅ Verification Protocol (Kiểm chứng)
Trước khi render, đối chiếu với `verification/layout_checklist.md`. Nếu kết quả là FAIL ở bất kỳ mục nào, Agent phải tự sửa code (Auto-Debug) cho đến khi đạt PASS.