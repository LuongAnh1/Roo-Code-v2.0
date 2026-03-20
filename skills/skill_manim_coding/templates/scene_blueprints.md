# SCENE BLUEPRINTS (KHUÔN MẪU CODE CHUẨN)

Agent BẮT BUỘC phải copy bộ khung (Blueprint) tương ứng dưới đây khi lập trình. Tuyệt đối không tự viết lại phần Import và Setup.

## 0. ĐOẠN MÃ KHỞI ĐẦU (HACK PATH)
*Dán đoạn này vào dòng 1 của mọi file Scene:*
```python
  import sys
  import os
  sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
  from execution.fami_lib import *
```

## 1. BLUEPRINT: SCENE 1 (HOOK)
*Nhịp độ nhanh, dứt khoát.*
```python
class Scene1_Hook(FaMIBaseScene):
    def construct(self):
        title = self.create_title("DÒNG TIÊU ĐỀ 1", "Dòng 2 (nếu có)")
        
        # [SÁNG TẠO: Khai báo các vật thể chính tại đây]
        # Ví dụ: icon = SVGMobject(...).move_to(POS_CENTER)

        with self.voiceover(text="[Thoại từ kịch bản]") as tracker:
            self.update_subtitle_dual("[Tiếng Việt]", "[Tiếng Anh]")
            # Quy tắc 80%: Tổng run_time = 0.8 * tracker.duration
            self.play(Write(title), run_time=tracker.duration * 0.3)
            self.play(FadeIn(icon, scale=0.5), run_time=tracker.duration * 0.5)
        
        self.finish_scene()
```

## 2. BLUEPRINT: SCENE 2 (MAIN BODY)
*Trình bày kiến thức, ưu tiên xếp DỌC.*
```python
class Scene2_MainBody(FaMIBaseScene):
    def construct(self):
        title = self.create_title("TỔNG KẾT KIẾN THỨC")
        
        # [SÁNG TẠO: Xếp các ý theo chiều dọc bằng VGroup]
        # pro_list = VGroup(item1, item2).arrange(DOWN, buff=0.5).move_to(POS_CENTER)

        with self.voiceover(text="[Thoại đoạn 1]") as tracker:
            self.update_subtitle_dual("[Vi]", "[En]")
            self.play(FadeIn(pro_list, shift=UP*0.5), run_time=tracker.duration * 0.8)

        self.finish_scene()
```

## 3. BLUEPRINT: SCENE 3 (TAKEAWAYS)
*Hiệu ứng thanh Search (Gõ chữ khóa trục Y).*
```python
class Scene3_Takeaways(FaMIBaseScene):
    def construct(self):
        title = self.create_title("TỪ KHÓA TÌM KIẾM")
        search_bar = RoundedRectangle(height=1.0, width=7.5).next_to(title, DOWN, buff=1.0)
        
        search_str = "[TỪ KHÓA]"
        last_char = search_bar # Vật thể mốc ban đầu
        current_buff = -3.5 # Tọa độ khởi đầu bên trong bar

        with self.voiceover(text="[Thoại]") as tracker:
            self.update_subtitle_dual("[Vi]", "[En]")
            self.play(Create(search_bar), run_time=tracker.duration * 0.2)
            
            for i, char in enumerate(search_str):
                if char == " ": current_buff += 0.2; continue # Xử lý khoảng trắng
                
                c = Text(char, font="Segoe UI", font_size=38)
                c.next_to(last_char, RIGHT, buff=current_buff).match_y(search_bar)
                self.play(FadeIn(c), run_time=0.08)
                last_char, current_buff = c, 0.05
```

## 4. BLUEPRINT: SCENE 4 (CTA)
*Câu hỏi mở + Mũi tên chỉ xuống nút Comment.*
```python
class Scene4_CTA(FaMIBaseScene):
    def construct(self):
        title = self.create_title("CÂU HỎI CHO BẠN")
        
        # [SÁNG TẠO: Vẽ hình ảnh minh họa cho câu hỏi mở ở POS_CENTER]

        # Vùng khóa cứng CTA ở dưới đáy (Y = -3.0)
        cta_box = RoundedRectangle(height=1.0, width=6.5, color=FAMI_CYAN)
        cta_text = Text("Comment câu trả lời!", font_size=30).move_to(cta_box)
        cta_group = VGroup(cta_box, cta_text).move_to(DOWN * 3.0)
        arrow = Arrow(cta_group.get_bottom(), cta_group.get_bottom() + DOWN * 1.0, color=SUCCESS)

        with self.voiceover(text="[Thoại]") as tracker:
            self.update_subtitle_dual("[Vi]", "[En]")
            self.play(FadeIn(cta_group, shift=UP*0.5), GrowArrow(arrow), run_time=tracker.duration * 0.8)

        self.finish_scene()
```