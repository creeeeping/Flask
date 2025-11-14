import os
import yaml
from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash,
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "db.yaml")

posts_bp = Blueprint("posts", __name__)


def load_posts():
    """YAML 파일에서 전체 글 목록 가져오기"""
    if not os.path.exists(DB_PATH):
        return []

    with open(DB_PATH, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}

    return data.get("posts", [])


def save_posts(posts):
    """글 목록을 YAML 파일에 저장"""
    data = {"posts": posts}
    with open(DB_PATH, "w", encoding="utf-8") as f:
        yaml.safe_dump(data, f, allow_unicode=True)


@posts_bp.route("/")
def index():
    posts = load_posts()
    # 별점이 있다면 평균도 같이 계산 (옵션)
    ratings = [p["rating"] for p in posts if p.get("rating") is not None]
    avg_rating = round(sum(ratings) / len(ratings), 1) if ratings else None

    return render_template("index.html", posts=posts, avg_rating=avg_rating)


@posts_bp.route("/new", methods=["GET", "POST"])
def new_post():
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        content = request.form.get("content", "").strip()
        rating = request.form.get("rating", "").strip()

        if not title or not content:
            flash("제목과 내용을 입력해주세요.", "error")
            return redirect(url_for("posts.new_post"))

        rating_value = None
        if rating:
            try:
                rating_value = int(rating)
            except ValueError:
                flash("별점은 숫자여야 합니다.", "error")
                return redirect(url_for("posts.new_post"))

        posts = load_posts()
        new_id = (posts[-1]["id"] + 1) if posts else 1

        posts.append(
            {
                "id": new_id,
                "title": title,
                "content": content,
                "rating": rating_value,
            }
        )
        save_posts(posts)
        flash("새 글이 등록되었습니다.", "success")
        return redirect(url_for("posts.index"))

    return render_template("new.html")


@posts_bp.route("/<int:post_id>/edit", methods=["GET", "POST"])
def edit_post(post_id):
    posts = load_posts()
    post = next((p for p in posts if p["id"] == post_id), None)

    if not post:
        flash("해당 글을 찾을 수 없습니다.", "error")
        return redirect(url_for("posts.index"))

    if request.method == "POST":
        title = request.form.get("title", "").strip()
        content = request.form.get("content", "").strip()
        rating = request.form.get("rating", "").strip()

        if not title or not content:
            flash("제목과 내용을 입력해주세요.", "error")
            return redirect(url_for("posts.edit_post", post_id=post_id))

        rating_value = None
        if rating:
            try:
                rating_value = int(rating)
            except ValueError:
                flash("별점은 숫자여야 합니다.", "error")
                return redirect(url_for("posts.edit_post", post_id=post_id))

        post["title"] = title
        post["content"] = content
        post["rating"] = rating_value
        save_posts(posts)

        flash("글이 수정되었습니다.", "success")
        return redirect(url_for("posts.index"))

    return render_template("edit.html", post=post)


@posts_bp.route("/<int:post_id>/delete")
def delete_post(post_id):
    posts = load_posts()
    new_posts = [p for p in posts if p["id"] != post_id]

    if len(new_posts) == len(posts):
        flash("삭제할 글을 찾지 못했습니다.", "error")
    else:
        save_posts(new_posts)
        flash("글이 삭제되었습니다.", "success")

    return redirect(url_for("posts.index"))
