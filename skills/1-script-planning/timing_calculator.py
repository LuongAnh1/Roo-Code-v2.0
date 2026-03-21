import json
import sys

# Tốc độ đọc trung bình tiếng Việt (khoảng 3.5 từ/giây)
WORDS_PER_SECOND = 3.5  
PAUSE_BETWEEN_CHUNKS = 0.5 # Nghỉ nửa giây giữa các câu

def calculate_chunk_timing(text):
    """Tính toán số từ và số giây chính xác tuyệt đối"""
    words = text.split()
    word_count = len(words)
    
    if word_count == 0:
        return 0, 0.0

    # Công thức: (Số từ / Tốc độ) + Thời gian nghỉ
    estimated_seconds = round((word_count / WORDS_PER_SECOND) + PAUSE_BETWEEN_CHUNKS, 2)
    
    return word_count, estimated_seconds

if __name__ == "__main__":
    # Agent có thể gọi script này qua terminal với input là text
    if len(sys.argv) > 1:
        input_text = sys.argv[1]
        count, duration = calculate_chunk_timing(input_text)
        print(json.dumps({"word_count": count, "estimated_duration_seconds": duration}))
    else:
        print(json.dumps({"error": "No input text provided."}))