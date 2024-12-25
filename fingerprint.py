import os

def port_scan(project_name, domain, proxychains):
    if proxychains == 'false':
        os.system(f'cat {project_name}/{domain}/subdomains.txt | naabu -Pn -top-ports 1000 -silent >> {project_name}/{domain}/a.txt')
        os.system(f'cat {project_name}/{domain}/subdomains.txt | naabu -Pn -p 66,80,81,443,445,457,1080,1100,1241,1352,1433,1434,1521,1944,2301,3000,3128,3306,4000,4001,4002,4100,5000,5432,5800,5801,5802,6346,6347,7001,7002,8000,8080,8443,8888,30821 -silent >> {project_name}/{domain}/a.txt')
        os.system(f'cat {project_name}/{domain}/a.txt | sort -u > {project_name}/{domain}/open_ports.txt')
        os.system(f'rm {project_name}/{domain}/a.txt')
    elif proxychains == 'true':
        os.system(f'proxychains4 cat {project_name}/{domain}/subdomains.txt | naabu -Pn -top-ports 1000 -silent >> {project_name}/{domain}/a.txt')
        os.system(f'proxychains4 cat {project_name}/{domain}/subdomains.txt | naabu -Pn -p 66,80,81,443,445,457,1080,1100,1241,1352,1433,1434,1521,1944,2301,3000,3128,3306,4000,4001,4002,4100,5000,5432,5800,5801,5802,6346,6347,7001,7002,8000,8080,8443,8888,30821 -silent >> {project_name}/{domain}/a.txt')
        os.system(f'proxychains4 cat {project_name}/{domain}/a.txt | sort -u > {project_name}/{domain}/open_ports.txt')
        os.system(f'proxychains4 rm {project_name}/{domain}/a.txt')

def get_web_servers(project_name, domain, proxychains):
    if proxychains == 'false':
        os.system(f'cat {project_name}/{domain}/open_ports.txt | httprobe -c 50 > {project_name}/{domain}/httprobe.txt')
    elif proxychains == 'true':
        os.system(f'cat {project_name}/{domain}/open_ports.txt | proxychains4 httprobe -c 50 > {project_name}/{domain}/httprobe.txt')

def fingerprint_web_servers(project_name, domain, proxychains):
    if proxychains == 'false':
        os.system(f'cat {project_name}/{domain}/httprobe.txt | httpx -fr -sc -title -tech-detect -silent -ip -server > {project_name}/{domain}/httpx.txt')
    elif proxychains == 'true':
        os.system(f'cat {project_name}/{domain}/httprobe.txt | proxychains4 httpx -fr -sc -title -tech-detect -silent -ip -server > {project_name}/{domain}/httpx.txt')

def fingerprint_subdomains(project_name, scan_type, domains, proxychains):
    if scan_type[1] == '0':
        pass
    elif scan_type[1] == '1':
        for domain in domains:
            port_scan(project_name, domain, proxychains)
            get_web_servers(project_name, domain, proxychains)
            fingerprint_web_servers(project_name, domain, proxychains)