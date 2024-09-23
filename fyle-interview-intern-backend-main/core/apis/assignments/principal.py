headers={"X-Principal": '{"user_id":5, "principal_id":1}'}


response={
    "data": [
        {
            "created_at": "2024-01-08T07:58:53.131970",
            "id": 1,
            "updated_at": "2024-01-08T07:58:53.131972",
            "user_id": 3
        }
    ]
}
headers={'X-Principal': '{"user_id":5, "principal_id":1}'}

payload={
    "id":  1,
    "grade": "A"
}

response={
    "data": {
        "content": "ESSAY T1",
        "created_at": "2021-09-17T03:14:01.580126",
        "grade": "A",
        "id": 1,
        "state": "GRADED",
        "student_id": 1,
        "teacher_id": 1,
        "updated_at": "2021-09-17T03:20:42.896947"
    }
}
headers={'X-Principal': '{"user_id":5, "principal_id":1}'}

response={
    "data": [
        {
            "content": "ESSAY T1",
            "created_at": "2021-09-17T03:14:01.580126",
            "grade": 'null',
            "id": 1,
            "state": "SUBMITTED",
            "student_id": 1,
            "teacher_id": 1,
            "updated_at": "2021-09-17T03:14:01.584644"
        }
    ]
}