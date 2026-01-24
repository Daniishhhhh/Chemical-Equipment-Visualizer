import requests

BASE_URL = "http://127.0.0.1:8000/api"


def get_latest_summary():
    try:
        res = requests.get(f"{BASE_URL}/latest-summary/")
        return res.json()
    except:
        return {"error": "Backend not reachable"}


def get_history():
    try:
        res = requests.get(f"{BASE_URL}/history/")
        return res.json()
    except:
        return {"error": "History fetch failed"}


def upload_csv(file_path):
    try:
        with open(file_path, "rb") as f:
            files = {"file": f}
            res = requests.post(f"{BASE_URL}/upload-csv/", files=files)

        return res.json()

    except Exception as e:
        return {"error": str(e)}


def download_pdf(save_path):
    try:
        res = requests.get(f"{BASE_URL}/generate-pdf/", stream=True)

        if res.status_code != 200:
            return False

        content_type = res.headers.get("Content-Type")

        if "pdf" not in content_type:
            return False

        with open(save_path, "wb") as f:
            for chunk in res.iter_content(chunk_size=8192):
                f.write(chunk)

        return True

    except:
        return False

