```text
├── .roo/                                # [HỆ THỐNG] Thư mục chứa các cấu hình, rules và template của Roo Code
│   ├── rules/                           # Quy tắc chung của dự án
│   │   └── general-coding.md            # Các tiêu chuẩn về coding (PEP 8, clean code, cấu trúc)
│   └── rules-manim-video-producer/      # Quy tắc dành riêng cho mode Manim Video Producer
│       ├── aesthetics-9-16.md           # Tiêu chuẩn thẩm mỹ, bố cục cho video dọc (Shorts/TikTok) tỷ lệ 9:16
│       ├── learning-examples.md         # Các ví dụ mẫu để tham khảo khi code Manim
│       ├── manim-standards.md           # Tiêu chuẩn code, animation và hiệu ứng của thư viện Manim
│       ├── scene-templates.md           # Các template mẫu cho từng loại Scene (Hook, Main, CTA...)
│       ├── step1-ingestion.md           # Hướng dẫn bước 1: Đọc và phân tích kịch bản
│       ├── step2-planning.md            # Hướng dẫn bước 2: Lên kế hoạch animation và layout
│       ├── step3-coding.md              # Hướng dẫn bước 3: Triển khai viết code Manim
│       ├── voiceover-rules.md           # Quy tắc xử lý âm thanh, lồng tiếng (Voiceover) và timing
│       └── work-flow.md                 # Quy trình làm việc tổng thể (Workflow) của agent
├── assets/                              # Thư mục chứa các tài nguyên tĩnh (hình ảnh, icon SVG, logo...)
├── knowledge/                           # Thư mục chứa tài liệu hướng dẫn chuyên sâu, nguyên lý hoặc code nháp
│   ├── test_logo.py                     # File nháp (test) dùng để thử nghiệm cách render logo vào Manim
│   └── tiktok_layout_guide.md           # Tài liệu hướng dẫn chi tiết về layout và vùng an toàn của video TikTok
├── media/                               # [MANIM] Nơi lưu trữ video, hình ảnh, audio do Manim tự động render ra
├── scripts/                             # Nơi chứa các file mã nguồn Python (.py) chính để chạy Manim
│   ├── scene_1_hook.py                  # Code Manim cho cảnh 1 (Hook - Thu hút sự chú ý đầu video)
│   ├── scene_2_main_body.py             # Code Manim cho cảnh 2 (Main Body - Nội dung chính)
│   ├── scene_3_takeaways.py             # Code Manim cho cảnh 3 (Takeaways - Bài học/Tóm tắt)
│   └── scene_4_cta.py                   # Code Manim cho cảnh 4 (Call to Action - Kêu gọi hành động)
├── skills/                              # Chứa các thư viện, hàm/lớp tiện ích dùng chung (helper functions)
│   └── fami_lib.py                      # Thư viện tiện ích tùy chỉnh (chứa các hàm tạo layout, màu sắc, icon...)
└── README.md                            # Tài liệu mô tả chung về dự án

Cấu trúc mới đề xuất
├── .roo/
│   ├── rules/
│   │   └── working-principles.md        # LUẬT THÉP: Bắt buộc tuân thủ 3 Giai đoạn, phải có file Plan, phải tự chạy thử manim.
│   └── rules-manim-video-producer/      # (Giữ nguyên như của bạn, nhưng phân rã manim-standards ra)
│       ├── phase1-planning.md           # Hướng dẫn tạo current_plan.md
│       ├── phase2-coding.md             # Hướng dẫn gọi các Skill để code
│       └── phase3-qa-render.md          # Hướng dẫn đọc log lỗi Manim
│
├── memory/                              # [MỚI] Bộ nhớ dự án
│   ├── current_plan.md                  # File kịch bản đã phân rã (AI viết ra ở Phase 1)
│   ├── active-tasks.json                # Trạng thái tiến độ
│   └── lessons-learned/                 # Những lỗi Manim AI từng mắc phải
│
├── skills/                              # [ĐÃ NÂNG CẤP] Biến thành các Folder trọn gói
│   ├── __init__.py                      
│   ├── text_generation_skill/           # Skill xử lý chữ
│   │   ├── SKILL.md                     # Hướng dẫn dùng skill này
│   │   └── text_helpers.py              # Code Python chứa các hàm text
│   ├── layout_calculation_skill/        # Skill chia lưới 9:16
│   └── audio_sync_skill/                # Skill khớp giọng nói
│
├── media/
├── scripts/
└── README.md


```