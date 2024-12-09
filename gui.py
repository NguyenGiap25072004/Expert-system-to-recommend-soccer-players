# gui.py
import csv
import tkinter as tk
from tkinter import messagebox, simpledialog
from events import load_events, load_players, load_rules, save_rules, save_events
from PIL import Image, ImageTk  # Yêu cầu cài đặt thư viện pillow (pip install pillow)

# Đọc dữ liệu từ các file CSV
events = load_events('events.csv')
players = load_players('players.csv')
rules = load_rules('rules.csv')

def create_gui():
    """Tạo giao diện người dùng cải tiến với Tkinter."""
    root = tk.Tk()
    root.title("Hệ Chuyên Gia - Tư vấn Cầu Thủ")
    root.geometry("1000x600")
    root.configure(bg="#f0f0f0")
    
    # Tạo khung cho hình ảnh
    frame_image = tk.Frame(root, bg="#ffffff", bd=2, relief=tk.GROOVE)
    frame_image.grid(row=0, column=3, rowspan=2, sticky="nsew", padx=10, pady=10)

    # Đặt label cho phần hình ảnh
    tk.Label(frame_image, text="Hướng dẫn sử dụng hệ chuyên gia", font=("Arial", 14), bg="#ffffff", fg="#000000").pack(pady=5)

    try:
        # Đọc và thay đổi kích thước hình ảnh
        image_path = "image.png"  # Đường dẫn đến tệp ảnh (cùng thư mục)
        image = Image.open(image_path)

        # Điều chỉnh kích thước ảnh cho phù hợp
        frame_width = 200  # Kích thước khung rộng hơn để vừa với hình
        frame_height = 200  # Chiều cao khung
        image = image.resize((frame_width, frame_height))  # Thay đổi kích thước ảnh

        # Chuyển đổi ảnh thành định dạng phù hợp để hiển thị trong Tkinter
        photo = ImageTk.PhotoImage(image)

        # Thêm ảnh vào label trong khung
        image_label = tk.Label(frame_image, image=photo, bg="#ffffff")
        image_label.image = photo  # Giữ tham chiếu đến hình ảnh
        image_label.pack(pady=10)

    # Thêm văn bản vào bên dưới ảnh
        text_label = tk.Label(frame_image, text="Đây là hướng dẫn sử dụng hệ chuyên gia gợi ý cầu thủ. Các bạn vui lòng đọc kỹ hướng dẫn sử dụng trước khi dùng", 
                            font=("Arial", 12), bg="#ffffff", fg="#000000", wraplength=180, justify="center")
        text_label.pack(side="top", pady=10)  # Đặt văn bản bên dưới ảnh

    except Exception as e:
        # Thông báo nếu không thể tải ảnh
        tk.Label(frame_image, text="Không thể tải ảnh.", font=("Arial", 12), fg="red", bg="#ffffff").pack(pady=5)
        print("Error loading image:", e)
    
    def clear_selection(event_listbox):
        """Bỏ chọn tất cả các mục trong danh sách."""
        event_listbox.selection_clear(0, tk.END)


    # Khung sự kiện
    frame_events = tk.Frame(root, bg="#f8f8ff", bd=2, relief=tk.GROOVE)
    frame_events.grid(row=0, column=0, rowspan=2, sticky="ns", padx=10, pady=10)
    # Danh sách sự kiện với thanh tìm kiếm
    search_event_entry = tk.Entry(frame_events, width=30)
    search_event_entry.pack(pady=5)
    tk.Label(frame_events, text="CÁC ĐẶC ĐIỂM CẦU THỦ", font=("Arial", 14), bg="#f8f8ff", fg="#000080").pack(pady=5)

    event_listbox = tk.Listbox(frame_events, selectmode=tk.MULTIPLE, width=30, height=25, font=("Arial", 12))
    for event_name in events.values():
        event_listbox.insert(tk.END, event_name)
    event_listbox.pack(pady=5)
# Nút "Thêm vào đã chọn" và "Xóa chọn tất cả" trên cùng dòng
    frame_buttons_top = tk.Frame(frame_events, bg="#f8f8ff")
    frame_buttons_top.pack(pady=5)
    btn_add_to_selected = tk.Button(
        frame_buttons_top, 
        text="Thêm vào đã chọn", 
        font=("Arial", 12), 
        bg="#00a2ed", 
        fg="white", 
        command=lambda: add_selected_events(event_listbox, selected_event_listbox)
    )
    btn_add_to_selected.pack(side="left", padx=5)

    btn_clear_selection = tk.Button(
        frame_buttons_top, 
        text="Xóa chọn tất cả", 
        font=("Arial", 12), 
        bg="yellow", 
        command=lambda: clear_selection(event_listbox)
    )
    btn_clear_selection.pack(side="left", padx=5)
    # Thêm nút "Thêm", "Chỉnh sửa", "Xóa"
    btn_add = tk.Button(frame_events, text="Thêm", command=lambda: add_event(event_listbox), bg="lightblue", width=15)
    btn_add.pack(side="left", padx=10, pady=5)

    btn_edit = tk.Button(frame_events, text="Chỉnh sửa", command=lambda: edit_event(event_listbox), bg="lightgreen", width=15)
    btn_edit.pack(side="left", padx=10, pady=5)

    btn_delete = tk.Button(frame_events, text="Xóa", command=lambda: delete_event(event_listbox), bg="lightcoral", width=15)
    btn_delete.pack(side="left", padx=10, pady=5)
    
    def search_events():
        query = search_event_entry.get().lower()
        event_listbox.delete(0, tk.END)
        for event_name in events.values():
            if query in event_name.lower():
                event_listbox.insert(tk.END, event_name)

    search_event_entry.bind("<KeyRelease>", lambda e: search_events())
    
    # Khung sự kiện đã chọn
    frame_selected = tk.Frame(root, bg="#fffaf0", bd=2, relief=tk.GROOVE)
    frame_selected.grid(row=0, column=1, rowspan=2, sticky="ns", padx=10, pady=10)
    tk.Label(frame_selected, text="ĐẶC ĐIỂM CẦU THỦ ĐÃ CHỌN", font=("Arial", 14), bg="#fffaf0", fg="#8b0000").pack(pady=5)

    selected_event_listbox = tk.Listbox(frame_selected, selectmode=tk.SINGLE, width=30, height=25, font=("Arial", 12))
    selected_event_listbox.pack(pady=5)

    tk.Button(frame_selected, text="Xóa", font=("Arial", 12), bg="#ff4500", fg="white",
              command=lambda: delete_selected_event(selected_event_listbox)).pack(pady=5)
    tk.Button(frame_selected, text="Xóa Tất Cả", font=("Arial", 12), bg="#ff6347", fg="white",
              command=lambda: selected_event_listbox.delete(0, tk.END)).pack(pady=5)

    # Khung gợi ý cầu thủ
    frame_result = tk.Frame(root, bg="#e6ffe6", bd=2, relief=tk.GROOVE)
    frame_result.grid(row=0, column=2, sticky="nsew", padx=10, pady=10)
    tk.Label(frame_result, text="KẾT QUẢ GỢI Ý CẦU THỦ", font=("Arial", 14), bg="#e6ffe6", fg="#006400").pack(pady=5)

    result_text = tk.Text(frame_result, width=50, height=15, font=("Arial", 12), bg="#f0fff0")
    result_text.pack(pady=5)
    tk.Button(frame_result, text="Gợi ý cầu thủ", font=("Arial", 12), bg="#32cd32", fg="white",
              command=lambda: diagnose(selected_event_listbox, result_text)).pack(pady=5)

    # Khung quản lý quy tắc
    frame_rules = tk.Frame(root, bg="#ffffe0", bd=2, relief=tk.GROOVE)
    frame_rules.grid(row=1, column=2, sticky="nsew", padx=10, pady=10)
    tk.Label(frame_rules, text="QUẢN LÝ LUẬT SUY DIỄN", font=("Arial", 14), bg="#ffffe0", fg="#b8860b").pack(pady=5)

    rules_listbox = tk.Listbox(frame_rules, width=50, height=10, font=("Arial", 12), bg="#fffff0")
    for rule in rules:
        rule_text = f"{', '.join(rule[0])} -> {rule[1]}"
        rules_listbox.insert(tk.END, rule_text)
    rules_listbox.pack(pady=5)

    tk.Button(frame_rules, text="Thêm luật", font=("Arial", 12), bg="#4682b4", fg="white",
              command=lambda: add_rule(rules_listbox)).pack(pady=5)
    tk.Button(frame_rules, text="Xóa luật", font=("Arial", 12), bg="#dc143c", fg="white",
              command=lambda: remove_rule(rules_listbox)).pack(pady=5)
    tk.Button(frame_rules, text="Chỉnh sửa luật", font=("Arial", 12), bg="#dc157c", fg="white",
              command=lambda: edit_rule(rules_listbox)).pack(pady=5)

    root.mainloop()

# Các hàm xử lý
def add_selected_events(event_listbox, selected_event_listbox):
    selected_indices = event_listbox.curselection()
    for index in selected_indices:
        event = event_listbox.get(index)
        if event not in selected_event_listbox.get(0, tk.END):
            selected_event_listbox.insert(tk.END, event)

def delete_selected_event(selected_event_listbox):
    selected_index = selected_event_listbox.curselection()
    if selected_index:
        selected_event_listbox.delete(selected_index)

def add_rule(rules_listbox):
    new_rule = simpledialog.askstring("Thêm luật", "Nhập rule (dạng: event1,event2,... -> player_id)")
    if new_rule:
        try:
            events_part, player_id = new_rule.split("->")
            events_list = [e.strip() for e in events_part.split(",")]
            rules.append((events_list, player_id.strip()))
            rules_listbox.insert(tk.END, f"{', '.join(events_list)} -> {player_id.strip()}")
            save_rules('rules.csv', rules)
        except ValueError:
            messagebox.showerror("Lỗi", "Định dạng không hợp lệ!")

def remove_rule(rules_listbox):
    selected = rules_listbox.curselection()
    if selected:
        rule_text = rules_listbox.get(selected[0])
        rule_parts = rule_text.split(" -> ")
        events_list = rule_parts[0].split(", ")
        player_id = rule_parts[1]
        rules.remove((events_list, player_id))
        rules_listbox.delete(selected[0])
        save_rules('rules.csv', rules)

def diagnose(selected_event_listbox, result_text):
    selected_events = [selected_event_listbox.get(index) for index in range(selected_event_listbox.size())]
    # Lấy danh sách khóa (id) của các đặc điểm đã chọn
    selected_event_keys = [key for key, value in events.items() if value in selected_events]

    matched_players = []  # Danh sách cầu thủ phù hợp
    matched_rules = []    # Danh sách các luật suy diễn đã dùng

    for rule_events, player_id in rules:
        if set(rule_events).issubset(selected_event_keys):  # Kiểm tra nếu luật được áp dụng
            matched_players.append(players[player_id])  # Thêm cầu thủ vào danh sách phù hợp
            matched_rules.append((rule_events, player_id))  # Lưu luật tương ứng

    # Xóa nội dung cũ trong hộp kết quả
    result_text.delete(1.0, tk.END)

    if matched_players:
        for idx, player in enumerate(matched_players, start=1):  # Đánh số thứ tự từ 1
            result_text.insert(tk.END, f"{idx}. Cầu thủ: {player['name']}\n")
            result_text.insert(tk.END, f"   Vị trí: {player['position']}\n")
            result_text.insert(tk.END, f"   Quốc gia: {player['country']}\n")
            result_text.insert(tk.END, f"   Tuổi: {player['age']}\n")
            result_text.insert(tk.END, f"   Overall: {player['overall']}\n")
            result_text.insert(tk.END, "-" * 90 + "\n")
            # Hiển thị đặc điểm cầu thủ
            used_events = [events[event_id] for event_id in matched_rules[idx - 1][0]]
            result_text.insert(tk.END, f"   Đặc điểm đã sử dụng: {', '.join(used_events)}\n")
            # Hiển thị luật suy diễn
            result_text.insert(tk.END, f"   Luật suy diễn: {', '.join(matched_rules[idx - 1][0])} -> {matched_rules[idx - 1][1]}\n")
            result_text.insert(tk.END, "=" * 50 + "\n")
    else:
        result_text.insert(tk.END, "Không tìm thấy cầu thủ phù hợp!\n")


def edit_rule(rules_listbox):
    """Sửa một rule được chọn."""
    selected = rules_listbox.curselection()
    if selected:
        rule_text = rules_listbox.get(selected[0])
        new_rule = simpledialog.askstring("Sửa Rule", f"Sửa Rule (hiện tại: {rule_text})\nDạng: event1,event2,... -> player_id")
        if new_rule:
            try:
                events_part, player_id = new_rule.split("->")
                events_list = [e.strip() for e in events_part.split(",")]
                # Cập nhật danh sách rules
                rule_parts = rule_text.split(" -> ")
                old_events_list = rule_parts[0].split(", ")
                old_player_id = rule_parts[1]
                rules.remove((old_events_list, old_player_id))
                rules.append((events_list, player_id.strip()))
                # Cập nhật giao diện
                rules_listbox.delete(selected[0])
                rules_listbox.insert(tk.END, f"{', '.join(events_list)} -> {player_id.strip()}")
                save_rules('rules.csv', rules)
            except ValueError:
                messagebox.showerror("Lỗi", "Định dạng không hợp lệ!")
# Hàm thêm sự kiện mới
def add_event(event_listbox):
    new_event = simpledialog.askstring("Thêm đặc điểm", "Nhập tên đặc điểm mới (định dạng: a(i): ....):")
    if new_event:
        event_key = f"a{len(events) + 1}"  # Tạo key mới cho sự kiện
        events[event_key] = new_event  # Thêm sự kiện vào từ điển
        event_listbox.insert(tk.END, new_event)  # Thêm sự kiện vào giao diện
        save_events('events.csv', events)  # Lưu sự kiện vào tệp CSV

# Hàm chỉnh sửa sự kiện đã chọn
def edit_event(event_listbox):
    try:
        selected_index = event_listbox.curselection()[0]  # Lấy chỉ số sự kiện được chọn
        current_event = event_listbox.get(selected_index)  # Lấy tên sự kiện hiện tại
        event_key = next(key for key, value in events.items() if value == current_event)  # Tìm key của sự kiện
        new_event = simpledialog.askstring("Chỉnh sửa đặc điểm", f"Sửa đặc điểm: {current_event}")
        if new_event:
            event_listbox.delete(selected_index)  # Xóa sự kiện cũ
            event_listbox.insert(selected_index, new_event)  # Thêm sự kiện mới
            events[event_key] = new_event  # Cập nhật từ điển
            save_events('events.csv', events)  # Lưu sự kiện vào tệp CSV
    except IndexError:
        messagebox.showwarning("Chỉnh sửa", "Chọn một đặc điểm để chỉnh sửa!")
    except StopIteration:
        messagebox.showerror("Lỗi", "Không tìm thấy sự kiện!")

# Hàm xóa sự kiện đã chọn
def delete_event(event_listbox):
    try:
        selected_index = event_listbox.curselection()[0]  # Lấy chỉ số sự kiện được chọn
        current_event = event_listbox.get(selected_index)  # Lấy tên sự kiện
        event_key = next(key for key, value in events.items() if value == current_event)  # Tìm key của sự kiện
        event_listbox.delete(selected_index)  # Xóa sự kiện khỏi giao diện
        del events[event_key]  # Xóa sự kiện khỏi từ điển
        save_events('events.csv', events)  # Lưu thay đổi vào tệp CSV
    except IndexError:
        messagebox.showwarning("Xóa", "Chọn một đặc điểm để xóa!")
    except StopIteration:
        messagebox.showerror("Lỗi", "Không tìm thấy đặc điểm!")
