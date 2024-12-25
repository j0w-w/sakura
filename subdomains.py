import os

def passive_subdomains_from_sources(project_name, domain):
    os.system(f'subfinder -d {domain} -recursive -all -silent -o ./{project_name}/{domain}/sources/subfinder.txt')
    os.system(f'assetfinder --subs-only {domain} > ./{project_name}/{domain}/sources/assetfinder.txt')
    os.system(f'findomain -t {domain} | grep {domain} > ./{project_name}/{domain}/sources/findomain.txt')
    os.system(f'github-subdomains -d {domain} -t ./github-tokens.txt')
    os.system(f'mv ./{domain}.txt ./{project_name}/{domain}/sources/github.txt')

def resolve_subdomains(project_name, domain):
    os.system(f'cat {project_name}/{domain}/sources/* | grep {domain} | sort -u > {project_name}/{domain}/d.txt')
    os.system(f'puredns resolve {project_name}/{domain}/d.txt -r ./r.txt -w {project_name}/{domain}/subdomains.txt')
    os.system(f'rm {project_name}/{domain}/d.txt')

def brute_subdomains(project_name, domain):
    os.system(f'dnsx -silent -d {domain} -r ~/resolvers.txt -w ./wordlist.txt > ./{project_name}/{domain}/sources/brute.txt')

def reverse_dns(project_name, domain):
    os.system(f'cat {project_name}/{domain}/subdomains.txt | dnsx -ro -silent > {project_name}/{domain}/ips.txt')
    os.system(f'cp {project_name}/{domain}/ips.txt {project_name}/{domain}/tmp.txt')
    os.system(f'sed -i \'s/$/\\/24/\' {project_name}/{domain}/tmp.txt')
    os.system(f'cat {project_name}/{domain}/tmp.txt | dnsx -resp-only -ptr -silent > {project_name}/{domain}/sources/reverse.txt')
    os.system(f'rm {project_name}/{domain}/tmp.txt')

def get_subdomains(project_name, scan_type, domains, proxychains):
    if scan_type[0] == '0':
        pass
    elif scan_type[0] == '1':
        for domain in domains:
            passive_subdomains_from_sources(project_name, domain)
            resolve_subdomains(project_name, domain)
    elif scan_type[0] == '2':
        for domain in domains:
            passive_subdomains_from_sources(project_name, domain)
            brute_subdomains(project_name, domain)
            resolve_subdomains(project_name, domain)
    elif scan_type[0] == '3':
        for domain in domains:
            brute_subdomains(project_name, domain)
            resolve_subdomains(project_name, domain)
    elif scan_type[0] == '4':
        for domain in domains:
            passive_subdomains_from_sources(project_name, domain)
            brute_subdomains(project_name, domain)
            resolve_subdomains(project_name, domain)
            reverse_dns(project_name, domain)
            resolve_subdomains(project_name, domain)
    elif scan_type[0] == '5':
        for domain in domains:
            passive_subdomains_from_sources(project_name, domain)
            resolve_subdomains(project_name, domain)
            reverse_dns(project_name, domain)
            resolve_subdomains(project_name, domain)
    elif scan_type[0] == '6':
        for domain in domains:
            brute_subdomains(project_name, domain)
            resolve_subdomains(project_name, domain)
            reverse_dns(project_name, domain)
            resolve_subdomains(project_name, domain)