import subprocess, datetime, os, termcolor, time

def export_mysql_to_sql():
    HOST, PORT, USER, PASSWORD = os.getenv("HOST"), os.getenv("PORT"), os.getenv("USER"), os.getenv("PASSWORD")
    while True:
        try:
            now = datetime.datetime.now().isoformat().split(".")[0]
            os.mkdir(f"./mysql/{now}")
            command = ["mysql",f"--host={HOST}",f"--port={PORT}",f"--user={USER}",f"--password={PASSWORD}","-e","SHOW DATABASES;"]
            result = subprocess.run(command, capture_output=True, text=True, check=True)
            for db in result.stdout.strip().split("\n")[:]:
                if db not in ["information_schema", "mysql", "performance_schema", "sys", "Database"]:
                    command = ["mysqldump",f"--host={HOST}",f"--port={PORT}",f"--user={USER}",f"--password={PASSWORD}",db]
                    with open(f"./mysql/{now}/{db}.sql", "w") as outfile:
                        subprocess.run(command, stdout=outfile, check=True)
                    print(termcolor.colored(f"database {db} backup successfull at {now}", "green"))
        except subprocess.CalledProcessError as e:
            print(termcolor.colored(f"database {db} backup faild at {now}", "red"))
        time.sleep(3600)

export_mysql_to_sql()
