import requests
from bs4 import BeautifulSoup
import pandas as pd

try:
    products = []
    for page in range(1, 4):
        print(f"🔍 Đang lấy dữ liệu từ trang {page}...")
        url = f"http://ocopviet.org.vn/san-pham.html?search=&order=1&showpage=24&per_page={page}"
        response = requests.get(url)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'html.parser')

        for item in soup.select('.product-small'):  # ví dụ selector, cần kiểm tra HTML thật
            name = item.select_one('.product-title > a').get_text(strip=True)
            print(name)
            province = item.select_one('.title_cut').get_text(strip=True)
            print (province)
            cost = item.select_one('.amount').get_text(strip=True)
            print(cost)
            products.append({
                "Tên sản phẩm": name,
                "Đơn vị": province,
                "Giá": cost
            })
            print(products[0])

    df = pd.DataFrame(products)
    df.to_csv("ocop_products.csv", index=False, encoding="utf-8-sig")

    print("✅ Đã lưu dữ liệu vào ocop_products.csv")
except Exception as e:
    print(f"❌ Đã xảy ra lỗi: {e}")

