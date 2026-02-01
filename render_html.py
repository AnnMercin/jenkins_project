from fetch_sales import get_total_sales

result = get_total_sales()

html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Total Sales</title>
</head>
<body>
    <h1>Total Sales for March</h1>
    <p><strong>{result}</strong></p>
</body>
</html>
"""

with open("index.html","w") as f:
    f.write(html)

print("index.html generated successfully")
