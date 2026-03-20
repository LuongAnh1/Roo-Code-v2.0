# 📂 CẤU TRÚC THƯ MỤC: FAMI MANIM OS v2.0

```text
/FaMI_Manim_Project
├── .roo/
│   └── rules-manim-video-producer-v2-0/      # [HỆ ĐIỀU HÀNH] Nạp tự động vào Roo Code
│       ├── master_runbook.md            # Quy trình điều phối các Pha (Phases)
│       └── global_constraints.md        # Các lệnh "CẤM" và Tiêu chuẩn chung
│
├── intent/                            # [LỚP MỤC TIÊU]
│   └── brand_identity.md                # Tầm nhìn kênh FaMI, Brand Voice, Persona
│
├── knowledge/                         # [LỚP TRI THỨC]
│   ├── manim_api_cheat_sheet.md         # Tra cứu nhanh hàm Manim & LaTeX
│   └── aesthetics_architecture.md       # Bản đồ vùng an toàn 9:16 (Layout Theory)
│
├── skills/                            # [LỚP KỸ NĂNG] Đóng gói thành từng Folder
│   ├── skill_parse_script/              # Kỹ năng bóc tách kịch bản CSV
│   │   ├── SKILL.md                     # Logic xử lý (Dòng lẻ: Thoại, Dòng chẵn: Hình)
│   │   └── verification_checklist.md    # Kiểm tra map đúng 4 cảnh chưa?
│   ├── skill_storyboard_design/         # Kỹ năng sáng tạo ẩn dụ hình ảnh
│   │   ├── SKILL.md                     # Cách tư duy Visual Metaphors
│   │   └── templates/                   # Các mẫu mô tả Storyboard chuẩn
│   ├── skill_manim_coding/              # Kỹ năng viết mã nguồn (Trọng tâm)
│   │   ├── SKILL.md                     # Quy tắc: Khóa trục Y, 80% duration, Subtitle
│   │   ├── templates/                   # 4 Blueprints cho 4 Scene
│   │   └── verification/                # Checklist chống tràn viền, chống lệch chữ
│   └── skill_auto_debug/                # Kỹ năng tự sửa lỗi Terminal
│       ├── SKILL.md                     # Cách đọc Traceback và sửa code
│       └── reference_errors.md          # Thư viện các lỗi đã từng gặp
│
├── execution/                         # [LỚP THỰC THI] "Tay chân" của Agent
│   ├── fami_lib.py                      # Thư viện core (Logo, Title, Gradient, Subtitle)
│   └── assets/                          # Chứa Logo.png và các file .svg icon
│
├── evolution/                         # [LỚP TIẾN HÓA] Học hỏi sau mỗi Video
│   ├── lessons_learned.md               # Ghi chép các "Gotchas" (Cú lừa) mới
│   └── changelog_os.md                  # Lịch sử cập nhật hệ thống Skill
│
├── outputs/                             # Nơi lưu file .py và .mp4 cuối cùng
└── scripts/                             # Nơi chứa file input (script.csv)
```

# 🔎 CHI TIẾT CÁC FILE QUAN TRỌNG THEO TƯ DUY SKILL-BASED

## 1. File Điều Phối: .roo/rules-manim-video-producer/master_runbook.md
- File này chỉ dạy Agent "Khi nào thì rút Skill nào ra xài".

## 2. Cấu trúc một Folder Skill (Ví dụ: skill_manim_coding)
- **SKILL.md**: Chứa "Algorithm" để Agent viết code (Quy tắc 80% thời gian, Quy tắc update_subtitle_dual).
- **templates/**: Chứa đoạn mã mẫu (Snippet) để Agent copy-paste nhanh các khối with self.voiceover.
- **verification/layout_checklist.md**: Ép Agent phải tự kiểm tra: "Mình đã dùng scale_to_fit_width(7.5) chưa? Chữ có đè logo không?" trước khi nó nộp bài cho bạn.

