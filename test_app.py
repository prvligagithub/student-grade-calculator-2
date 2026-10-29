from app import app

def test_result():
    c = app.test_client()
    r = c.get("/result?m1=80&m2=70&m3=90")
    assert r.data == b"Total: 240.0, Average: 80.0"

