@echo off

echo -------------------------------User Info------------------------------- > report.txt
net user %username% >> report.txt
echo -------------------------------System Info------------------------------- >> report.txt
echo current Date and time : %date% %time% >> report.txt
systeminfo >> report.txt
echo -------------------------------Running Proccses------------------------------- >> report.txt
tasklist >> report.txt
echo -------------------------------Running Proccses with associated modules------------------------------- >> report.txt
tasklist /m >> report.txt
echo -------------------------------Running Proccses with associated services------------------------------- >> report.txt
tasklist /svc >> report.txt
echo -------------------------------System variables------------------------------- >> report.txt
set >> report.txt
echo -------------------------------Network Connections------------------------------- >> report.txt
netstat -ano >> report.txt
echo -------------------------------ARP Table------------------------------- >> report.txt
arp -a >> report.txt
echo -------------------------------System Network configuration------------------------------- >> report.txt
ipconfig /all >> report.txt
echo -------------------------------DNS configuration------------------------------- >> report.txt
ipconfig /displaydns >> report.txt
echo -------------------------------Routing Configuration------------------------------- >> report.txt
route print >> report.txt
echo -------------------------------Network Shares------------------------------- >> report.txt
net share >> report.txt
