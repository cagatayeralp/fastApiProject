from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

test_object_correct = {
  "json_input": [
    {
      "productId": 1,
      "name": "Samosa",
      "description": "Praesent scelerisque, mi sed ultrices condimentum, lacus ipsum viverra massa, in lobortis sapien eros in arcu. Quisque vel lacus ac magna vehicula sagittis ut non lacus.<br/>Sed volutpat tellus lorem, lacinia tincidunt tellus varius nec. Vestibulum arcu turpis, facilisis sed ligula ac, maximus malesuada neque. Phasellus commodo cursus pretium.",
      "price": 15,
      "categoryName": "Appetizer",
      "imageUrl": "https://cagataydotnetmastery.blob.core.windows.net/mango/14.jpg"
    },
    {
      "productId": 2,
      "name": "Paneer Tikka",
      "description": "Praesent scelerisque, mi sed ultrices condimentum, lacus ipsum viverra massa, in lobortis sapien eros in arcu. Quisque vel lacus ac magna vehicula sagittis ut non lacus.<br/>Sed volutpat tellus lorem, lacinia tincidunt tellus varius nec. Vestibulum arcu turpis, facilisis sed ligula ac, maximus malesuada neque. Phasellus commodo cursus pretium.",
      "price": 13.99,
      "categoryName": "Appetizer",
      "imageUrl": "https://cagataydotnetmastery.blob.core.windows.net/mango/12.jpg"
    },
    {
      "productId": 3,
      "name": "Sweet Pie",
      "description": "Praesent scelerisque, mi sed ultrices condimentum, lacus ipsum viverra massa, in lobortis sapien eros in arcu. Quisque vel lacus ac magna vehicula sagittis ut non lacus.<br/>Sed volutpat tellus lorem, lacinia tincidunt tellus varius nec. Vestibulum arcu turpis, facilisis sed ligula ac, maximus malesuada neque. Phasellus commodo cursus pretium.",
      "price": 10.99,
      "categoryName": "Dessert",
      "imageUrl": "https://cagataydotnetmastery.blob.core.windows.net/mango/11.jpg"
    },
    {
      "productId": 4,
      "name": "Pav Bhaji",
      "description": "Praesent scelerisque, mi sed ultrices condimentum, lacus ipsum viverra massa, in lobortis sapien eros in arcu. Quisque vel lacus ac magna vehicula sagittis ut non lacus.<br/>Sed volutpat tellus lorem, lacinia tincidunt tellus varius nec. Vestibulum arcu turpis, facilisis sed ligula ac, maximus malesuada neque. Phasellus commodo cursus pretium.",
      "price": 15,
      "categoryName": "Entree",
      "imageUrl": "https://cagataydotnetmastery.blob.core.windows.net/mango/13.jpg"
    }
  ]
}

def test_stream():
    response = client.post(
        "/convert_excel",
        json=test_object_correct,
    )
    assert response.status_code == 200

def test_csv_correct():
    response = client.post(
        "/convert_csv",
        json=test_object_correct,
    )
    assert response.status_code == 200

def test_pdf_correct():
    response = client.post(
        "/convert_pdf",
        json=test_object_correct,
    )
    assert response.status_code == 200



