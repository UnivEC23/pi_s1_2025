import time
from init import app, db
import sys
from multiprocessing import Process


if __name__ == "__main__":
    # checar por comandos dps
    # if (len(sys.argv) > 1):
    #     if (sys.argv[1] == "dev"):
    #         pass
    server = Process(target=app.run, args=('localhost', 5000, False))
    server.start()
    # app.run(debug=True, host='127.0.0.1', port=5000)
    with app.app_context():
        db.drop_all()
    time.sleep(1)
    server.terminate()

exit()
