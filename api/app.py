# Flask API를 완성하세요.
# 요구사항:
# - 데이터 파일 경로: /app/data/expenses.json  (초기 내용: [])
# - GET  /api/records   : 저장된 데이터를 JSON으로 반환
# - POST /api/records   : {title, amount, date} 저장 (유효성 검사 포함)
# - GET  /api/summary   : {count, total} 반환
# - GET  /api/download  : expenses.json 파일 다운로드

from flask import Flask, request, jsonify, send_file
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

# GET /api/records : 저장된 데이터를 JSON으로 반환
@app.get("/api/records")
def get_records():
    try:
        with open(DATA_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# POST /api/records : {title, amount, date} 저장 (유효성 검사 포함)
@app.post("/api/records")
def add_record():
    try:
        record = request.get_json()
        
        # 유효성 검사
        if not record or not isinstance(record, dict):
            return jsonify({"error": "Invalid JSON format"}), 400
        
        title = record.get("title")
        amount = record.get("amount")
        date = record.get("date")
        
        # 필수 필드 확인
        if not title or not isinstance(title, str) or not title.strip():
            return jsonify({"error": "title is required and must be a non-empty string"}), 400
        
        if amount is None or not isinstance(amount, (int, float)) or amount < 0:
            return jsonify({"error": "amount is required and must be a non-negative number"}), 400
        
        if not date or not isinstance(date, str):
            return jsonify({"error": "date is required and must be a string"}), 400
        
        # 기존 데이터 읽기
        with open(DATA_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        # 새 레코드 추가
        data.append({
            "title": title.strip(),
            "amount": amount,
            "date": date
        })
        
        # 파일에 저장
        with open(DATA_PATH, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        return jsonify({"message": "Record added successfully"}), 201
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# GET /api/summary : {count, total} 반환
@app.get("/api/summary")
def summary():
    try:
        with open(DATA_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        count = len(data)
        total = sum(record.get("amount", 0) for record in data)
        
        return jsonify({
            "count": count,
            "total": total
        }), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# GET /api/download : expenses.json 파일 다운로드
@app.get("/api/download")
def download_json():
    try:
        if not DATA_PATH.exists():
            return jsonify({"error": "File not found"}), 404
        
        return send_file(
            DATA_PATH,
            as_attachment=True,
            download_name="expenses.json",
            mimetype="application/json"
        )
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # 적절한 포트(예: 5000)로 0.0.0.0 에서 실행
    app.run(host="0.0.0.0", port=5000)
