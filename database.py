import sqlite3
from datetime import datetime


DATABASE_NAME = "study_material.db"


def create_database():

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            file_name TEXT,
            transformation TEXT,
            difficulty TEXT,
            question_count INTEGER,
            result TEXT,
            created_at TEXT
        )
    """)

    connection.commit()
    connection.close()


def save_result(
    file_name,
    transformation,
    difficulty,
    question_count,
    result
):

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO history
        (
            file_name,
            transformation,
            difficulty,
            question_count,
            result,
            created_at
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        file_name,
        transformation,
        difficulty,
        question_count,
        result,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    connection.commit()
    connection.close()


def get_history():

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            id,
            file_name,
            transformation,
            difficulty,
            question_count,
            result,
            created_at
        FROM history
        ORDER BY id DESC
    """)

    history = cursor.fetchall()

    connection.close()

    return history


def delete_history(record_id):

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM history WHERE id = ?",
        (record_id,)
    )

    connection.commit()
    connection.close()