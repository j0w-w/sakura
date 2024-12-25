import os

def scan_js(project_name, domain, proxychains):
    if proxychains == 'false':
        os.system(f'cat {project_name}/{domain}/js.txt | mantra -d >> {project_name}/{domain}/scans/mantra.scan')
        os.system(f'cat {project_name}/{domain}/js.txt | nuclei -t ~/nuclei-templates/http/exposures -silent > {project_name}/{domain}/scans/nucleijs.scan')
    elif proxychains == 'true':
        os.system(f'cat {project_name}/{domain}/js.txt | proxychains4 mantra -d >> {project_name}/{domain}/scans/mantra.scan')
        os.system(f'cat {project_name}/{domain}/js.txt | proxychains4 nuclei -t ~/nuclei-templates/http/exposures -silent > {project_name}/{domain}/scans/nucleijs.scan')

def web_application_scan(project_name, domain, proxychains):
    if proxychains == 'false':
        os.system(f'cat {project_name}/{domain}/httprobe.txt | nuclei -t ~/mytemplates -silent > {project_name}/{domain}/scans/nuclei.scan')
    elif proxychains == 'true':
        os.system(f'cat {project_name}/{domain}/httprobe.txt | proxychains4 nuclei -t ~/mytemplates -silent > {project_name}/{domain}/scans/nuclei.scan')

def scan_urls(project_name, scan_type, domains, proxychains):
    if scan_type[3] == '0':
        pass
    elif scan_type[3] == '1':
        for domain in domains:
            scan_js(project_name, domain, proxychains)
    elif scan_type[3] == '2':
        for domain in domains:
            web_application_scan(project_name, domain, proxychains)
    elif scan_type[3] == '3':
        for domain in domains:
            scan_js(project_name, domain, proxychains)
            web_application_scan(project_name, domain, proxychains)