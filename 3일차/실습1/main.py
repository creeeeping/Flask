from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

# 데이터베이스 연걸
engine = create_engine("sqlite:///user.db", echo=True)

# Base 클래스 정의
Base = declarative_base()

# 모델 (테이블) 정의
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    def __repr__(self): # 파이썬 객체를 개발자 친화적 문자열로 표현
        return f"<User(id={self.id}, name='{self.name}')>"

# DB 안에 테이블 생성
Base.metadata.create_all(bind=engine)

# 세션 준비
SessionLocal = sessionmaker(bind=engine)


##### 단일 데이터 핸들링
def run_single():
    db = SessionLocal()

    # Insert
    new_user = User(name="소민")
    db.add(new_user)
    db.commit()
    print("사용자 추가:", new_user)

    # Select
    user = db.query(User).first()
    print("사용자 검색:", user)

    # Update
    user = db.query(User).first()
    if user:
        user.name = "건우"
        db.commit()
        print("사용자 변경:", user)

    # Delete
    user = db.query(User).first()
    if user:
        db.delete(user)
        db.commit()
        print("사용자 삭제~~~")

    db.close()


#### 복수 데이터 핸들링
db = SessionLocal()

# Insert
users = [User(name="BE_종찬"),User(name="BE_동석"), User(name="건영")]
db.add_all(users)
db.commit()
print("여러 사용자 추가:", users)

# Select
### 전체 데이터 조회
users = db.query(User).all()
for user in users:
    print(user.name)

### 조건 검색
find_user = db.query(User).filter(User.name == "건영").first()
print("조건 조회:", find_user)

### 패턴 검색
find_users = db.query(User).filter(User.name.like("BE_%")).all()
print("패턴 검색:", find_users)

# Update
users = db.query(User).all()
for u in users:
    u.name = u.name + "_New"
db.commit()
print("업데이트 완료", users)

# Delete
db.query(User).delete()
db.commit()
print("모든 유저 삭제 끝")
users = db.query(User).all
if users:
    print("아직 있습니다.", users)
else:
    print("데이터 모두 삭제 되었습니다.")




db.close()