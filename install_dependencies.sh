#!/bin/sh

if [ $(id -u) -ne 0 ]
  then echo Please run as root.
  exit
fi

sudo apt-get install proxychains4
sudo apt-get install golang

go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
go install github.com/tomnomnom/assetfinder@latest
sudo apt-get install findomain
go install github.com/gwen001/github-subdomains@latest
go install github.com/d3mondev/puredns/v2@latest
go install -v github.com/projectdiscovery/dnsx/cmd/dnsx@latest

go install -v github.com/projectdiscovery/naabu/v2/cmd/naabu@latest
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest
go install github.com/tomnomnom/httprobe@latest

GO111MODULE=on go install github.com/jaeles-project/gospider@latest
CGO_ENABLED=1 go install github.com/projectdiscovery/katana/cmd/katana@latest

go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest
go install github.com/Brosck/mantra@latest

sudo mv ~/go/bin/* /bin/