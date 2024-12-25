import os

def gather_urls_actively(project_name, domain, proxychains):
    if proxychains == 'false':
        os.system(f'cat {project_name}/{domain}/httprobe.txt| katana -jc -kf all -ct 60 -silent >> {project_name}/{domain}/urls.txt')
    elif proxychains == 'true':
        os.system(f'cat {project_name}/{domain}/httprobe.txt| proxychains4 katana -jc -kf all -ct 60 -silent >> {project_name}/{domain}/urls.txt')
    
def gather_urls_passively(project_name, domain, proxychains):
    if proxychains == 'false':
        os.system(f'cat {project_name}/{domain}/httprobe.txt | gospider -a -q > {project_name}/{domain}/tmp.txt')
    elif proxychains == 'true':
        os.system(f'cat {project_name}/{domain}/httprobe.txt | proxychains4 gospider -a -q > {project_name}/{domain}/tmp.txt')

    os.system(f"cat {project_name}/{domain}/tmp.txt | awk '{{print $1}}' | grep {domain} >> {project_name}/{domain}/urls.txt")
    os.system(f"cat {project_name}/{domain}/tmp.txt | awk '{{print $2}}' | grep {domain} >> {project_name}/{domain}/urls.txt")
    os.system(f"cat {project_name}/{domain}/tmp.txt | awk '{{print $3}}' | grep {domain} >> {project_name}/{domain}/urls.txt")
    os.system(f"cat {project_name}/{domain}/tmp.txt | awk '{{print $4}}' | grep {domain} >> {project_name}/{domain}/urls.txt")
    os.system(f"cat {project_name}/{domain}/tmp.txt | awk '{{print $5}}' | grep {domain} >> {project_name}/{domain}/urls.txt")
    os.system(f"cat {project_name}/{domain}/tmp.txt | awk '{{print $6}}' | grep {domain} >> {project_name}/{domain}/urls.txt")
    os.system(f"cat {project_name}/{domain}/tmp.txt | awk '{{print $7}}' | grep {domain} >> {project_name}/{domain}/urls.txt")
    os.system(f'rm {project_name}/{domain}/tmp.txt')

def extract_email_and_js(project_name, domain):
    os.system(f'cat {project_name}/{domain}/urls.txt | grep js >> {project_name}/{domain}/js.txt')
    os.system(f'cat {project_name}/{domain}/urls.txt | grep mailto | cut -c 8- >> {project_name}/{domain}/emails.txt')

def gather_urls(project_name, scan_type, domains, proxychains):
    if scan_type[2] == '0':
        pass
    elif scan_type[2] == '1':
        for domain in domains:
            gather_urls_passively(project_name, domain, proxychains)
            extract_email_and_js(project_name, domain)
    elif scan_type[2] == '2':
        for domain in domains:
            gather_urls_actively(project_name, domain, proxychains)
            extract_email_and_js(project_name, domain)
    elif scan_type[2] == '3':
        for domain in domains:
            gather_urls_actively(project_name, domain, proxychains)
            gather_urls_passively(project_name, domain, proxychains)
            extract_email_and_js(project_name, domain)