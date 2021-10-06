import scanner

target_url = "http://10.0.2.8/dvwa/"
links_to_ignore = ["http://10.0.2.8/dvwa/logout.php"]
data_dict = {"username": "admin", "password": "password", "login": "submit"}


vuln_scanner = scanner.Scanner(target_url, links_to_ignore)
vuln_scanner.session.post("http://10.0.2.8/dvwa/login.php", data=data_dict)

vuln_scanner.crawl()
vuln_scanner.run_scanner()
