from flask import Flask, render_template_string

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Simple E-Commerce Website</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f4f4f4;
            margin: 0;
            padding: 0;
        }
        header {
            background: #333;
            color: #fff;
            padding: 1em 0;
            text-align: center;
        }
        .container {
            max-width: 900px;
            margin: 2em auto;
            background: #fff;
            padding: 2em;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }
        .products {
            display: flex;
            flex-wrap: wrap;
            gap: 2em;
            justify-content: center;
        }
        .product {
            background: #fafafa;
            border: 1px solid #eee;
            border-radius: 6px;
            padding: 1em;
            width: 220px;
            text-align: center;
            box-shadow: 0 1px 4px rgba(0,0,0,0.05);
        }
        .product img {
            width: 120px;
            height: 120px;
            object-fit: cover;
            margin-bottom: 1em;
        }
        .product h3 {
            margin: 0.5em 0;
        }
        .product p {
            color: #555;
            font-size: 0.95em;
        }
        .product .price {
            color: #27ae60;
            font-weight: bold;
            margin: 0.5em 0;
        }
        .product button {
            background: #27ae60;
            color: #fff;
            border: none;
            padding: 0.5em 1.2em;
            border-radius: 4px;
            cursor: pointer;
            transition: background 0.2s;
        }
        .product button:hover {
            background: #219150;
        }
        footer {
            text-align: center;
            padding: 1em 0;
            background: #333;
            color: #fff;
            margin-top: 2em;
        }
    </style>
</head>
<body>
    <header>
        <h1>My E-Commerce Store</h1>
        <p>Shop the best products!</p>
    </header>
    <div class="container">
        <div class="products">
            <div class="product">
                <img src="https://via.placeholder.com/120?text=Shoes" alt="Shoes">
                <h3>Running Shoes</h3>
                <p>Comfortable and stylish running shoes for everyday use.</p>
                <div class="price">$49.99</div>
                <button>Add to Cart</button>
            </div>
            <div class="product">
                <img src="https://via.placeholder.com/120?text=Headphones" alt="Headphones">
                <h3>Wireless Headphones</h3>
                <p>High-quality sound with noise cancellation.</p>
                <div class="price">$89.99</div>
                <button>Add to Cart</button>
            </div>
            <div class="product">
                <img src="https://via.placeholder.com/120?text=Watch" alt="Watch">
                <h3>Smart Watch</h3>
                <p>Track your fitness and stay connected on the go.</p>
                <div class="price">$129.99</div>
                <button>Add to Cart</button>
            </div>
            <div class="product">
                <img src="https://via.placeholder.com/120?text=Backpack" alt="Backpack">
                <h3>Travel Backpack</h3>
                <p>Spacious and durable backpack for all your adventures.</p>
                <div class="price">$39.99</div>
                <button>Add to Cart</button>
            </div>
        </div>
    </div>
    <footer>
        &copy; 2024 My E-Commerce Store
    </footer>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_PAGE)

if __name__ == '__main__':
    app.run(debug=True)