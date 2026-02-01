import psycopg2

def get_total_sales():
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="coffe_shop_sales_db",
        user="postgres",
        password="postgres"
    )

    with conn.cursor() as cur:
        cur.execute("""
            SELECT SUM(unit_price * transaction_qty)
            FROM sales
            WHERE EXTRACT(MONTH FROM transaction_date) = 3;
        """)
        result = cur.fetchone()[0]

    conn.close()
    return result


if __name__ == "__main__":
    print(get_total_sales())
