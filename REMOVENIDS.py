
print("\33[1;36mTHIS TOOL FORE REMVE NEW IDS 10009,10008,6155")
print("\33[1;35mBY : @J11IU ")


file_path = input("\33[1;32mPUT FILE : ")

with open(file_path, 'r') as file:
    lines = file.readlines()
#حذف ايديات الجديده
filtered_lines = [line for line in lines if not line.startswith(('10009', '10008', '6155'))]

with open(file_path, 'r') as file:
    lines = file.readlines()

# حذف الأسطر المكررة
lines = list(set(lines))

# ترتيب البيانات
lines.sort()

with open(file_path, 'w') as file:
    for line in lines:
        file.write
with open(file_path, 'w') as file:
    for line in filtered_lines:
        file.write(line)  
        
print("\33[1;32mDONE REMOVE AND SAVE")