#!/bin/python3
import sys
import os
from subdomains import *
from fingerprint import *
from urls import *
from scanning import *

def banner():
    print('    ██████  ▄▄▄       ██ ▄█▀ █    ██  ██▀███   ▄▄▄      ')
    print('▒██    ▒ ▒████▄     ██▄█▒  ██  ▓██▒▓██ ▒ ██▒▒████▄      ')
    print('░ ▓██▄   ▒██  ▀█▄  ▓███▄░ ▓██  ▒██░▓██ ░▄█ ▒▒██  ▀█▄    ')
    print('▒   ██▒░██▄▄▄▄██ ▓██ █▄ ▓▓█  ░██░▒██▀▀█▄  ░██▄▄▄▄██     ')
    print('▒██████▒▒ ▓█   ▓██▒▒██▒ █▄▒▒█████▓ ░██▓ ▒██▒ ▓█   ▓██▒  ')
    print('▒ ▒▓▒ ▒ ░ ▒▒   ▓▒█░▒ ▒▒ ▓▒░▒▓▒ ▒ ▒ ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░  ')
    print('░ ░▒  ░ ░  ▒   ▒▒ ░░ ░▒ ▒░░░▒░ ░ ░   ░▒ ░ ▒░  ▒   ▒▒ ░  ')
    print('░  ░  ░    ░   ▒   ░ ░░ ░  ░░░ ░ ░   ░░   ░   ░   ▒     ')
    print('    ░        ░  ░░  ░      ░        ░           ░  ░    \n')
    print('bug bounty recon and fingerprinting framework created by j0w-w\n')

def project_setup(project_name, domains):
    os.system(f'mkdir {project_name}')
    os.system(f'mkdir ./{project_name}/scans')
    for domain in domains:
        os.system('mkdir ./' + project_name + '/' + domain)
        os.system('mkdir ./' + project_name + '/' + domain + '/scans')
        os.system('mkdir ./' + project_name + '/' + domain + '/sources')
        os.system('echo ' + domain + ' >> ./' + project_name + '/roots.txt')

def combine_results(project_name, domains):
    for domain in domains:
        os.system(f'cat {project_name}/{domain}/subdomains.txt >> {project_name}/subdomains.txt')
        os.system(f'cat {project_name}/{domain}/urls.txt >> {project_name}/urls.txt')
        os.system(f'cat {project_name}/{domain}/open_ports.txt >> {project_name}/open_ports.txt')
        os.system(f'cat {project_name}/{domain}/httprobe.txt >> {project_name}/httprobe.txt')
        os.system(f'cat {project_name}/{domain}/httpx.txt >> {project_name}/httpx.txt')
        os.system(f'cat {project_name}/{domain}/ips.txt >> {project_name}/ips.txt')
        os.system(f'cat {project_name}/{domain}/urls.txt >> {project_name}/urls.txt')
        os.system(f'cat {project_name}/{domain}/js.txt >> {project_name}/js.txt')
        os.system(f'cat {project_name}/{domain}/emails.txt >> {project_name}/emails.txt')
        os.system(f'cat {project_name}/{domain}/scans/mantra.scan >> {project_name}/scans/mantra.scan')
        os.system(f'cat {project_name}/{domain}/scans/nuclei.scan >> {project_name}/scans/nuclei.scan')

def main():
    banner()
    try:
        project_name = sys.argv[1]
        scan_type = sys.argv[2]
        proxychains = sys.argv[3]
        domains = []
        for line in sys.stdin:
            line = line.strip('\n')
            domains.append(line)
    except:
        exit()
    
    project_setup(project_name, domains)
    get_subdomains(project_name, scan_type, domains, proxychains)
    fingerprint_subdomains(project_name, scan_type, domains, proxychains)
    gather_urls(project_name, scan_type, domains, proxychains)
    scan_urls(project_name, scan_type, domains, proxychains)
    combine_results(project_name, domains)

main()