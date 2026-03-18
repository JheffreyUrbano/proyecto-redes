$TTL    604800
@   IN  SOA papadasoftware.com. root.papadasoftware.com. (
                3         ; Serial
           604800
            86400
          2419200
           604800 )

@           IN  NS      servidor1.papadasoftware.com.

;
@           IN  A       192.168.100.2

; servidores
servidor1   IN  A       192.168.100.2
servidor2   IN  A       192.168.100.3

; web
www         IN  CNAME   papadasoftware.com.

; api
api         IN  A       192.168.100.3
