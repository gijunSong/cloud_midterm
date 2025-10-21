FROM python:3.11

WORKDIR /app

COPY api/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY api/ /app/

# Flask가 리슨하는 포트(5000) 노출
EXPOSE 5000

# 컨테이너 시작 시 Flask 앱 실행
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
