import csv

def load_events(file_path):
    
    events = {}
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Bỏ qua dòng tiêu đề
        for row in reader:
            event_id, event_name = row
            events[event_id] = event_name
    return events

def load_players(file_path):
    
    players = {}
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Bỏ qua dòng tiêu đề
        for row in reader:
            player_id, name, position, country, age, overall = row
            players[player_id] = {
                'name': name,
                'position': position,
                'country': country,
                'age': int(age),
                'opverall': int(overall)
            }
    return players

def load_rules(file_path):
    
    rules = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Bỏ qua dòng tiêu đề
        for row in reader:
            events = row[:-1]  # Các sự kiện nằm ở các cột trước cột cuối cùng
            player_id = row[-1]  # Cầu thủ tương ứng
            rules.append((events, player_id))
    return rules

def save_rules(file_path, rules):
    
    with open(file_path, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["events", "player_id"])  # Ghi tiêu đề
        for rule in rules:
            writer.writerow(rule[0] + [rule[1]])  # Ghi mỗi rule

def save_events(file_path, events):
    
    try:
        with open(file_path, mode='w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['id', 'event_name'])  # Ghi header
            for event_id, event_name in events.items():
                writer.writerow([event_id, event_name])  # Ghi dữ liệu
    except Exception as e:
        print("Lỗi khi lưu file events.csv:", e)
