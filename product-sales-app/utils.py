def read_file(filename):
    """อ่านไฟล์ทีละบรรทัด (ตัดช่องว่าง/ขึ้นบรรทัดใหม่ และข้ามบรรทัดว่าง) ถ้าไม่มีไฟล์คืน []"""
    try:
        with open(filename, "r") as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        return []
