# Flask API를 완성하세요.
# 요구사항:
# - 데이터 파일 경로: /app/data/expenses.json  (초기 내용: [])
# - GET  /api/records   : 저장된 데이터를 JSON으로 반환
# - POST /api/records   : {title, amount, date} 저장 (유효성 검사 포함)
# - GET  /api/summary   : {count, total} 반환
# - GET  /api/download  : expenses.json 파일 다운로드

from flask import Flask  #, request, jsonify, send_file
from pathlib import Path
import json, os

app = Flask(__name__)

DATA_PATH = Path("/app/data/expenses.json")
DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
if not DATA_PATH.exists():
    DATA_PATH.write_text("[]", encoding="utf-8")

@app.get("/healthz")
def healthz():
    return "ok", 200

# 아래 엔드포인트들을 구현하세요. ( 함수명은 임의로 지정한 내용임 )
# @app.get("/api/records")
# def get_records():
#     raise NotImplementedError

# @app.post("/api/records")
# def add_record():
#     raise NotImplementedError

# @app.get("/api/summary")
# def summary():
#     raise NotImplementedError

# @app.get("/api/download")
# def download_json():
#     raise NotImplementedError

if __name__ == "__main__":
    # 적절한 포트(예: 5000)로 0.0.0.0 에서 실행
    app.run(host="0.0.0.0", port=5000)