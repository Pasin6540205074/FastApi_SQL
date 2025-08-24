import requests

BASE_URL = "http://127.0.0.1:8000"

def test_users():
    print("=== ทดสอบ  ===")

    user_data = {"name": "ริคาโด้", "email": "ricardo@example.com", "password": "123456"}
    resp = requests.post(f"{BASE_URL}/users/", json=user_data)
    user = resp.json()
    print("สร้างผู้ใช้งาน:", user)
    user_id = user["id"]

    print("ผู้ใช้งานทั้งหมด:", requests.get(f"{BASE_URL}/users/").json())
    print("ผู้ใช้งานรายเดียว:", requests.get(f"{BASE_URL}/users/{user_id}").json())

    updated_data = {"name": "ริคาโด้ ใหม่", "email": "ricado_new@example.com", "password": "newpass"}
    resp = requests.put(f"{BASE_URL}/users/{user_id}", json=updated_data)
    print("อัปเดตผู้ใช้งาน:", resp.json())

    print("ผลลัพธ์การลบผู้ใช้งาน:", requests.delete(f"{BASE_URL}/users/{user_id}").json())

def test_books():
    print("\n=== ทดสอบ หนังสือ ===")
    
    user_data = {"name": "คาปิบาร่า", "email": "capibara@example.com", "password": "abc123"}
    resp = requests.post(f"{BASE_URL}/users/", json=user_data)
    owner = resp.json()
    owner_id = owner["id"]

    book_data = {"title": "หนังสือเล่มแรก", "author": "คาปิบาร่า"}
    resp = requests.post(f"{BASE_URL}/books/?owner_id={owner_id}", json=book_data)
    book = resp.json()
    print("สร้างหนังสือ:", book)
    book_id = book["id"]

    print("หนังสือทั้งหมด:", requests.get(f"{BASE_URL}/books/").json())
    print("หนังสือรายเดียว:", requests.get(f"{BASE_URL}/books/{book_id}").json())

    updated_book = {"title": "หนังสือที่อัปเดตแล้ว", "author": "คาปิบาร่า ใหม่"}
    resp = requests.put(f"{BASE_URL}/books/{book_id}", json=updated_book)
    print("อัปเดตหนังสือ:", resp.json())

    print("ผลลัพธ์การลบหนังสือ:", requests.delete(f"{BASE_URL}/books/{book_id}").json())
    requests.delete(f"{BASE_URL}/users/{owner_id}")

if __name__ == "__main__":
    test_users()
    test_books()
