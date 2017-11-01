# attendence-management-system

Installation Instructions
--------------

1. Setup virtual environment for the project.

	* `python3.6 -m <virtualenv_name>`
	* Now in the <b>requirements</b> folder in the project, run `pip install -r requirements/base.txt`.

2. Setup Database for the project.
	* Create Database user `createuser --interactive -P`, (refer chitrank.py settings file).

  * Create Database `createdb --owner <user_of_db> <db_name>`, (refer chitrank.py settings file).

 APIs Documentation
 -----------------
 1. User Create API
    * API Endpoint : http://127.0.0.1:8000/api/v1/users/
    * Method: POST
    * Request JSON:
    ```
    {
      	"username": "sadjka",
      	"password": "abc123",
      	"first_name": "asdasd",
      	"last_name": "asdasd",
      	"email": "abc6@abc.com",
      	"mobile_number": 9769730099,
      	"avatar_url": "http://sad.com",
      	"gender": "M",
      	"age": 27
    }
    ```

    * Response:
    ```
    {
        "meta": {
            "status": 1000,
            "is_error": false,
            "message": ""
        },
        "data": {
            "id": 6,
            "username": "sadjka",
            "first_name": "asdasd",
            "last_name": "asdasd",
            "email": "abc6@abc.com",
            "mobile_number": "9769730099",
            "avatar_url": "http://sad.com",
            "gender": "M",
            "age": 27
        }
    }
    ```

   2. User Login API

      * API Endpoint: http://127.0.0.1:8000/api/v1/user-login/
      * Method: POST
      * Request JSON:
      ```
      {
      	"email": "admin@at.com",
      	"password": "admin123"
      }
      ```
      * Response:
      ```
      {
          "id": 1,
          "username": null,
          "first_name": null,
          "last_name": null,
          "email": "admin@at.com",
          "mobile_number": null,
          "avatar_url": null,
          "gender": null,
          "age": 10
      }
      ```

  3. Student Create API

        * API Endpoint: http://127.0.0.1:8000/api/v1/students/
        * Method: POST
        * Request JSON:
        ```
        {
        	"user": 2
        }
        ```
        * Response:

        ```
        {
            "meta": {
                "status": 1000,
                "is_error": false,
                "message": ""
            },
            "data": {
                "id": 5,
                "user": 2
            }
        }
        ```

  4. Add Student Attendence (supports bulk attendence creation)
      * API Endpoint: http://127.0.0.1:8000/api/v1/attendences/
      * Method: POST
      * Request JSON:
      ```
      [
      	{
      		"student": 5,
      		"date": "2017-11-02",
      		"status": "P" (P -> Present, A -> Absent, L -> Leave)
      	}
      ]
      ```
      * Response:
      ```
      {
        "meta": {
          "status": 1000,
          "is_error": false,
          "message": ""
        },
        "data": "Attendence has been recorded"
      }
      ```
  5. Get Student Attendence by Id:
    * API Endpoint: http://127.0.0.1:8000/api/v1/attendences/get-student-attendence/?student_id=5
    * Method : GET
    * Request Params: student_id
    * Response:
    ```
    {
        "meta": {
            "status": 1000,
            "is_error": false,
            "message": ""
        },
        "data": [
            {
                "id": 1,
                "student": 5,
                "date": "2017-10-31",
                "status": "P"
            },
            {
                "id": 2,
                "student": 5,
                "date": "2017-10-30",
                "status": "P"
            },
            {
                "id": 3,
                "student": 5,
                "date": "2017-10-01",
                "status": "P"
            },
            {
                "id": 4,
                "student": 5,
                "date": "2017-10-29",
                "status": "P"
            },
            {
                "id": 5,
                "student": 5,
                "date": "2017-10-28",
                "status": "P"
            }
        ]
    }
    ```
