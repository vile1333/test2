import sqlite3


conn = sqlite3.connect('store_database.db')
cursor = conn.cursor()


def display_stores():
    cursor.execute("SELECT store_id, title FROM store")
    stores = cursor.fetchall()
    for store in stores:
        print(f"{store[0]}. {store[1]}")
    return [store[0] for store in stores]


def display_products(store_id):
    cursor.execute("""
        SELECT p.title, c.title, p.unit_price, p.stock_quantity
        FROM products p
        JOIN categories c ON p.category_code = c.code
        WHERE p.store_id = ?
    """, (store_id,))
    products = cursor.fetchall()
    if products:
        for product in products:
            print(f"\nНазвание продукта: {product[0]}")
            print(f"Категория: {product[1]}")
            print(f"Цена: {product[2]}")
            print(f"Количество на складе: {product[3]}")
    else:
        print("В этом магазине нет продуктов.")


def main():
    print(
        "Вы можете отобразить список продуктов по выбранному id магазина из перечня магазинов ниже, для выхода из программы введите цифру 0:")

    while True:
        store_ids = display_stores()
        try:
            user_input = int(input("\nВведите ID магазина или 0 для выхода: "))
            if user_input == 0:
                print("Выход из программы.")
                break
            elif user_input in store_ids:
                display_products(user_input)
            else:
                print("Неправильный ID магазина, попробуйте снова.")
        except ValueError:
            print("Пожалуйста, введите корректное число.")

    conn.close()


if __name__ == "__main__":
    main()
