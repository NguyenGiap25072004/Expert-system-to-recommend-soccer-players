# Expert-system-to-recommend-soccer-players
Midterm project assignment for introductory artificial intelligence course

1. Giới thiệu

Mục tiêu của hệ thống: Xây dựng một hệ thống chuyên gia có khả năng gợi ý cầu thủ bóng đá dựa trên các đặc điểm mà người dùng mong muốn.

Lợi ích của hệ thống:

Hỗ trợ người dùng tìm kiếm cầu thủ phù hợp với yêu cầu một cách nhanh chóng và hiệu quả.

Cung cấp thông tin chi tiết về cầu thủ, bao gồm các thuộc tính, kỹ năng và chỉ số.

Giúp người dùng ra quyết định trong việc lựa chọn cầu thủ, ví dụ như trong game quản lý bóng đá hoặc tuyển chọn cầu thủ thực tế.

Phương pháp tiếp cận: Sử dụng phương pháp suy diễn tiến, dựa trên luật (rule-based reasoning) để gợi ý cầu thủ.
2. Kiến trúc hệ thống

Hệ thống bao gồm 3 thành phần chính:

Cơ sở tri thức:
Tập hợp các sự kiện (đặc điểm cầu thủ) được lưu trữ trong file events.csv.

Tập hợp các cầu thủ và thông tin chi tiết của họ được lưu trữ trong file players.csv.

Tập hợp các luật suy diễn, mỗi luật liên kết một tập hợp các sự kiện với một cầu thủ cụ thể, được lưu trữ trong file rules.csv.

Công cụ suy diễn:

Sử dụng phương pháp suy diễn tiến để tìm ra các cầu thủ phù hợp với các sự kiện (đặc điểm) mà người dùng đã chọn.

Duyệt qua các luật, kiểm tra xem tập các sự kiện đầu vào có khớp với tập sự kiện trong luật hay không. Nếu khớp, cầu thủ tương ứng trong luật sẽ được đưa vào danh sách kết quả.

Giao diện người dùng:

Được xây dựng bằng thư viện Tkinter, cung cấp cho người dùng các chức năng:

Chọn các đặc điểm cầu thủ mong muốn.

Xem danh sách cầu thủ được gợi ý.

Thêm, xóa, sửa luật suy diễn.

Thêm, xóa, sửa các sự kiện (đặc điểm cầu thủ).

3. Mô tả chi tiết các thành phần
   
Đánh giá cầu thủ qua các:

Đặc điểm chung:
a1: Thuận hai chân 
a2: Kỹ thuật tốt 
a3: Thể lực cao 
a4: Tốc độ nhanh 
a5: Khả năng chuyền bóng tốt 
a6: Kỹ năng dứt điểm chính xác 
a7: Chiều cao vượt trội 
a8: Còn trẻ khỏe 
a9: Khả năng phòng thủ xuất sắc 
a10: Kỹ năng chuyền bóng dài 
a11: Khả năng đoán tình huống tốt 
a12: Khả năng chơi bóng đầu tốt 
a13: Khả năng kiểm soát bóng tốt 
a14: Khả năng lãnh đạo tốt 
a15: Khả năng phản ứng nhanh 
a16: Tầm nhìn tốt
Thủ môn (Goalkeeper)
a17: Khả năng phản xạ xuất sắc
a18: Khả năng chỉ huy hàng phòng ngự
a19: Kỹ năng bắt bóng bổng
a20: Khả năng phát bóng chính xác
a21: Kỹ năng xử lý bóng bằng chân
Hậu vệ (Defender)
a22: Khả năng kèm người chặt chẽ
a23: Khả năng tắc bóng hiệu quả
a24: Kỹ năng không chiến tốt
a25: Khả năng hỗ trợ tấn công
a26: Tính kỷ luật trong phòng thủ
Tiền vệ (Midfielder)
a27: Khả năng kiểm soát nhịp độ trận đấu
a28: Khả năng chuyền ngắn chính xác
a29: Khả năng rê bóng thoát pressing
a30: Khả năng chuyền dài tốt
a31: Khả năng ghi bàn từ xa
Tiền đạo (Forward)
a32: Bản năng săn bàn tốt
a33: Khả năng di chuyển không bóng thông minh
a34: Khả năng tạo khoảng trống
a35: Kỹ năng dứt điểm đa dạng
a36: Khả năng chọn vị trí tốt


4. Luật suy diễn

Mỗi luật suy diễn có dạng: event1, event2, ... -> player_id

Ví dụ: a1, a2, a3 -> b1 nghĩa là nếu cầu thủ có các đặc điểm a1, a2, a3 thì hệ thống sẽ gợi ý cầu thủ b1.

5. Ví dụ minh họa

Giả sử người dùng chọn các đặc điểm: "Thuận hai chân", "Kỹ thuật tốt", "Thể lực cao". Hệ thống sẽ tìm kiếm các luật có chứa các sự kiện tương ứng (ví dụ: a1, a2, a3) và đưa ra gợi ý cầu thủ phù hợp (ví dụ: b1).
