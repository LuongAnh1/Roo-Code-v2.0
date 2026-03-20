import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from execution.fami_lib import *

class CheckLayoutV2(FaMIBaseScene):
    def construct(self):
        # 1. TIÊU ĐỀ
        title = self.create_title("KIỂM TRA BỐ CỤC v2.2")

        # 2. VẼ CÁC ĐIỂM MỐC ĐỂ TEST (Debug Visualization)
        # Những điểm này giúp bạn nhìn thấy "Xương sống" của bố cục
        dot_top = Dot(POS_TOP_FOCUS, color=FAMI_CYAN)
        dot_center = Dot(POS_CENTER, color=WHITE)
        dot_bottom = Dot(POS_BOTTOM_FOCUS, color=ACCENT)
        
        # Vẽ nhãn cho các mốc
        label_top = Text("Top Focus", font_size=20).next_to(dot_top, RIGHT)
        label_center = Text("Center Focus", font_size=20).next_to(dot_center, RIGHT)
        label_bottom = Text("Bottom Focus", font_size=20).next_to(dot_bottom, RIGHT)

        # 3. ANIMATION
        with self.voiceover(text="Đầu tiên là kiểm tra phần đỉnh màn hình.") as tracker:
            self.update_subtitle("Đầu tiên là kiểm tra phần đỉnh màn hình.")
            self.play(Write(title), run_time=tracker.duration * 0.4)
            self.play(FadeIn(dot_top), Write(label_top), run_time=tracker.duration * 0.6)

        with self.voiceover(text="Tiếp theo là vùng trung tâm và vùng dưới.") as tracker:
            self.update_subtitle("Tiếp theo là vùng trung tâm và vùng dưới.")
            # Dùng Skill pop_in có sẵn
            anim_center, rate_center = skill_pop_in(VGroup(dot_center, label_center))
            self.play(anim_center, rate_func=rate_center, run_time=1.0)
            self.play(FadeIn(dot_bottom), Write(label_bottom), run_time=1.0)

        with self.voiceover(text="Cuối cùng là phụ đề song ngữ nằm ở vùng an toàn.") as tracker:
            self.update_subtitle("Phụ đề song ngữ nằm ở vùng an toàn đáy.")
            self.play(Indicate(self.subtitle_obj, color=ACCENT), run_time=2.0)

        self.finish_scene()