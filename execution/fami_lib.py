from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
from deep_translator import GoogleTranslator
import os

# Khởi tạo Translator (Dùng engine của Google)
translator = GoogleTranslator(source='vi', target='en')

# ==========================================================
# 1. HỆ TỌA ĐỘ KHÓA CỨNG (Đã tối ưu cho không gian rộng)
# ==========================================================
# Đẩy Logo và Title lên cao sát mép, tạo không gian lớn cho Main Stage
POS_TITLE = UP * 5.2          # Tiêu đề cao hơn (Sát logo)
POS_TOP_FOCUS = UP * 3.5      # Vùng trên nới rộng
POS_CENTER = UP * 0.5           # Tâm chính giữa màn hình (để có nhiều đất diễn)
POS_BOTTOM_FOCUS = DOWN * 2.5 # Vùng dưới
POS_SUBTITLE = DOWN * 4.2     # Phụ đề giữ an toàn

# Hằng số so sánh Trái-Phải (Căn theo trục X của màn hình 9:16)
# Frame width là 9, chia đôi là 4.5. 
# Vị trí X = 2.2 là khoảng cách an toàn, tránh sát mép màn hình
POS_LEFT = LEFT * 2.2 + POS_CENTER
POS_RIGHT = RIGHT * 2.2 + POS_CENTER

# ==========================================
# 2. BẢNG MÀU THƯƠNG HIỆU
# ==========================================
config.pixel_height, config.pixel_width = 1920, 1080
config.frame_height, config.frame_width = 16.0, 9.0

FAMI_BLUE = "#005BAA"
FAMI_CYAN = "#45C4D9"
FAMI_SUB = "#DFE858"
ACCENT = "#fffa65"
DANGER = "#ff4d4d"
SUCCESS = "#00e676"
TEXT_COLOR = WHITE

# --- SKILL: ĐỔ MÀU GRADIENT ---
def apply_fami_gradient(mobject, colors=None):
    if colors is None:
        colors = [FAMI_CYAN, FAMI_BLUE]
    for submob in mobject.family_members_with_points():
        if len(submob.points) > 0:
            submob.set_color(colors)
    return mobject

# ==========================================
# 3. CLASS CƠ SỞ (BASE SCENE)
# ==========================================
class FaMIBaseScene(VoiceoverScene):
    def setup(self):
        super().setup()
        self.set_speech_service(GTTSService(lang="vi"))
        
        # 1. Khởi tạo Phụ đề (Luôn chạy dù logo có lỗi hay không)
        self.subtitle_obj = Text("", font="Segoe UI", font_size=35, color=WHITE, weight=BOLD)
        self.subtitle_obj.move_to(POS_SUBTITLE)
        self.add_foreground_mobject(self.subtitle_obj)
        
        # 2. Logo FaMI
        logo_path = os.path.join(os.path.dirname(__file__), "assets", "fami_logo.png")
        if os.path.exists(logo_path):
            self.logo = ImageMobject(logo_path).scale_to_fit_width(1.2).to_edge(UP, buff=0.4)
        else:
            # Ghi log lỗi để bạn biết nhưng không làm crash toàn bộ setup
            print(f"CẢNH BÁO: Không tìm thấy logo tại {logo_path}")
            self.logo = Text("FaMI 1956", font_size=25, color=FAMI_BLUE, weight=BOLD).to_edge(UP, buff=0.4)
        
        self.add_foreground_mobject(self.logo)

    # --- SKILLS ---
    def update_subtitle(self, vi_text, max_width=7.5):
        """Skill: Tự động dịch sang tiếng Anh bằng Deep Translator"""
        try:
            # Lệnh dịch mới, rất nhanh và ít lỗi
            en_text = translator.translate(vi_text)
        except Exception as e:
            print(f"Lỗi dịch thuật: {e}")
            en_text = "" # Nếu rớt mạng thì để trống
        
        # 1. Tiếng Việt
        vi_sub = Paragraph(vi_text, font="Segoe UI", font_size=35, color=WHITE, weight=BOLD, alignment="center")
        
        # 2. Tiếng Anh
        en_sub = Paragraph(en_text, font="Segoe UI", font_size=28, color=FAMI_SUB, slant=ITALIC, alignment="center")
        
        sub_group = VGroup(vi_sub, en_sub).arrange(DOWN, buff=0.1)
        if sub_group.width > max_width:
            sub_group.scale_to_fit_width(max_width)
            
        sub_group.move_to(POS_SUBTITLE)
        self.subtitle_obj.become(sub_group)
    
    def create_title(self, line1, line2="", apply_gradient=True):
        """Skill: Tạo tiêu đề chuẩn FaMI - Vị trí an toàn dưới Logo nhỏ"""
        if line2:
            title = Paragraph(line1, line2, font="Segoe UI", font_size=40, weight=BOLD, alignment="center")
        else:
            title = Text(line1, font="Segoe UI", font_size=40, weight=BOLD)
        
        # Sử dụng next_to để logo và tiêu đề tự giãn cách
        title.next_to(self.logo, DOWN, buff=0.4) 
        
        if title.width > 7.5:
            title.scale_to_fit_width(7.5)
            
        if apply_gradient:
            apply_fami_gradient(title)
        return title
    
    def finish_scene(self):
        self.wait(1)

# ==========================================
# 4. KỸ NĂNG DI CHUYỂN (MOTION SKILLS)
# ==========================================
def skill_pop_in(obj):
    """Hiệu ứng xuất hiện nảy (Juicy) chuẩn TikTok"""
    return FadeIn(obj, scale=0.5, shift=UP*0.2), rate_functions.ease_out_back

def skill_slide_up(obj):
    """Hiệu ứng trượt từ dưới lên chuyên nghiệp"""
    return FadeIn(obj, shift=UP*1.5), rate_functions.smooth

def arrange_comparison(self, obj_left, obj_right, buff=1.0):
        """
        Skill: Khóa cứng bố cục So sánh (Trái - Phải) tại vùng trung tâm.
        Sử dụng POS_LEFT và POS_RIGHT đã định nghĩa ở đầu file.
        """
        obj_left.move_to(POS_LEFT)
        obj_right.move_to(POS_RIGHT)
        return VGroup(obj_left, obj_right)