import csv

def load_events(file_path):
    """Đọc sự kiện từ file CSV."""
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
            player_id,name,position,team,age,overall, potential ,height,weight,foot,bestoverall,growth,value,wage,releaseclause,totalattacking,crossing,finishing,headingaccuracy,shortpassing,volleys,totalskill,dribbling,curve,fkaccuracy,longpassing,ballcontrol,totalmovement,acceleration,sprintspeed, agility,shotpower,jumping,stamina,strength,longshots,totaldefending,defensiveawareness,standingtackle,slidingtackle,totalgoalkeeping,gkdiving,gkhandling,gkkicking,gkpositioning,gkreflexes,internationalreputation,contract,onloan, predicted_value_linear_regression, predicted_value_lightgbm, actual_value  = row
            players[player_id] = {
                'name': name,
                'position': position,
                'team': team,
                'age': int(age),
                'overall': int(overall),
                'potential': int(potential),
                'height': int(height),
                'weight': int(weight),
                'foot': foot,
                'bestoverall': int(bestoverall),
                'growth': int(growth),
                'value': int(value),
                'wage': int(wage),
                'releaseclause': int(releaseclause),
                'totalattacking': int(totalattacking),
                'crossing': int(crossing),
                'finishing': int(finishing),
                'headingaccuracy': int(headingaccuracy),
                'shortpassing': int(shortpassing),
                'dribbling': int(dribbling),
                'curve': int(curve),
                'fkaccuracy': int(fkaccuracy),
                'longpassing': int(longpassing),
                'ballcontrol': int(ballcontrol),
                'totalmovement': int(totalmovement),
                'acceleration': int(acceleration),
                'sprintspeed': int(sprintspeed),
                'agility': int(agility),
                'shotpower': int(shotpower),
                'jumping': int(jumping),
                'stamina': int(stamina),
                'strength': int(strength),
                'longshots': int(longshots),
                'totaldefending': int(totaldefending),
                'defensiveawareness': int(defensiveawareness),
                'standingtackle': int(standingtackle),
                'slidingtackle': int(slidingtackle),
                'totalgoalkeeping': int(totalgoalkeeping),
                'gkdiving': int(gkdiving),
                'gkhandling': int(gkhandling),
                'gkkicking': int(gkkicking),
                'gkpositioning': int(gkpositioning),
                'gkreflexes': int(gkreflexes),
                'internationalreputation': int(internationalreputation),
                'contract': contract,
                'onloan': onloan,
                'predicted_value_linear_regression': float(predicted_value_linear_regression),
                'predicted_value_lightgbm': float(predicted_value_lightgbm),
                'actual_value': float(actual_value)
            }
    return players

def load_rules(file_path):
    """Đọc các quy tắc từ file CSV."""
    rules = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Bỏ qua dòng tiêu đề
        for row in reader:
            try:
                events = row[:-1]  # Các sự kiện nằm ở các cột trước cột cuối cùng
                player_id = row[-1]  # Cầu thủ tương ứng
                rules.append((events, player_id))
            except IndexError:
                print(f"Lỗi: Dòng thiếu dữ liệu: {row}")  # In ra dòng lỗi để dễ dàng kiểm tra
    return rules

def save_rules(file_path, rules):
    """Lưu các quy tắc mới vào file CSV."""
    with open(file_path, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["events", "player_id"])  # Ghi tiêu đề
        for rule in rules:
            writer.writerow(rule[0] + [rule[1]])  # Ghi mỗi rule
# events.py
def save_events(file_path, events):
    """Lưu danh sách sự kiện vào file CSV."""
    try:
        with open(file_path, mode='w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['id', 'event_name'])  # Ghi header
            for event_id, event_name in events.items():
                writer.writerow([event_id, event_name])  # Ghi dữ liệu
    except Exception as e:
        print("Lỗi khi lưu file events.csv:", e)
