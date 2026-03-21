import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from skills.fami_lib import *
import numpy as np

class Video01(FaMIBaseScene):
    def construct(self):
        title = self.create_title("PHÂN LOẠI EMAIL SPAM", "ĐỊNH LÝ BAYES")

        # --- SCENE 1: Hook ---
        q_text = MarkupText("Làm sao để phân loại\nEmail Spam?", font="Segoe UI", font_size=40)
        apply_fami_gradient(q_text, [RED, YELLOW])
        
        with self.voiceover(text="Làm sao để phân loại Email Spam?") as tracker:
            self.update_subtitle("Làm sao để phân loại Email Spam?")
            self.play(Write(title), run_time=min(1.0, tracker.duration * 0.4))
            self.play(Write(q_text), run_time=min(1.0, tracker.duration * 0.4))
            
        self.play(FadeOut(q_text))

        # --- SCENE 2-4: Main Body (Bayes) ---
        text2 = Text("Qua câu chuyện này, ta thấy rằng", font="Segoe UI", font_size=32).move_to(UP * 2.5)
        apply_fami_gradient(text2)
        
        with self.voiceover(text="Qua câu chuyện này, ta thấy rằng") as tracker:
            self.update_subtitle("Qua câu chuyện này, ta thấy rằng")
            self.play(FadeIn(text2), run_time=min(1.0, tracker.duration * 0.8))

        bayes_form = MathTex(r"P(A|B) = \frac{P(B|A)P(A)}{P(B)}").scale_to_fit_width(6.0)
        apply_fami_gradient(bayes_form)
        
        with self.voiceover(text="Định lý Bayes không chỉ là công thức") as tracker:
            self.update_subtitle("Định lý Bayes không chỉ là công thức")
            self.play(Write(bayes_form), run_time=min(1.5, tracker.duration * 0.8))

        icon_life = Star(color=YELLOW).scale(0.5).next_to(bayes_form, DOWN, buff=0.5)
        
        with self.voiceover(text="mà còn được ứng dụng trực tiếp trong đời sống.") as tracker:
            self.update_subtitle("mà còn được ứng dụng trực tiếp trong đời sống.")
            self.play(GrowFromCenter(icon_life), run_time=min(1.5, tracker.duration * 0.8))

        self.play(FadeOut(VGroup(text2, bayes_form, icon_life)))

        # --- SCENE 5-8: Ưu điểm ---
        text_adv = Text("Ưu điểm:", font="Segoe UI", font_size=36, color=GREEN).move_to(UP * 2.5)
        
        with self.voiceover(text="Về ưu điểm, đây không phải thuật toán tĩnh,") as tracker:
            self.update_subtitle("Về ưu điểm, đây không phải thuật toán tĩnh,")
            self.play(Write(text_adv), run_time=min(1.0, tracker.duration * 0.8))

        robot = Text("BOT", font="Segoe UI", font_size=60).move_to(UP * 1.0)
        with self.voiceover(text="nó có khả năng học từ dữ liệu mới,") as tracker:
            self.update_subtitle("nó có khả năng học từ dữ liệu mới,")
            self.play(FadeIn(robot), run_time=min(1.0, tracker.duration * 0.8))

        chart = BarChart(values=[10, 5, 2], bar_names=["L1", "L2", "L3"]).scale(0.5).next_to(robot, DOWN, buff=0.5)
        with self.voiceover(text="giảm thiểu đánh nhầm email quan trọng thành Spam") as tracker:
            self.update_subtitle("giảm thiểu đánh nhầm email quan trọng thành Spam")
            self.play(Create(chart), run_time=min(1.5, tracker.duration * 0.8))

        clock = Text("TIME", font="Segoe UI", font_size=50).next_to(chart, RIGHT, buff=0.5)
        with self.voiceover(text="cùng tốc độ tính toán nhanh.") as tracker:
            self.update_subtitle("cùng tốc độ tính toán nhanh.")
            self.play(GrowFromCenter(clock), run_time=min(1.0, tracker.duration * 0.8))

        self.play(FadeOut(VGroup(text_adv, robot, chart, clock)))

        # --- SCENE 9-12: Hạn chế ---
        text_dis = Text("Hạn chế: Spam tinh vi", font="Segoe UI", font_size=36, color=RED).move_to(UP * 2.5)
        with self.voiceover(text="Về hạn chế thì Spam ngày nay ngày càng tinh vi.") as tracker:
            self.update_subtitle("Về hạn chế thì Spam ngày nay ngày càng tinh vi.")
            self.play(Write(text_dis), run_time=min(1.0, tracker.duration * 0.8))

        word_free = Text("free", font="Segoe UI", font_size=40).move_to(UP * 1.0)
        word_fr33 = Text("fr33", font="Segoe UI", font_size=40, color=ORANGE).move_to(UP * 1.0)
        
        with self.voiceover(text="Thay vì viết free, kẻ gửi có thể viết fr33;") as tracker:
            self.update_subtitle("Thay vì viết free, kẻ gửi có thể viết fr33;")
            self.play(Write(word_free), run_time=min(0.5, tracker.duration * 0.4))
            self.play(Transform(word_free, word_fr33), run_time=min(1.0, tracker.duration * 0.4))

        word_vars = Text("f.r.e.e  |  fr€€", font="Segoe UI", font_size=36, color=YELLOW).next_to(word_fr33, DOWN, buff=0.5)
        with self.voiceover(text="f.r.e.e; fr€€ làm hệ thống dựa trên từ khóa") as tracker:
            self.update_subtitle("f.r.e.e; fr€€ làm hệ thống dựa trên từ khóa")
            self.play(FadeIn(word_vars), run_time=min(1.0, tracker.duration * 0.8))

        cross = Cross().move_to(word_vars)
        with self.voiceover(text="khó nhận diện.") as tracker:
            self.update_subtitle("khó nhận diện.")
            self.play(Create(cross), run_time=min(1.0, tracker.duration * 0.8))

        self.play(FadeOut(VGroup(text_dis, word_free, word_vars, cross)))

        # --- SCENE 13-17: Từ khóa Google ---
        an_text = Text("Phương pháp của An", font="Segoe UI", font_size=30).move_to(UP * 2.5)
        with self.voiceover(text="Từ phương pháp của An, nếu muốn hiểu sâu hơn") as tracker:
            self.update_subtitle("Từ phương pháp của An, nếu muốn hiểu sâu hơn")
            self.play(FadeIn(an_text), run_time=min(1.0, tracker.duration * 0.8))

        flow = Arrow(LEFT, RIGHT).next_to(an_text, DOWN, buff=1.0)
        with self.voiceover(text="về cách các hệ thống lọc Spam hoạt động trong thực tế,") as tracker:
            self.update_subtitle("về cách các hệ thống lọc Spam hoạt động trong thực tế,")
            self.play(GrowArrow(flow), run_time=min(1.0, tracker.duration * 0.8))

        search_bar = Rectangle(width=6.0, height=0.8).next_to(flow, DOWN, buff=1.0)
        with self.voiceover(text="bạn có thể tìm kiếm cụm từ khóa") as tracker:
            self.update_subtitle("bạn có thể tìm kiếm cụm từ khóa")
            self.play(Create(search_bar), run_time=min(1.0, tracker.duration * 0.8))

        keyword = Text("Naive Bayes Classifier", font="Segoe UI", font_size=30).move_to(search_bar)
        apply_fami_gradient(keyword)
        with self.voiceover(text="Naive Bayes Classifier") as tracker:
            self.update_subtitle("Naive Bayes Classifier")
            self.play(Write(keyword), run_time=min(1.0, tracker.duration * 0.8))

        g_logo = Text("Google System", font="Segoe UI", font_size=24, color=BLUE).next_to(search_bar, DOWN, buff=0.5)
        with self.voiceover(text="là hệ thống lọc Spam lớn của Google") as tracker:
            self.update_subtitle("là hệ thống lọc Spam lớn của Google")
            self.play(FadeIn(g_logo), run_time=min(1.0, tracker.duration * 0.8))

        self.play(FadeOut(VGroup(an_text, flow, search_bar, keyword, g_logo)))

        # --- SCENE 18-21: CTA ---
        q_cta = Text("?", font="Segoe UI", font_size=80, color=RED).move_to(UP * 2.0)
        with self.voiceover(text="Câu hỏi cuối video dành cho bạn đó là") as tracker:
            self.update_subtitle("Câu hỏi cuối video dành cho bạn đó là")
            self.play(GrowFromCenter(q_cta), run_time=min(1.0, tracker.duration * 0.8))

        spammer = Text("SPAMMER", font="Segoe UI", font_size=40).move_to(ORIGIN)
        with self.voiceover(text="phải xử lý như nào nếu kẻ Spam cố tình") as tracker:
            self.update_subtitle("phải xử lý như nào nếu kẻ Spam cố tình")
            self.play(FadeIn(spammer), run_time=min(1.0, tracker.duration * 0.8))

        f_txt = Text("free -> fr€€", font="Segoe UI", font_size=40).next_to(spammer, DOWN, buff=0.5)
        apply_fami_gradient(f_txt, [YELLOW, RED])
        with self.voiceover(text="viết free thành fr€€?") as tracker:
            self.update_subtitle("viết free thành fr€€?")
            self.play(Write(f_txt), run_time=min(1.0, tracker.duration * 0.8))

        # Khóa cứng CTA
        cta_box = RoundedRectangle(height=1.0, width=6.5, color=FAMI_CYAN)
        cta_text = Text("Comment câu trả lời của bạn!", font="Segoe UI", font_size=30).move_to(cta_box)
        cta_group = VGroup(cta_box, cta_text).move_to(DOWN * 3.0)
        arrow = Arrow(cta_group.get_top() + UP*1.0, cta_group.get_top(), color=SUCCESS)

        with self.voiceover(text="Nếu bạn biết câu trả lời, hãy comment phía dưới.") as tracker:
            self.update_subtitle("Nếu bạn biết câu trả lời, hãy comment phía dưới.")
            self.play(FadeIn(cta_group, shift=UP*0.5), GrowArrow(arrow), run_time=min(1.5, tracker.duration * 0.8))

        self.finish_scene()
