# Food Detection System


Project Structure
--------
```sh
.
├── app.py
├── models
│   └── succ_300_data_aug_128px.pt
├── README.md
├── requirements.txt
├── runserver.py
├── static
│   ├── css
│   │   ├── bootstrap.min.css
│   │   ├── dropzone.min.css
│   │   └── style.css
│   ├── images
│   │   ├── chai.jpg
│   │   ├── jalebi.jpg
│   │   ├── samosa.jpg
│   │   └── upload.png
│   └── js
│       ├── bootstrap.min.js
│       ├── dropzone.min.js
│       ├── jquery.min.js
│       └── main.js
├── templates
│   └── app.html
└── util.py
```

## Quick Start (Setup in local)

1. Clone the repo
  ```
  $ git clone git@github.com:kp-nagar/Food_Detection.git
  $ cd Food_Detection
  ```


2. Initialize and activate a virtualenv:
  ```
  $ python3 -m venv env
  $ source env/bin/activate
  ```

3. Install the dependencies:
  ```
  $ pip install -r requirements.txt
  ```

5. Run the development server:
  ```
  $ python3 run.py
  ```

6. Navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000)