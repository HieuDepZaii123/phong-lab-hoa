# Phòng Lab — Hóa học THPT

Phòng thí nghiệm hóa học trên trình duyệt cho học sinh trung học phổ thông. Học sinh pha hóa chất, làm bài thí nghiệm theo hướng dẫn, chuẩn độ, tra bảng tuần hoàn, đọc sổ tay và làm trắc nghiệm.

## Các trạm

- **Bàn thí nghiệm** — pha hóa chất và xem phản ứng
- **Bảng tuần hoàn** — 118 nguyên tố
- **Bài thí nghiệm** — 18 bài có hướng dẫn (theo SGK, gồm các bài Hóa 12)
- **Chuẩn độ** — axit–bazơ, đường pH
- **Sổ tay** — lý thuyết và câu hỏi
- **47 câu trắc nghiệm**

## Cách mở

Toàn bộ ứng dụng nằm trong một file tĩnh: `index.html`. Mở file đó trực tiếp trong trình duyệt (kéo thả hoặc nháy đúp). Không cần cài đặt, không cần máy chủ.

## Sửa nội dung

Đây là bản build đã minify, không có mã nguồn tách riêng. Muốn đổi nội dung thì vá chuỗi trong file HTML. Script `tools/patch.py` thêm 6 thí nghiệm Hóa 12 từ bản gốc (`archive/phong-lab-v1.html`). Script `tools/patch2.py` vá tiếp trên `index.html`: nút đun theo từng bước, hình điện phân, bài nước cứng và bài PE/PVC. Chạy lại script trên file đã vá sẽ không khớp.
