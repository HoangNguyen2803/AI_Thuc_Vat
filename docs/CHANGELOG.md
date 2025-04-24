# CHANGELOG

Tài liệu này ghi lại các thay đổi đáng chú ý trong quá trình phát triển dự án.

---

## Phiên bản 0.1 (Phát hành: 2025-04-14)

### Tính năng:
- Phát triển các chức năng cơ bản cho hệ thống.
- Thiết lập cấu trúc thư mục và môi trường ban đầu.

### Đánh giá:
- Là bản phát hành đầu tiên, đặt nền tảng cho việc phát triển AI trong các phiên bản tiếp theo.

---

## Phiên bản 0.2 (Phát hành: 2025-04-15)

### Cải tiến mô hình:
- Thay đổi kiến trúc mạng nơ-ron trong `neural_network_model.py` nhằm tăng độ chính xác trong phân loại hoa Iris.
- Thêm các lớp `BatchNormalization` và `Dropout` để cải thiện độ ổn định mô hình và giảm hiện tượng overfitting.

### Cập nhật đánh giá mô hình:
- Nâng cấp hàm `evaluate_iris_model` trong `model_evaluation.py`:
  - Thêm các chỉ số đánh giá: `precision`, `recall`, `F1-score`.
  - Tích hợp báo cáo phân loại chi tiết (classification report).

### Dọn dẹp mã nguồn:
- Đã **xóa** file `neural_network_model.py` (không còn sử dụng do kiến trúc mới đã được tích hợp).

---

## Phiên bản 0.3 (Phát hành: 2025-04-24)

### Tính năng mới:
- Giao diện người dùng (UI):
+ Thiết kế giao diện mandala với các phần tử tương tác cho từng loại hoa (Cỏ, Cây, Lá, Hoa).
+ Thêm tiêu đề chào mừng ở phía trên giao diện.
+ Cải thiện trải nghiệm người dùng với hiệu ứng hover cho các phần tử.

### Cải tiến:
+ Cấu trúc CSS:
- Sử dụng biến CSS để quản lý màu sắc dễ dàng hơn.
- Điều chỉnh vị trí của bông hoa trong mandala để phù hợp với thiết kế mới.
- Bo tròn các cánh hoa để tạo cảm giác mềm mại hơn.
+ Âm thanh:
+ *Tích hợp âm thanh:*
- Thêm âm thanh hover và nhạc nền cho trải nghiệm người dùng phong phú hơn.

### Tối ưu hóa:
+ Tối ưu hóa mã JavaScript:
- Cải tiến mã JavaScript để xử lý các sự kiện hover và click hiệu quả hơn.
- Tích hợp chức năng lấy tiến độ cho việc tô cánh hoa trong mandala.

### Phát hiện lỗi:
- Âm thanh không phát khi hover hoặc click.
- Giao diện chưa hoàn chỉnh, cần điều chỉnh thêm.
- Một số liên kết bị hỏng, không trỏ đến trang tương ứng.
### Tiến trình:
- Đang tiếp tục cải tiến và khắc phục các vấn đề đã phát hiện.