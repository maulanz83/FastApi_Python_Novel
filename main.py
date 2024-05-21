# main.py

from fastapi import FastAPI, HTTPException
import uvicorn

# Membuat instance dari FastAPI
app = FastAPI()

# Data dummy untuk novel, penulis, dan penerbit
novels = [
    {"id": 1, "title": "To Kill a Mockingbird", "author_id": 1, "publisher_id": 1},
    {"id": 2, "title": "1984", "author_id": 2, "publisher_id": 2},
    {"id": 3, "title": "Pride and Prejudice", "author_id": 3, "publisher_id": 3},
    {"id": 4, "title": "The Great Gatsby", "author_id": 4, "publisher_id": 4},
    {"id": 5, "title": "Moby-Dick", "author_id": 5, "publisher_id": 5},
]

authors = [
    {"id": 1, "name": "Harper Lee"},
    {"id": 2, "name": "George Orwell"},
    {"id": 3, "name": "Jane Austen"},
    {"id": 4, "name": "F. Scott Fitzgerald"},
    {"id": 5, "name": "Herman Melville"},
]

publishers = [
    {"id": 1, "name": "J.B. Lippincott & Co."},
    {"id": 2, "name": "Secker & Warburg"},
    {"id": 3, "name": "T. Egerton"},
    {"id": 4, "name": "Charles Scribner's Sons"},
    {"id": 5, "name": "Harper & Brothers"},
]

# Endpoint root
@app.get('/')
async def root():
    return [
        {"id": 1, "nama": "Endpoint Novels", "endpoint": "/novels"},
        {"id": 2, "nama": "Endpoint Novel Detail", "endpoint": "/novels/{novel_id}"},
        {"id": 3, "nama": "Endpoint Authors", "endpoint": "/authors"},
        {"id": 4, "nama": "Endpoint Publishers", "endpoint": "/publishers"},
        {"id": 5, "nama": "Endpoint Add Novel", "endpoint": "/novels"},
        {"id": 6, "nama": "Endpoint Delete Novel", "endpoint": "/novels/{novel_id}"}
    ]

# Endpoint untuk mendapatkan data novel
@app.get('/novels')
async def get_novels():
    # Menyederhanakan data novel agar hanya mengandung id dan title
    simplified_novels = [
        {"id": novel["id"], "title": novel["title"]}
        for novel in novels
    ]
    return {
        "Message": "Success fetch novel data",
        "Data": simplified_novels
    }

# Endpoint untuk mendapatkan detail novel berdasarkan id
@app.get('/novels/{novel_id}')
async def get_novel(novel_id: int):
    # Mencari novel berdasarkan id
    for novel in novels:
        if novel["id"] == novel_id:
            return {
                "Message": "Success fetch novel detail",
                "Data": novel
            }
    # Jika novel tidak ditemukan, mengembalikan HTTP 404
    raise HTTPException(status_code=404, detail="Novel not found")

# Endpoint untuk mendapatkan data penulis
@app.get('/authors')
async def get_authors():
    return {
        "Message": "Success fetch author data",
        "Data": authors
    }

# Endpoint untuk mendapatkan data penerbit
@app.get('/publishers')
async def get_publishers():
    return {
        "Message": "Success fetch publisher data",
        "Data": publishers
    }

# Endpoint untuk menambahkan novel baru
@app.post('/novels')
async def add_novel(novel: dict):
    new_novel = {
        "id": len(novels) + 1,
        "title": novel.get("title"),
        "author_id": novel.get("author_id"),
        "publisher_id": novel.get("publisher_id")
    }
    novels.append(new_novel)
    return {
        "Message": "Success add novel",
        "Data": new_novel
    }

# Endpoint untuk menghapus novel berdasarkan id
@app.delete('/novels/{novel_id}')
async def delete_novel(novel_id: int):
    for novel in novels:
        if novel["id"] == novel_id:
            novels.remove(novel)
            return {"Message": "Novel deleted successfully"}
    raise HTTPException(status_code=404, detail="Novel not found")

# Menjalankan aplikasi menggunakan Hypercorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
