# MASTER RUNBOOK: MANIM PRODUCTION

Thực hiện dự án theo vòng lặp 4 Pha (Phases). Tại mỗi pha, hãy gọi (Invoke) folder Skill tương ứng.

## PHA 1: NẠP DỮ LIỆU (INGESTION)
- **Skill:** `3_skills/skill_parse_script`
- **Mục tiêu:** Trích xuất Thoại & Hình từ CSV.
- 🔴 **STOP:** Chờ người dùng duyệt bản bóc tách.

## PHA 2: PHÁC THẢO (ART DIRECTION)
- **Skill:** `3_skills/skill_storyboard_design`
- **Tài liệu tham khảo:** `2_knowledge/aesthetics_architecture.md`
- 🔴 **STOP:** Chờ người dùng duyệt ý tưởng ẩn dụ hình ảnh.

## PHA 3: LẬP TRÌNH & KIỂM CHỨNG (EXECUTION & VERIFY)
- **Skill:** `3_skills/skill_manim_coding`
- **Công cụ thực thi:** `4_execution/fami_lib.py`
- **Quy trình:** Viết code -> Chạy `verification/checklist.md` -> Render nháp.

## PHA 4: TỰ SỬA LỖI & TIẾN HÓA (EVOLVE)
- **Skill:** `3_skills/skill_auto_debug`
- **Hành động:** Nếu lỗi, sửa code. Nếu sửa thành công lỗi mới, cập nhật `5_evolution/lessons_learned.md`.